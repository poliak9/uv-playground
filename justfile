set shell := ["bash", "-euo", "pipefail", "-c"]

packages := "apps/fp-studio apps/pta-consumer packages/pta-shared"

# list available recipes
default:
    @just --list

# run every check (tests + lints)
check: test lint typecheck deps

# run the full pytest suite across the workspace
test *args:
    uv run pytest {{args}}

# run one package's tests in an isolated venv (catches phantom deps)
test-isolated package:
    uv run --isolated --package {{package}} --with pytest pytest {{package}}

# run tests isolated for every package
test-isolated-all:
    for p in {{packages}}; do \
        name=$(basename "$p"); \
        echo "--- $name ---"; \
        uv run --isolated --package "$name" --with pytest pytest "$p"; \
    done

# ruff lint + format check
lint:
    uv run ruff check .
    uv run ruff format --check .

# ruff auto-fix + format
fix:
    uv run ruff check --fix .
    uv run ruff format .

# type-check every package with ty
typecheck:
    for p in {{packages}}; do \
        echo "--- $p ---"; \
        uv run ty check "$p"; \
    done

# deptry: one run per package, from inside the package dir so its pyproject is picked up
deps:
    for p in {{packages}}; do \
        echo "--- $p ---"; \
        (cd "$p" && uv run --isolated --with deptry deptry .); \
    done

# sync the workspace (install all members + dev group)
sync:
    uv sync --all-packages
