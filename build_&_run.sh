#!/usr/bin/env bash

set -e
set -x

# run the containers in detach mode
docker compose up -d --build

# run the migrations
./migrations.sh