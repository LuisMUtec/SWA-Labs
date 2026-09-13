# Working agreement for agents

1. Read `.specify/memory/constitution.md` before changing project artifacts.
2. `specs/001-remoteschooly/spec.md` is the only source of behavioral truth. Do not create a second
   backlog or add behavior only in the plan or architecture.
3. A spec change invalidates the current EVAL fingerprint. Commit the spec, run a new immutable EVAL,
   then re-check plan and traceability.
4. Do not mark a package `Listo` without manifest-complete verification.
5. Do not claim the 40 % from price, model choice, provider cache or lower publishing volume.
6. Keep student content out of AI and government aggregates.
7. Regenerate diagram outputs with `scripts/render-diagrams.sh` after editing DOT sources.
8. Run `scripts/validate_repo.py` and `git diff --check` before committing.
9. Product implementation is deferred. Unchecked tasks in `tasks.md` are a plan, not completed work.
