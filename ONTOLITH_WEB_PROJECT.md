# Ontolith — Enterprise Ontology Control Plane

Ontolith is a precision-oriented enterprise data ontology and knowledge graph workspace for data architects and engineers. It provides a browser-based preview of multi-source ingestion, ontology inference, schema drift detection, conflict resolution, graph traversal, and ingestion observability.

The interface uses a royal-blue architectural blueprint visual system with a faint drafting grid, white technical linework, compact engineering labels, and high-contrast typography.

## Product capabilities

| Capability | Description |
| --- | --- |
| Multi-source ingestion | Paste JSON or SQL schema snippets, select CSV input, or load a local CSV/JSON/SQL file in the preview workspace. |
| Ontology inference | Infer entities and relationships from fields and foreign-key-style identifiers, then map them into a canonical entity model. |
| Knowledge graph | Inspect Customer, Order, Facility, Shipment, and Product entities in an interactive node-link graph. Select nodes to inspect fields, source datasets, and connected entities. |
| Schema drift detection | Compare versioned snapshots and surface added, removed, and changed fields or relationships with severity indicators. |
| Conflict resolver | Merge conflicting field definitions while preserving source provenance and confidence. |
| Query workspace | Run lightweight natural-language traversal queries against the in-memory entity/relation graph. |
| Ingestion history | Track source names, versions, timestamps, entity counts, and drift alerts for preview ingestion runs. |

## Technology

The project is scaffolded as a full-stack React and TypeScript application using Vite, Tailwind CSS, Express, tRPC, Drizzle, Vitest, and the Manus web runtime. The current preview implementation keeps ontology snapshots and ingestion history in memory so the workflows can be tested immediately in a browser. The architecture is ready for a durable database, PySpark ingestion workers, and Neo4j persistence as a next integration step.

## Getting started

Install dependencies and start the development server:

```bash
pnpm install
pnpm dev
```

The project uses the scaffolded environment variables for authentication, database access, analytics, storage, and built-in services. Do not commit local `.env` files or secrets.

## Validation

Run the TypeScript checker, Vitest suite, and production build:

```bash
pnpm check
pnpm test
pnpm build
```

The current test suite covers JSON and CSV parsing, drift detection, ontology inference, conflict merging, graph traversal, and the scaffolded authentication logout flow.

## Project structure

```text
client/src/pages/Home.tsx       Main control-plane dashboard and workflows
client/src/lib/ontology.ts      Parsing, inference, drift, conflict, and traversal logic
client/src/lib/ontology.test.ts Core ontology unit tests
client/src/index.css            Blueprint visual system and responsive layout
server/                         Express, tRPC, authentication, and database scaffolding
drizzle/                        Database schema and migration workspace
todo.md                         Project implementation checklist
```

## Next production integrations

A production deployment should add durable source snapshot and ingestion-run tables, a FastAPI or tRPC ingestion boundary, PySpark jobs for large-scale schema normalization, Neo4j for graph persistence and traversal, and a background drift monitor with approval workflows. These integrations should preserve the current canonical vocabulary: entities, fields, relations, source datasets, schema snapshots, drift items, and ingestion runs.

## License

This repository does not currently declare a license. Add the appropriate license file before publishing it as an open-source project.
