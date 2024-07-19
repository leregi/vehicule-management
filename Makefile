.PHONY: build run stop runMigrations  clean
# Build and run the containers
build:
	docker-compose up -d --build
	docker-compose exec web alembic upgrade head
# Run the containers only
run:
	docker-compose up -d 
	docker-compose exec web alembic upgrade head
# Stop the containers
stop:
	docker compose stop
# Run the migrations only
runMigrations:
	docker-compose exec web alembic upgrade head
# Clean up Docker containers
clean:
	docker-compose down -v --remove-orphans

