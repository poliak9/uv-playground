# syntax=docker/dockerfile:1.9
# Build from the repo root:
#   docker build -f apps/fp-studio/Dockerfile -t fp-studio .

FROM ghcr.io/astral-sh/uv:python3.14-trixie-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0 \
    UV_NO_DEFAULT_GROUPS=1

WORKDIR /app

# Manifest layer: just the files needed for dependency resolution.
# Stays cached across source-only changes. All workspace member
# pyprojects are required for --locked/--frozen to validate.
COPY pyproject.toml uv.lock ./
COPY packages/pta-shared/pyproject.toml packages/pta-shared/pyproject.toml
COPY apps/fp-studio/pyproject.toml apps/fp-studio/pyproject.toml
COPY apps/pta-consumer/pyproject.toml apps/pta-consumer/pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync \
        --frozen \
        --package fp-studio \
        --no-install-workspace \
        --no-editable

# Source layer: only the workspace members fp-studio actually depends on.
COPY packages/pta-shared/src packages/pta-shared/src
COPY apps/fp-studio/src apps/fp-studio/src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync \
        --locked \
        --package fp-studio \
        --no-editable


FROM python:3.14-slim-trixie AS runtime

WORKDIR /app

# Only the built venv is needed — --no-editable installs real wheels,
# so no project source is required at runtime.
COPY --from=builder /app/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

RUN useradd --system --create-home app
USER app

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fp_studio.app:app"]

