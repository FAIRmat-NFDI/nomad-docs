# NOMAD Actions

Actions are executable workflows that NOMAD runs asynchronously, decoupled from the
regular [processing](./processing.md) cycle. They are contributed by
[plugins](./plugin_system.md) and are typically triggered from an entry — for example
through a button in an [ELN](../howto/manage/gui/elns.md) — but they do not run inside
the processing step that triggers them. Instead, the run is placed on a queue and
executed by dedicated *action workers*, while processing continues without waiting for
the result.

This page explains why actions exist, what they are made of, and how they run. For
implementing one, see [how to create an action](../howto/plugins/types/actions.md).

## Why actions exist

[Parsers](../howto/plugins/types/parsers.md) and
[normalizers](../howto/plugins/types/normalizers.md) run synchronously as part of
entry processing on NOMAD's internal worker: every affected entry passes through them
each time it is processed. This keeps them simple and predictable, but it also imposes
constraints. They should finish quickly, use only the resources of the shared worker,
and not depend on anything outside the upload they are processing.

Some processing does not fit these constraints:

- **Long runtimes**: simulations, machine-learning inference, or analysis pipelines
  that take hours or days rather than seconds.
- **External services**: robust interaction with third-party APIs, which requires
  retries, rate limiting, and tolerance for outages.
- **Special resources**: hardware such as GPUs that the internal worker does not have.
- **Human input**: steps that must pause and wait for a user decision before
  continuing.

Actions decouple such work from entry processing. The processing cycle only *starts*
an action and immediately moves on; the actual work happens elsewhere, on workers
provisioned for it.

## Anatomy of an action

An action is distributed as a plugin [entry point](./plugin_system.md#plugin-entry-points)
and bundles three things:

- **Workflows** describe the sequence of steps and the flow of data between them.
  They orchestrate, but do not compute.
- **Activities** are the individual units of work that a workflow calls: run a
  computation, call an external API, read or write files.
- A **task queue** assignment that determines which worker pool executes the action.
  NOMAD provides `CPU` and `GPU` queues by default, and an Oasis can add specialized
  workers with their own dependencies and hardware.

<figure markdown style="width: 100%">
  ``` mermaid
  graph LR
    subgraph Entry processing
      eln(ELN entry) -- button click --> norm("normalize()")
    end
    norm -- start_action --> temporal[Temporal]
    subgraph Action workers
      cpu(CPU worker)
      gpu(GPU worker)
    end
    temporal -- CPU task queue --> cpu
    temporal -- GPU task queue --> gpu
    cpu & gpu -. write results .-> archive[(Entry archive)]
  ```
  <figcaption>An action triggered from an ELN entry: processing only enqueues the run;
  dedicated workers execute it and write results back.</figcaption>
</figure>

Under the hood, actions are built on
[Temporal](https://temporal.io/){:target="_blank" rel="noopener"}, the workflow engine
that is part of the NOMAD [architecture](./architecture.md#temporal). Temporal keeps
the state of every run durable: if a worker crashes mid-run, the workflow resumes
instead of being lost, failed activities are retried, and the current status is always
queryable.

!!! note

    The workflows executed by actions are Temporal workflows — descriptions of *code
    to run*. They are not the same as [NOMAD workflows](./workflows.md), which are
    data that describe the provenance of results. An action can, of course, produce
    NOMAD workflow entries as part of its output.

## How an action runs

Actions follow a fire-and-forget model. A trigger — typically a schema's
`normalize()` reacting to a button in an ELN entry — calls `start_action()`, which
enqueues a workflow run and returns a workflow ID within milliseconds. Nothing waits
for the action to finish. Instead:

- The status of the run (`RUNNING`, `COMPLETED`, `FAILED`, ...) can be requested at
  any time using the workflow ID.
- Results are written back into the triggering [entry](../reference/glossary.md#entry)'s
  [archive](../reference/glossary.md#archive) by the action itself, so they appear
  when the entry is next viewed or processed.
- Input files (*assets*) and output files (*artifacts*) are kept in dedicated storage
  locations, per action and per run.

Because Temporal workflows can pause indefinitely without occupying a worker, actions
also support human-in-the-loop steps: a run can wait for user input provided through
the GUI and resume when it arrives — even days later.

## Actions or normalizers?

Actions are more powerful than normalizers, but also more complex to define and
operate. The how-to guide's rule of thumb: for trivial data manipulation — populating
a quantity from another quantity, importing data from a raw file — use a normalizer or
parser; reach for an action when the work needs an external API, a long runtime, or
special resources.

|                   | Normalizer                        | Action                                    |
|-------------------|-----------------------------------|-------------------------------------------|
| Runs              | during entry processing           | independently, after being enqueued       |
| Blocks processing | yes                               | no                                        |
| Runtime budget    | seconds                           | up to days                                |
| Executed by       | internal worker                   | dedicated CPU/GPU action workers          |
| Failure handling  | processing failure                | Temporal retries and durable state        |
| Effort to define  | low                               | higher (workflows, activities, models)    |

## Learn more

- [How to create an action](../howto/plugins/types/actions.md) covers implementation:
  entry points, data models, storage, signals, and secrets.
- [Processing](./processing.md) explains the regular processing cycle that actions
  complement.
- [Architecture](./architecture.md) shows where Temporal and the workers sit in the
  overall system.
