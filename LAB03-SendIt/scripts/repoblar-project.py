#!/usr/bin/env python3
"""Repuebla un Project v2 con las columnas, campos y las 47 tarjetas del Caso #3.
Uso: python3 repoblar.py <owner> <numero-de-project>"""
import json, subprocess, sys

OWNER, NUM = sys.argv[1], sys.argv[2]

def sh(*a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode: print("ERROR:", r.stderr[:500], file=sys.stderr); sys.exit(1)
    return r.stdout

def gql(q):
    d = json.loads(sh("gh","api","graphql","-f",f"query={q}"))
    if "errors" in d: print("ERROR:", d["errors"][0]["message"], file=sys.stderr); sys.exit(1)
    return d["data"]

proj = next(p for p in json.loads(sh("gh","project","list","--owner",OWNER,"--format","json"))["projects"]
            if str(p["number"]) == NUM)
PID = proj["id"]
print(f"  proyecto: {proj['title']}  ({proj['url']})")

# 1. columnas de Status
fields = json.loads(sh("gh","project","field-list",NUM,"--owner",OWNER,"--format","json"))["fields"]
F_STATUS = next(f["id"] for f in fields if f["name"] == "Status")
COLS = [("Backlog","GRAY","Identificado. Todavia no comprometido"),
        ("Ready","BLUE","Tiene todo lo que necesita para empezar"),
        ("In progress","YELLOW","Alguien lo esta haciendo ahora"),
        ("In review","ORANGE","Hecho. Espera revision, EVAL o aprobacion del PR"),
        ("Blocked","RED","Espera una decision, un dato o un acceso externo"),
        ("Done","GREEN","Cerrado y verificado")]
opts = ",".join('{name:"%s",color:%s,description:"%s"}' % c for c in COLS)
r = gql('mutation{updateProjectV2Field(input:{fieldId:"%s",singleSelectOptions:[%s]})'
        '{projectV2Field{...on ProjectV2SingleSelectField{options{id name}}}}}' % (F_STATUS, opts))
ST = {o["name"]: o["id"] for o in r["updateProjectV2Field"]["projectV2Field"]["options"]}
print(f"  columnas: {' → '.join(ST)}")

# 2. campos Paso y Prioridad
PASOS = ["R — Requerimientos","E — Estimar","D — Diseñar servicio","A — Modelo de datos",
         "L — Componentes","E — Escalar","EVAL","Meta","Entrega"]
def campo(nombre, opciones):
    ex = [f for f in fields if f["name"] == nombre]
    if ex: return ex[0]["id"], {o["name"]: o["id"] for o in ex[0].get("options",[])}
    d = json.loads(sh("gh","project","field-create",NUM,"--owner",OWNER,"--name",nombre,
                      "--data-type","SINGLE_SELECT","--single-select-options",",".join(opciones),
                      "--format","json"))
    fl = json.loads(sh("gh","project","field-list",NUM,"--owner",OWNER,"--format","json"))["fields"]
    f = next(x for x in fl if x["id"] == d["id"])
    return f["id"], {o["name"]: o["id"] for o in f["options"]}
F_PASO, O_PASO = campo("Paso", PASOS)
F_PRIO, O_PRIO = campo("Prioridad", ["P0","P1","P2"])
print(f"  campos: Paso ({len(O_PASO)} opciones) · Prioridad ({len(O_PRIO)})")

# 3. tarjetas
LBL2PASO = {"paso:R":"R — Requerimientos","paso:E-estimar":"E — Estimar","paso:D":"D — Diseñar servicio",
            "paso:A":"A — Modelo de datos","paso:L":"L — Componentes","paso:E-escalar":"E — Escalar",
            "paso:eval":"EVAL","paso:meta":"Meta","paso:entrega":"Entrega"}
STATUS_POR_ISSUE = {1:"In review",2:"Done",3:"Done",
                    4:"Ready",5:"Ready",6:"Ready",7:"Ready",8:"Ready",9:"Ready",10:"Ready"}

issues = sorted(json.loads(sh("gh","issue","list","-L","100","--state","all",
                              "--json","number,id,title,labels",
                              "-R","LuisMUtec/SWA-LAB03-SendIt")), key=lambda i: i["number"])
items = {}
for c in range(0, len(issues), 12):
    muts = "\n".join('a%d: addProjectV2ItemById(input:{projectId:"%s",contentId:"%s"}){item{id}}'
                     % (i["number"], PID, i["id"]) for i in issues[c:c+12])
    for k, v in gql("mutation{\n"+muts+"\n}").items(): items[int(k[1:])] = v["item"]["id"]
print(f"  tarjetas: {len(items)}")

ops = []
def setv(al, it, fld, opt):
    return ('%s: updateProjectV2ItemFieldValue(input:{projectId:"%s",itemId:"%s",fieldId:"%s",'
            'value:{singleSelectOptionId:"%s"}}){projectV2Item{id}}' % (al, PID, it, fld, opt))
for i in issues:
    n, it = i["number"], items[i["number"]]
    labs = [l["name"] for l in i["labels"]]
    ops.append(setv(f"s{n}", it, F_STATUS, ST[STATUS_POR_ISSUE.get(n, "Backlog")]))
    for l in labs:
        if l in LBL2PASO: ops.append(setv(f"p{n}", it, F_PASO, O_PASO[LBL2PASO[l]])); break
    for l in labs:
        if l in O_PRIO: ops.append(setv(f"r{n}", it, F_PRIO, O_PRIO[l])); break
for c in range(0, len(ops), 20):
    gql("mutation{\n" + "\n".join(ops[c:c+20]) + "\n}")
print(f"  campos fijados: {len(ops)}")

# 4. vistas
# El agrupamiento no se puede fijar por API (solo visibleFieldIds), pero una vista
# de tablero agrupa por Status por su cuenta: las seis columnas salen solas.
F_TITLE  = next(f["id"] for f in fields if f["name"] == "Title")
F_LABELS = next(f["id"] for f in fields if f["name"] == "Labels")
vistas = gql('{node(id:"%s"){...on ProjectV2{views(first:20){nodes{id name layout}}}}}' % PID
             )["node"]["views"]["nodes"]
board = next((v["id"] for v in vistas if v["layout"] == "BOARD_LAYOUT"), None)
table = next((v["id"] for v in vistas if v["layout"] == "TABLE_LAYOUT"), None)
if not table:
    table = gql('mutation{createProjectV2View(input:{projectId:"%s",name:"Por paso R.E.D.A.L.E.",'
                'layout:TABLE_LAYOUT}){projectV2View{id}}}' % PID
                )["createProjectV2View"]["projectV2View"]["id"]
if not board:
    board = gql('mutation{createProjectV2View(input:{projectId:"%s",name:"Tablero",'
                'layout:BOARD_LAYOUT}){projectV2View{id}}}' % PID
                )["createProjectV2View"]["projectV2View"]["id"]
campos = '","'.join([F_TITLE, F_PASO, F_PRIO, F_STATUS, F_LABELS])
gql('mutation{'
    'b: updateProjectV2View(input:{viewId:"%s",name:"Tablero"}){projectV2View{name}}'
    't: updateProjectV2View(input:{viewId:"%s",name:"Por paso R.E.D.A.L.E.",'
    'configuration:{visibleFieldIds:["%s"]}}){projectV2View{name}}}' % (board, table, campos))
print("  vistas: Tablero (board) · Por paso R.E.D.A.L.E. (table)")

print(f"\n  ✓ listo → {proj['url']}")
print("     El agrupamiento de la vista de tabla se elige a mano: "
      "Group by → Paso. Un clic, la API no lo expone.")
