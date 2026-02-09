.PHONY: run docker

run:
	@echo "Running Dash + FastAPI..."
	python3 -m app.main

docker:
	@echo "Building and running Docker container..."
	docker build -t af-detect .
	docker run -p 8050:8050 af-detect
