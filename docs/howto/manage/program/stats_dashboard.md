# How to build a stats dashboard

This guide shows how to collect statistics on NOMAD data — entry counts, aggregations,
and occurrence counts — and combine them into a stats dashboard such as a data-overview
page or homepage counters. It is mostly geared towards NOMAD Oasis operators, and
anybody else interested in building a statistics dashboard. For the underlying model — the three levels of statistics
granularity and what is (not) supported — see
[Explanation > Statistics on NOMAD data](../../../explanation/statistics.md).

## What you will learn

- Which statistics NOMAD offers today and how to query them.
- How to choose the right granularity for a dashboard number.
- How the pieces combine into a data-overview or homepage dashboard.

## Recommended preparation

- [Explanation > Statistics on NOMAD data](../../../explanation/statistics.md)
- [How-to guides > ... > Use the API](./api.md)
- [How-to guides > ... > Authenticate programmatically](./auth.md) (only for statistics
  over non-published data)

## What exists today

Three building blocks are available:

1. **Filters + entry counts.** Any query against the search index returns the number
   of matching entries. This powers the counts in the GUI search interface and is
   available programmatically through the `entries/query` endpoint.
1. **Aggregation queries.** The same endpoint can aggregate over the matched entries,
   for example to group counts by a quantity's values.
1. **Published statistics.** NOMAD itself publishes aggregate numbers about its data
   in the GUI's information pages, built from these same mechanisms.

### Count entries with a filter

Query `entries/query` with a `page_size` of 0 to retrieve only the count. For example,
to count entries containing both Ti and O:

```sh
curl -X POST "{{ nomad_url() }}/v1/entries/query" \
-H 'Content-Type: application/json' \
-d '{
    "query": {
        "results.material.elements": {
            "all": ["Ti", "O"]
        }
    },
    "pagination": {
        "page_size": 0
    }
}'
```

The response's `pagination.total` is the entry count.

!!! note
    Entry counts under-represent actual data volume: one entry may contain many
    molecular-dynamics snapshots or multiple outputs, yet it counts once. Use them for
    "how many datasets/calculations", not for "how much data".

### Group counts with an aggregation

Add an `aggregations` object to break a count down by the values of a quantity, for
example by method:

```sh
curl -X POST "{{ nomad_url() }}/v1/entries/query" \
-H 'Content-Type: application/json' \
-d '{
    "pagination": {
        "page_size": 0
    },
    "aggregations": {
        "methods": {
            "terms": {
                "quantity": "results.method.simulation.program_name"
            }
        }
    }
}'
```

This returns one bucket per program name with its entry count. A breakdown such as
"DFT versus other methods" works the same way over the method quantities — an entry
typically has one method, so entry counts are adequate here. Note that DFT+ variants
have multiple definitions, so check which method quantities your grouping relies on.

## Choose the right granularity

Use the decision framework from
[Explanation > Statistics on NOMAD data](../../../explanation/statistics.md): pick the
coarsest level that answers your question.

- "How many entries have a band gap?" &rarr; filters + entry count.
- "How many entries per simulation code?" &rarr; terms aggregation.
- "How many force vectors does NOMAD hold?" &rarr; occurrence counts (below).
- "How many atoms do those forces span?" &rarr; needs shapes/dimensions, which are
  **deferred (under construction, may not happen)** — this question currently cannot
  be answered from stored statistics.

## Count individual occurrences

Occurrence counts record every registration of a quantity across all entries — for
example, the total number of stored force vectors — including multiple registrations
within a single entry (different systems, force types, or snapshots constituting
separate calculations, or several subtasks). They are the right source for global
dashboard totals such as "N structures, N forces".

The concrete API for querying occurrence counts is still being finalized **[TBC]**:
endpoint and field names are not yet documented here. Per-entry detail is available
through aggregation queries on the same data (for example, totals per entry) **[TBC]**.

## Combine into a dashboard

A data-overview page with homepage numbers combines the blocks above:

1. **Headline totals** from occurrence counts: "N structures, N forces, …". These are
   the honest volume numbers, aimed for example at principal investigators browsing a
   data-overview page.
1. **Per-category breakdowns** from terms aggregations: entries per method, per
   program, per upload.
1. **Focused counts** from filtered entry queries: entries matching the specific
   criteria your audience cares about, for example a rough data-coverage estimate for
   machine-learned potentials via the number of atomic force vectors.

Fetch the numbers server-side or client-side from the endpoints above and render them
in your page or app; no dedicated statistics service is required.

!!! warning "Attention"
    On large databases, fine-grained statistics add real indexing and query cost. Do
    not overuse fine-grained statistics: prefer coarse counts for frequently refreshed
    dashboards, and cache results where possible.
