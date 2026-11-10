---
type: Overview
title: Process Overview
description: Human entrypoint for the documentation-process area, explaining what this area covers and how its documents fit together.
tags:
  - docs
  - process
  - overview
  - mental-model
---

# Process Overview

This area explains how documentation is structured, discovered, maintained, and kept consistent in this repository.

It exists so both humans and agents can find the smallest useful set of docs, understand how those docs are supposed to be used, and keep the docs tree synchronized as repository truth changes.

Enter through [the root index](../index.md), then use [this area's index](index.md)
to select the relevant documents. `Read when` is the primary signal, supported
by descriptions and tags. The index is navigation; this README explains how
the parts fit together. [Status](_status.md) records current reality and
[decisions](_decisions.md) preserve rationale.

These documents are concepts in the `docs/` OKF v0.2 bundle. Their frontmatter
owns type, title, description, and tags; the index projects descriptions and
tags while independently maintaining reading conditions. The root index owns
the process area's routing metadata. See [Docs System](docs-system.md) for
metadata maintenance and [Docs Routing](docs-routing.md) for selection behavior.

Read the focused docs here when you need details about routing, the indexed docs system, transitional states, co-located docs, or the business dictionary workflow.

Read [conceptual-simplicity.md](conceptual-simplicity.md) when a task affects boundaries, decomposition,
terminology, or docs structure.

[Demand-Driven Context](../DICTIONARY.md#demand-driven-context) complements routing:
a real task may expose missing, incomplete, stale, or undecided knowledge even
after the relevant docs have been read. The [context policy](demand-driven-context.md)
explains how to assess those gaps, ask only when necessary, and incorporate
validated reusable answers into the existing documentation system without
creating a second knowledge base.
