# Calculus 1 — Complete Course

A self-study Calculus 1 course delivered as static HTML: an index page plus ten module pages,
each pairing a ~1000-word tutorial with 20 practice problems and tap-to-reveal solutions. Math is
rendered client-side with KaTeX; there is no build step for the content itself.

## Layout

| Path | Purpose |
| --- | --- |
| `src/calc1_00_index.html` | Landing page and navigation hub, links to all ten modules. |
| `src/calc1_01_*.html` … `src/calc1_10_*.html` | The ten course modules, in study order. |
| `Dockerfile` | Serves `src/` with busybox httpd; `/` defaults to the course index. |
| `deploy/docker-compose.yaml` | Runs the image locally on port 8080. |
| `.github/workflows/docker-publish.yml` | CI: version-tags each push and publishes to Docker Hub. |
| `docs/graph-night-design-system/` | Design-system reference used by the pages. |

## Viewing locally

Open the index directly in a browser — no server required:

```bash
xdg-open src/calc1_00_index.html
```

A network connection is needed at view time (fonts and KaTeX load from CDNs). To serve the pages
over HTTP instead:

```bash
python3 -m http.server -d src        # then open http://localhost:8000/calc1_00_index.html
```

## Running with Docker

```bash
docker compose -f deploy/docker-compose.yaml up -d   # then open http://localhost:8080/
docker compose -f deploy/docker-compose.yaml down
```

The image is built from the root `Dockerfile` (busybox httpd, ~3 MB), copies `src/*.html` into
the web root, and symlinks the index so `http://localhost:8080/` loads the course.

## Continuous deployment

On every push to `develop`, the `docker-publish.yml` workflow:

1. Increments the patch version from the latest `vX.Y.Z` git tag (starting at `v0.0.1`).
2. Creates and pushes that git tag.
3. Builds the Docker image and pushes it to Docker Hub as both
   `latest` and the new version tag.

### Required Docker Hub secrets

The workflow authenticates to Docker Hub using two **repository secrets**. Add them under
**Settings → Secrets and variables → Actions → New repository secret**:

| Secret | Value |
| --- | --- |
| `DOCKERHUB_USERNAME` | Your Docker Hub username. The image is published as `<username>/calculus`. |
| `DOCKERHUB_TOKEN` | A Docker Hub **access token** (Account Settings → Personal access tokens) with read/write scope — not your account password. |

Without both secrets, the login and build-and-push steps fail. The workflow also needs
`contents: write` permission to push the version tag; this is already declared in the workflow
file, so no extra configuration is required.
