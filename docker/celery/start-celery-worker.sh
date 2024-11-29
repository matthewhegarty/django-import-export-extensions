#!/bin/bash

# Starts a celery worker process

set -o errexit

echo "starting local celery worker..."
celery --workdir /home/app/server/ --app=test_project.celery_app.app worker --loglevel=INFO
