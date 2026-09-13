<!--
Sync Impact Report
Version change: template -> 1.0.0
Modified principles: none; initial ratification
Added sections: Core Principles; Scope and Assumptions; Quality Gates and Workflow; Governance
Removed sections: none
Follow-up TODOs: none
-->

# RemoteSchooly Constitution

## Core Principles

### I. Requirements Precede Architecture (NON-NEGOTIABLE)

Every component, data store, external dependency, and connection in the architecture MUST trace to
one or more requirements in `specs/001-remoteschooly/spec.md`. Requirements state observable
outcomes, never products or implementation mechanisms. If the design needs behavior that the spec
does not require, the spec is corrected and re-evaluated before the architecture is changed.

### II. Weekly Learning Works Without Continuous Internet (NON-NEGOTIABLE)

A weekly course package is usable only when its manifest, required files, and version are complete
and verified at the provincial site. Students and provincial teachers MUST be able to use an
already-synchronized package over the local school network while the Internet link is unavailable.
Connectivity loss MUST NOT turn a partial transfer into a published package or require restarting
an otherwise valid transfer from zero.

### III. Token Reduction Is Measured, Not Claimed (NON-NEGOTIABLE)

AI use by Lima teachers MUST pass through a single metered boundary. The system MUST demonstrate a
reduction of at least 40 percent in combined input and output tokens per approved material unit,
compared with a versioned baseline over the same representative tasks and quality rubric. Provider
price changes, fewer published materials, or a cheaper model alone MUST NOT count as token savings.
Human authoring and review MUST remain possible without AI.

### IV. Every Behavior Has an Owner

The four required actors are Government, Student, Lima Teacher, and Provincial Teacher. Every
functional requirement MUST name one of them or an explicit program rule as its owner. Permissions
are least-privilege: government governs the program and sees aggregates; Lima teachers author and
publish; provincial teachers synchronize and use packages; students consume assigned material and
record their own progress. No downstream document may silently widen those boundaries.

### V. Evaluation and Traceability Are Deliverables

The requirement EVAL MUST score at least 8.0 out of 10 before the architecture is accepted. Each
evaluation run is immutable and cites the exact spec revision it judged. The architecture MUST be
shown top-down in successive iterations, with a traceability matrix from every requirement to the
first iteration that makes it true. All four happy paths MUST be visible in the final diagram.

## Scope and Assumptions

- This repository delivers the analyzed requirements, EVAL evidence, and architecture design for
  the laboratory; it does not claim a production implementation.
- The lab explicitly does not require 100 percent availability or advanced high-availability
  mechanisms yet. The design MUST still preserve correctness of course-package delivery.
- Unknown domain choices use `[ASSUMPTION: ...]`; decisions that cannot safely be defaulted use
  `[CLARIFY: ...]`. Neither may be hidden as fact.
- Personal student content and raw teacher prompts MUST NOT appear in government aggregate views.
- A simple design is preferred until a requirement proves that another component is necessary.

## Quality Gates and Workflow

1. Transcribe and visually inspect the source statement, including its diagram.
2. Specify actor journeys, requirements, edge cases, assumptions, and measurable outcomes.
3. Validate the specification checklist and run the requirements EVAL to a score of at least 8.0.
4. Plan the solution, including data, contracts, and a runnable validation guide.
5. Draw the architecture top-down: system context, delivery split, then full component view.
6. Verify requirement-to-diagram coverage, all four happy paths, Markdown links, and diagrams.
7. Any requirement change invalidates its EVAL result and every downstream traceability claim until
   the affected checks are run again.

## Governance

This constitution prevails over every downstream artifact in the repository. Amendments require a
documented rationale, a semantic version change, an updated Sync Impact Report, and a review of all
affected specs, plans, evaluations, and diagrams. MAJOR removes or incompatibly redefines a
principle; MINOR adds or materially expands governance; PATCH clarifies without changing meaning.
Compliance is reviewed at each EVAL and before publication to `main`.

**Version**: 1.0.0 | **Ratified**: 2026-09-02 | **Last Amended**: 2026-09-02
