# Process Decisions

## Separate Routing From Explanation

`_index.md` exists to support routing and discoverability. `README.md` exists to help a human understand the area. Keeping those roles separate makes each file easier to maintain.

## Keep Status And Rationale Out Of `README.md`

`_status.md` and `_decisions.md` isolate information that changes for different reasons than the core mental model. This avoids turning `README.md` into a mixed-purpose document.

## Keep One Global Dictionary

The repository uses `docs/DICTIONARY.md` instead of per-folder glossaries so terminology stays centralized and easier to keep consistent.
