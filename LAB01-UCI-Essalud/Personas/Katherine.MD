# Katherine Ttito — Coordinadora de TI de Red Asistencial

> Persona ancla de las **metas de rendimiento, disponibilidad y escalamiento**, y del despliegue de **P3**.

## Perfil

| Campo | Valor |
|---|---|
| Edad | 35 |
| Rol | Coordinadora de Tecnologías de Información, Red Prestacional Lima |
| Institución | Oficina de TI de la Red — responsable de los hospitales del piloto |
| Turno / horario | Administrativo 08:00 – 17:00, con disponibilidad en llamada |
| Antigüedad | 7 años en la Red |
| Nivel técnico | Alto |
| Dispositivo principal | Laptop de trabajo; acceso a consolas de monitoreo |

## Contexto

Katherine responde por el funcionamiento del sistema en todos los hospitales del piloto, con un equipo
de cinco personas para una red que ya tiene decenas de sedes y que debe crecer un orden de magnitud
cada seis meses. No tiene personal de TI presencial en cada hospital: en la mayoría, el "soporte local"
es un técnico que atiende también impresoras y redes.

El parque de máquinas es heterogéneo y viejo: PCs con Windows desactualizado, navegadores que no se
pueden actualizar por dependencias de otros sistemas, y enlaces de internet de calidad muy dispar entre
un hospital de Lima centro y uno periférico. La UCI no tiene ventana de mantenimiento: es un servicio
24/7 donde no existe "vamos a apagarlo el domingo de madrugada".

Cada nueva versión desplegada hoy implica coordinar con cada sede. Cuando algo falla de noche, se entera
por una llamada de la unidad, no por una alerta del sistema.

## Objetivos

- Desplegar actualizaciones sin tocar máquina por máquina ni interrumpir la operación clínica.
- Enterarse de una falla **antes** de que la llame una enfermera.
- Sostener la disponibilidad de 99.9 % y recuperar el servicio en menos de 5 minutos.
- Crecer de 1K a 100K sedes sin multiplicar el equipo por cien.
- Cumplir con protección de datos y trazabilidad de accesos sin frenar la atención.

## Frustraciones / Dolores actuales

- Actualizaciones que requieren intervención presencial en cada hospital.
- Sistemas que asumen conectividad estable y se vuelven inservibles cuando el enlace cae.
- Enterarse de las caídas por teléfono y no por monitoreo.
- No poder reproducir un incidente porque no hay trazas suficientes.
- Software que exige requisitos de hardware que la red no tiene y no va a tener pronto.
- Que el crecimiento del piloto se traduzca directamente en más carga operativa manual.

## Tareas críticas en el sistema

| # | Tarea | Frecuencia | Criticidad |
|---|---|---|---|
| 1 | Desplegar nuevas versiones en todas las sedes | Quincenal | Alta |
| 2 | Monitorear disponibilidad y latencia por sede | Continuo | Crítica |
| 3 | Detectar y diagnosticar incidentes en producción | Semanal | Crítica |
| 4 | Ejecutar y verificar la recuperación ante caída | Ante cada incidente | Crítica |
| 5 | Incorporar un nuevo hospital a la red del sistema | Creciente | Alta |
| 6 | Gestionar identidades, roles y auditoría de accesos | Continuo | Alta |
| 7 | Reportar cumplimiento de SLA a la Dirección de Red | Mensual | Media |

## Escenario clave

**Mes 7 del piloto.** El sistema pasó de 1K a algo más de 30K sedes activas y sigue creciendo. Un
martes a las 21:00, las notificaciones de escalamiento empiezan a llegar con dos y tres minutos de
retraso en un subconjunto de hospitales. Nadie reporta "caída": el sistema responde, solo que tarde.

Katherine necesita saber, sin ir hospital por hospital: qué sedes están afectadas, si es un problema de
la red del hospital o del servicio central, desde cuándo, y si el retraso llegó a comprometer algún
escalamiento clínico real. Necesita también poder degradar el servicio de forma controlada —mantener
las notificaciones críticas y postergar lo secundario— en vez de que se caiga todo por igual.

Y necesita hacerlo con cinco personas, para una red que en cinco meses más será tres veces más grande.

**Lo que el sistema debe garantizar:** observabilidad por sede, degradación controlada bajo carga, y
que incorporar hospitales no implique trabajo manual proporcional.

## Criterios de éxito

Katherine considera exitoso el sistema si:

- Una actualización llega a todas las sedes **sin intervención presencial** y sin ventana de corte.
- El monitoreo le avisa de una degradación antes de que la reporte la unidad.
- La recuperación ante una caída ocurre en **< 5 minutos**, y puede demostrarlo con evidencia.
- Incorporar un hospital nuevo es una operación de configuración, no un proyecto.
- El sistema sigue siendo usable de forma degradada cuando el enlace del hospital falla.
- Puede auditar quién accedió a qué dato clínico y cuándo, sin trabajo manual.
- Pasar de 1K a 100K sedes no requiere multiplicar su equipo.

## Restricciones

- Parque de PCs heterogéneo y antiguo, con navegadores que no siempre puede actualizar.
- Conectividad variable e intermitente entre sedes; algunas con enlaces de baja capacidad.
- La UCI es 24/7: **no existe ventana de mantenimiento** con corte de servicio.
- Equipo de cinco personas para toda la red, sin TI presencial por hospital.
- Debe cumplir la Ley N.° 29733 (datos sensibles de salud) y alinearse a RENHICE (Ley N.° 30024).
- Presupuesto público: los costos de infraestructura deben crecer sublinealmente respecto a las sedes.
- No puede exigir dispositivos institucionales para el personal clínico que usa su celular personal.
