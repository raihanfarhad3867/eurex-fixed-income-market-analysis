.PHONY: build test all
build:
	python scripts/build_project.py

test:
	pytest -q

all: build test
