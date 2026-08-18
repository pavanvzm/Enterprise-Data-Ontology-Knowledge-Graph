# Next-Session Repository Repair Checklist

## Audit scope

This checklist compares the live `main` branch of [pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph](https://github.com/pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph) with the complete local Ontolith React web project. The repository is currently readable and its latest commit is `d793d245069671789d850f410af7dde847a6145f`, with the message `feat: Complete project scaffold with ontology, knowledge graph, API, tests, and documentation`.

The central finding is that the live repository currently contains a **Python/FastAPI scaffold**, while the local project contains the **React 19 + TypeScript + Vite + Express + tRPC web application**. The two trees are not yet merged on GitHub.

## Priority 0 — repository write access

| Item | Current state | Next action |
| --- | --- | --- |
| GitHub push permission | Read access works, but pushes from the current environment return HTTP 403 | Use SSH or a refreshed secure GitHub credential that has write access to this exact repository |
| Target branch | `main` | Push the prepared merge to `main` after authentication is fixed |
| Local merged commit | `a494cb8` | Push this commit or recreate the merge in the next Codespace |

Do not create more tokens in chat. If using SSH, verify `ssh -T git@github.com`, set the remote to `git@github.com:pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph.git`, and confirm the authenticated GitHub account has repository write permission.

## Priority 1 — missing web application files

The following local web-project paths are absent from the live repository and should be added first:

| Missing path or group | Why it matters | Source to add |
| --- | --- | --- |
| `package.json` | Defines the React/Vite/Express/tRPC scripts and dependencies | Local project root |
| `pnpm-lock.yaml` | Reproducible Node dependency installation | Local project root |
| `client/` | React application, routes, components, pages, styling, and ontology workspace | Local project `client/` |
| `server/` | Express, tRPC, auth, database, storage, and runtime scaffolding | Local project `server/` |
| `drizzle/` | Database schema, migration metadata, and relations | Local project `drizzle/` |
| `shared/` | Shared types and constants | Local project `shared/` |
| `components.json` | shadcn/UI component configuration | Local project root |
| `drizzle.config.ts` | Drizzle migration configuration | Local project root |
| `tsconfig.json` | TypeScript compiler configuration | Local project root |
| `vite.config.ts` | Vite and Manus runtime configuration | Local project root |
| `vitest.config.ts` | Unit-test discovery and configuration | Local project root |
| `template.json` | Project template metadata | Local project root |
| `patches/` | Wouter patch required by the Node dependency tree | Local project `patches/` |

## Priority 2 — required product and test files

Verify that the following application-specific files are present after the merge:

| File | Purpose |
| --- | --- |
| `client/src/pages/Home.tsx` | Blueprint-style dashboard and all interactive workspaces |
| `client/src/lib/ontology.ts` | CSV/JSON/SQL parsing, ontology inference, drift detection, conflict merging, and graph traversal |
| `client/src/lib/ontology.test.ts` | Tests for ontology parsing, inference, conflicts, and traversal |
| `client/src/index.css` | Royal-blue blueprint grid, technical linework, responsive layout, and dropzone styling |
| `client/src/App.tsx` | Root route and dashboard wiring |
| `client/src/components/DashboardLayout.tsx` | Reusable internal dashboard shell |
| `server/routers.ts` | tRPC application router and auth procedures |
| `server/db.ts` | Database access helpers |
| `drizzle/schema.ts` | Auth and application schema definitions |
| `server/auth.logout.test.ts` | Existing server-side test coverage |

## Priority 3 — setup guide and documentation

The setup guide is missing from the live repository and must be added:

| Missing file | Required action |
| --- | --- |
| `SETUP_INSTALLATION_GUIDE.pdf` | Add the validated six-page installation guide to the repository root |
| `setup-guide-pdf/` | Add the Typst source and verification artifacts if source reproducibility is desired |
| `ONTOLITH_WEB_PROJECT.md` | Add the React web-project README without deleting the current Python scaffold README |
| `bootstrap-ontolith-web.sh` | Add the Codespaces bootstrap script that installs Node dependencies, runs checks/tests, and starts the app |
| `.typst-content-manifest.json` and `.typst-build-plan.json` | Optional build metadata for reproducing the guide PDF |

## Priority 4 — conflicting scaffold files

These files currently describe or build the Python scaffold rather than the React web application. Decide whether to preserve them as a separate backend scaffold or replace/extend them:

| Existing remote file | Problem | Recommended next-session action |
| --- | --- | --- |
| `bootstrap-codespace.sh` | Generates a Python project structure and does not install or start the React web project | Preserve it as `bootstrap-python-scaffold.sh` or replace it with the Node/React bootstrap script |
| `README.md` | Documents the Python/FastAPI project, not the React control plane | Keep as `PYTHON_API_README.md` and make the web-project README the primary README, or combine both clearly |
| `docs/getting-started.md` | Contains only Python and Uvicorn instructions | Add a web-project section with `pnpm install`, `pnpm check`, `pnpm test`, and `pnpm dev` |
| `docker/Dockerfile` | Builds only `python:3.11-slim` and starts Uvicorn | Add a separate Node web Dockerfile or document that this Dockerfile is for the Python API scaffold only |
| `docker/docker-compose.yml` | Exposes only FastAPI on port 8000 and Redis; it does not run the React/Vite app | Add a web service or explicitly separate the Python API compose stack from the React app |
| `.github/workflows/tests.yml` | Appears designed for Python tests | Add a Node job using pnpm, `pnpm check`, `pnpm test`, and optionally `pnpm build` |
| `requirements.txt` | Covers Python dependencies only | Preserve for the Python API; do not treat it as a replacement for `package.json` and `pnpm-lock.yaml` |
| `src/` and `tests/` | Python ontology/API scaffold, not the React web tree | Preserve as backend prototype or document it as a separate implementation layer |

## Priority 5 — expected runtime/build issues after merge

These issues are likely if the repository is opened in Codespaces before the web files are added:

1. `pnpm install` fails because the live repository has no `package.json` or `pnpm-lock.yaml`.
2. `pnpm dev`, `pnpm check`, `pnpm test`, and `pnpm build` are unavailable because the Node scripts are missing.
3. The Python bootstrap script creates a different directory structure and does not start the React dashboard.
4. The Python Dockerfile cannot build or serve the Vite/Express web application.
5. The current Python compose file does not expose the React frontend.
6. The existing Python CI workflow does not validate the TypeScript client or Node server.
7. `SETUP_INSTALLATION_GUIDE.pdf` cannot be found because it is not on the live `main` branch.
8. The full local web project and the Python scaffold use different application roots, dependency managers, test runners, and runtime commands; they must be documented as one intentionally merged repository or separated into explicit subprojects.

## One-by-one push sequence for the next session

Begin with the authentication fix and stop if it fails. Then execute the following sequence in a Codespace:

```bash
git clone git@github.com:pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph.git
cd Enterprise-Data-Ontology-Knowledge-Graph
ssh -T git@github.com
```

Copy the local web-project directories and files into this checkout without deleting the Python scaffold. Add the PDF, web README, and bootstrap script. Then run:

```bash
pnpm install
pnpm check
pnpm test
pnpm build
git status --short
git add client server drizzle shared package.json pnpm-lock.yaml \
  components.json drizzle.config.ts tsconfig.json vite.config.ts \
  vitest.config.ts template.json patches SETUP_INSTALLATION_GUIDE.pdf \
  setup-guide-pdf ONTOLITH_WEB_PROJECT.md bootstrap-ontolith-web.sh
git commit -m "Add Ontolith React web project and setup guide"
git push origin main
```

Verify the result with:

```bash
git ls-remote --heads origin main
gh repo view pavanvzm/Enterprise-Data-Ontology-Knowledge-Graph
```

## Definition of done

The merge is complete when the live `main` branch contains `package.json`, `pnpm-lock.yaml`, `client/`, `server/`, `drizzle/`, `shared/`, `SETUP_INSTALLATION_GUIDE.pdf`, the web-project documentation, and the Codespaces bootstrap script. The repository should also have a clear README strategy, a CI workflow that tests both Python and Node layers if both are retained, and a successful `pnpm check`, `pnpm test`, and `pnpm build` result.
