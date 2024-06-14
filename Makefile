.PHONY: format

format:
	ruff format .

species-ingest:
	poetry run python -m ingest.species_ingest