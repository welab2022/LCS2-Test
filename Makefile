.PHONY: up
up:
	@echo "Stopping docker images (if running...)"
	docker compose down
	@echo "Building (when required) and starting docker images..."
	docker compose up --build -d
	@echo "Docker images built and started!"

.PHONY: down
down:
	@echo "Stopping docker compose..."
	docker compose down
	@echo "Done!" 
	@echo

.PHONY: atest
atest:
	@echo "Running automation test..."
	@pytest
	@echo "Done"
	@echo