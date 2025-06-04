
# main check (Enforced before commit)

format:
  ruff format --preview .

ruff-check:
  ruff check --fix --unsafe-fixes .

basedpyright-check:
    basedpyright .

pyrefly-check:
    pyrefly check .

check: format ruff-check basedpyright-check pyrefly-check

test:
    pytest -v tests/

# Additional analysis checks (not Enforced)

check-uv-lock:
    uv lock --check

compile-user-dep:
  uv pip compile pyproject.toml -o requirements.txt

compile-dev-dep:
    uv pip compile pyproject.toml --all-extras -o requirements-dev.txt

compile-dep: compile-user-dep compile-dev-dep check-uv-lock
