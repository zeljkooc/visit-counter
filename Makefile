build:
	docker compose build

up:
	docker compose up -d

test:
	python -m pytest -v

down:
	docker compose down
