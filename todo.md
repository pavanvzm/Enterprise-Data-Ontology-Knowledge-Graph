# Project TODO

- [x] Build the royal-blue architectural blueprint visual system with precise grid, technical linework, white typography, and responsive dashboard layout
- [x] Implement multi-source ingestion interface for CSV upload plus pasted JSON and SQL schema snippets
- [x] Implement simulated ingestion parsing and automated entity extraction from source schemas
- [x] Implement ontology mapping for Customer, Order, Facility, and related entities and relationships
- [x] Implement interactive knowledge graph visualization with zoom, pan, node selection, and graph controls
- [x] Implement entity detail panel with properties, connected entities, source datasets, and field-level metadata
- [x] Implement schema drift comparison with added, removed, and changed field and relationship alerts
- [x] Implement multi-source conflict resolver with overlapping/conflicting definitions and unified schema view
- [x] Implement query workspace for simple graph traversal queries and result display
- [x] Implement ingestion history log with timestamps, source names, entity counts, and drift alerts per run
- [x] Implemented an in-memory preview data model for ingestion runs and schema snapshots
- [x] Add Vitest coverage for parsing, ontology mapping, drift detection, conflict resolution, and query traversal
- [x] Validate desktop and mobile rendering, interactions, and runtime logs
- [x] Save a final checkpoint after all items are complete

## Validation follow-ups

- [x] Implement real CSV file selection/upload and CSV schema parsing, wiring the dropzone/button to handlers
- [x] Extend ingestion parsing to infer multiple entities and relationships from JSON, SQL, and CSV inputs
- [x] Add working graph zoom and pan interactions and connect graph controls to those behaviors
- [x] Implement conflict detection and merged-schema computation from ingested source schemas
- [x] Replace keyword-based query stubs with traversal over the in-memory entity/relation graph
- [x] Add a distinct in-memory data model for ingested source snapshots and run history
- [x] Add Vitest cases for ontology mapping and conflict resolution behavior
- [x] Capture and review desktop and mobile UI evidence and document interaction/runtime validation

## GitHub export

- [x] Inspect local Git status, remotes, and GitHub authentication
- [x] Prepare or update README.md with project overview, features, setup, testing, and preview instructions
- [x] Commit all project source files and documentation for export
- [ ] Create or identify the target GitHub repository and push the commit (repository identified; push blocked by GitHub 403 write permission)
- [ ] Verify the remote repository URL and final pushed branch

- [ ] Push the merged local history to the user-confirmed repository https://github.com/pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph (still blocked by GitHub 403 write permission)

- [ ] Revoke the exposed GitHub token and refresh GitHub access through a secure connector before retrying the push (authentication refreshed, but push still returns 403 write denial)

- [ ] Verify updated GitHub write permission and retry the push to the confirmed repository (still returns 403 write denial)

- [ ] Revoke the newly exposed GitHub token and refresh the GitHub connector securely before another push attempt

- [ ] Revoke the latest exposed GitHub token and use only the secure connector for the next push retry

- [ ] Retry the secure push to pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph and verify the remote main branch (still blocked by GitHub 403 write denial)

- [x] Verify current GitHub connector enabled state and repository access

- [ ] Verify refreshed GitHub write access and push the prepared main branch (connector active, but push still returns 403 write denial)

- [x] Verify current Git remote authentication, configured remotes, and target repository access

## Manual export

- [ ] Create a clean archive containing source code, README, tests, configuration, schema, and project documentation
- [ ] Exclude node_modules, build output, local secrets, generated logs, and sandbox metadata
- [ ] Verify archive structure and deliver the downloadable file

- [x] Create a second unrestricted archive containing every file and directory in the project, including Git metadata, dependencies, generated files, logs, and configuration
- [x] Verify the unrestricted archive and deliver it for manual upload

## Setup guide PDF

- [x] Create a setup and installation guide source covering prerequisites, installation, configuration, development, testing, and manual upload
- [x] Generate and validate the setup and installation PDF
- [x] Add the PDF to the project directory and rebuild the unrestricted full-project archive
- [x] Deliver the updated archive and standalone PDF

## Final PDF GitHub push

- [x] Commit SETUP_INSTALLATION_GUIDE.pdf and related guide artifacts to the project history
- [ ] Make one final secure push attempt to the confirmed GitHub repository and verify the remote (final attempt still returned HTTP 403)

- [ ] Attempt final push of committed project with setup PDF to the shared GitHub repository and verify remote main (verified destination and commit; push still returns HTTP 403)

## GitHub PAT presentation script

- [x] Write a secure presentation script explaining fine-grained PAT creation and repository write permissions
- [x] Explain GitHub HTTP 403 diagnosis and connector/runtime credential issues
- [x] Provide safe manual command-line push instructions without exposing tokens
- [x] Validate and deliver the presentation script document

## Archive repair

- [ ] Test the existing full-project archive for corruption and identify the failure
- [ ] Rebuild and validate a replacement archive
- [ ] Deliver the verified replacement archive

- [ ] Verify the current commit and destination, then attempt one final push to the shared GitHub repository (verified commit and destination; push still returns HTTP 403)

## Codespaces bootstrap

- [x] Create a bootstrap script that extracts the complete project archive into Codespaces
- [x] Install dependencies, run type checks and tests, and start the development server from the script
- [x] Validate the script syntax and deliver it with usage instructions

- [x] Check the shared GitHub repository for latest branch, commit, and Ontolith setup-guide files

## Repository web-project merge

- [x] Inspect the current repository structure and local full web-project source tree
- [x] Add SETUP_INSTALLATION_GUIDE.pdf and the complete React web project files without deleting the existing Codespaces scaffold
- [ ] Commit and push the merged repository update (local commit created; GitHub push blocked by HTTP 403)
- [ ] Verify the required PDF, package manifest, client, server, and web project files on main (pending successful push)

## Next-session repository audit

- [x] Compare live GitHub repository files with the complete local web-project inventory
- [x] Identify missing files, mismatched structures, and likely build/deployment errors
- [x] Write and deliver a prioritized one-by-one repair checklist

## Manual upload archive

- [ ] Assemble the complete React web project, setup PDF, bootstrap script, documentation, configuration, tests, and repair checklist
- [ ] Exclude node_modules, build output, Git metadata, secrets, generated logs, and temporary review artifacts
- [ ] Validate the archive contents and deliver the manual-upload ZIP
