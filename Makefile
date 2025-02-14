PYTHON_FILES := .

.PHONY: format ruff-check mypy-strict pyright-check check coverage security radon radon-mi vulture

# main check (Enforced before commit)

format:
	ruff format --preview --line-length 79 .

ruff-check:
	ruff check --fix --unsafe-fixes $(PYTHON_FILES)

mypy-strict:
	mypy $(PYTHON_FILES)

pyright-check:
	pyright $(PYTHON_FILES)

basedpyright-check:
	basedpyright $(PYTHON_FILES)

check: format ruff-check mypy-strict

# Additional analysis checks (not Enforced)
coverage:
	coverage run -m pytest
	coverage report -m
	coverage html

security:
	ruff check --extend-select S --fix

radon: # cyclomatic complexity
	radon cc -a -nc -s $(PYTHON_FILES)

radon-mi: # maintainability index
	radon mi -s $(PYTHON_FILES)

vulture: # unused code
	vulture $(PYTHON_FILES) --min-confidence 80 --sort-by-size

# Management
compile-dep:
	uv pip compile pyproject.toml -o requirements.txt
