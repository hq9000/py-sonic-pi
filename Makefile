.PHONY: test lint format check clean

test:
	python -m pytest

lint:
	python -m ruff check .

format:
	python -m ruff format .

check: lint format

clean:
	@echo Cleaning up...
	rm -rf build/ dist/ *.egg-info .pytest_cache __pycache__ */__pycache__ .ruff_cache
	@echo Done.