.PHONY: run docker

PORT ?= 8050
DEBUG ?= 1

run:
	@echo "Running Dash + FastAPI on port $(PORT)..."
	python3 -m app.main

#docker:
#	docker build -t af-detect .
#	docker run -p $(PORT):8050 af-detect
