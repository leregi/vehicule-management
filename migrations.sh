#!/usr/bin/env bash

set -e
set -x


######################################
 #
 #      Always execute
 #
 ######################################


# will execute the migration forward
docker-compose exec web alembic upgrade head




 #####################################
 #
 #      Don't uncomment
 #      (Only here to show you the command to run)
 #
 ######################################

# How to create the baseline migrations folder. We chose to name it migrations
# docker-compose exec web alembic init -t async migrations


# to make alembic auto generate a new migration
#docker compose exec web alembic revision --autogenerate -m "init_the_db"






