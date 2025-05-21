
# main check (Enforced before commit)

format:
  ruff format --preview .

ruff-check:
  ruff check --fix --unsafe-fixes .

basedpyright-check:
    basedpyright .

check: format ruff-check basedpyright-check

test:
    pytest -v tests/

# Additional analysis checks (not Enforced)

compile-dep:
  uv pip compile pyproject.toml -o requirements.txt
