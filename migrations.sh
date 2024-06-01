#!/usr/bin/env bash

set -e
set -x

#create migrations folder and stuff
# docker-compose exec web alembic init -t async migrations

# run first migration
#docker-compose exec web 
#alembic revision --autogenerate -m "init"

# run migrations upword
#docker-compose exec web 
alembic upgrade head

# run migrations backword
#
