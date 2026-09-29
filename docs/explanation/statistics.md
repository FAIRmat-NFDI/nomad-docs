# Statistics on NOMAD data

NOMAD stores rich, structured data: entries that contain quantities (energies, forces,
band gaps, …) produced by different methods. Statistics features report on this stored
data — for example "how many entries use DFT" or "how many force vectors does NOMAD
hold". Such numbers drive dashboards, data-overview pages, and outreach material.

The central design question is *granularity*: how fine-grained should the stored
statistics be? Finer statistics answer more questions but cost more to index and
maintain, and the cost only becomes visible at large data volumes. This page explains
the levels of granularity NOMAD distinguishes, which of them are supported, and why.
For practical guidance on querying these statistics, see
[How-to guides > ... > Build a stats dashboard](../howto/manage/program/stats_dashboard.md).

## Three levels of coarseness

Statistics on quantities can be collected at three levels, from coarse to fine. The
levels form a decision framework: pick the coarsest level that answers your question.

1. **Filters + entry counts.** Filter entries that contain a given quantity (or match
   any other search criterion) and count the matching entries. This is the existing,
   general-purpose mechanism behind the search interface and the query API.
    - *Provides*: fast, flexible counts over any indexed search quantity, combinable
      with arbitrary filters.
    - *Misses*: entries are bulky and rich in metadata — a single entry can hold many
      molecular-dynamics snapshots or multiple outputs. Entry counts therefore
      **under-represent the actual data volume**: one entry with a thousand force
      vectors counts the same as one entry with a single force vector.
1. **Counts of all individual occurrences.** Count every occurrence of a quantity
   across all entries — for example, the total number of stored force vectors or
   energy values — without recording their dimensions.
    - *Provides*: honest volume numbers that also capture multiple registrations of
      the same quantity within one entry — different systems, force types, or
      snapshots constituting separate calculations, or the subtasks of a workflow.
      The mechanism is cheap and generic: it requires no
      schema change. Global totals are the primary use case (dashboards, homepage
      numbers, workshop figures); per-entry detail remains available through
      aggregation queries (for example, "give me the total per entry").
    - *Misses*: the shape of the data. A count of force vectors does not tell you how
      many atoms or time steps they span.
1. **Shapes and dimensions.** Additionally record the dimensions of each stored
   quantity.
    - *Provides*: in principle, exact data-volume accounting — for example, the
      number of atoms stored, or any other statistics at atomic resolution.
    - *Misses*: nothing conceptually — but see the status below; this level is not
      available.

## What is supported

Levels 1 and 2 are the supported scope:

- **Level 1** (filters + entry counts) exists today and stays as-is, with the
  volume-under-representation limitation described above.
- **Level 2** (occurrence counts, no dimensions) is the implemented statistics
  mechanism. The concrete query interface for these counts is still being finalized
  **[TBC]**.

!!! warning "Attention"
    **Level 3 (shapes and dimensions) is deferred: under construction, and may not
    happen.** Recording dimensions carries a large-scale indexing risk that only
    becomes visible at high data volumes and is hard to test ahead of time, and it may
    be more machinery than the known use cases need. This page documents the deferral;
    it does not commit anyone to implementing it.

## Motivating use cases

These use cases motivated the chosen scope; they are illustrations, not requirements.

- **Data coverage for machine-learned potentials.** A rough estimate of training-data
  coverage, for example the number of atomic force vectors. Multiple forces per system
  are valuable here because ML models use them locally, which is exactly what
  occurrence counts capture and entry counts miss.
- **Data-overview and homepage numbers.** Headline figures such as "N structures,
  N forces, …" aimed at principal investigators — a different audience from the
  entry-based numbers typically shown in workshops and conferences.
- **Breakdown by method** (for example, DFT versus other methods). This is achievable
  with the existing filter and aggregation fields, since an entry typically has one
  method; no new mechanism is needed. Note that DFT+ variants have multiple
  definitions, so method-based groupings need care.

## Optional extension: dimension annotations

An open option exists to declare in a schema that a section should be registered with
specific dimensions. The current registration tracks presence; annotations would add
positive integer counts for the annotated dimensions — for example, a specific
dimension of a quantity's shape, or several of its slices. This is available as an
opt-in extension, with caveats:

- It is a schema tweak, and schema changes carry breakage risk.
- It should not be overused on huge databases, where the added indexing cost matters.

Whether and where annotations are used is a pending decision of the respective data
owners **[TBC]**.

## Out of scope

- **Flexible dataframes** — data with flexible variables whose axes are defined later —
  cannot be covered by registration at this level. They are explicitly out of scope
  for the statistics mechanisms described here.
- **Dedicated per-quantity counters** (for example, a special atom counter) are not
  provided. If a small number of specific, deeper use cases emerge, the pattern is to
  implement a *normalizer* that stores the specific values — this keeps the general
  statistics store sparse.

!!! note
    Statistics are not free. On large databases, fine-grained statistics add indexing
    and storage cost. Prefer the coarsest level that answers your question, and treat
    fine-grained extensions (such as annotations) as deliberate, case-by-case choices.
