#!/usr/bin/env bash

set -e
set -x

# run the containers in detach mode
docker compose stop

# docker compose drop