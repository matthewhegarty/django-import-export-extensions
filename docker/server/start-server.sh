#!/usr/bin/env bash
set -e
echo "start-server.sh"
python3 test_project/manage.py migrate --pythonpath .

echo "starting local server..."
gunicorn --workers=3 \
    --threads=3 \
    --worker-class=gthread \
    --log-file=- \
    --bind 0.0.0.0:8000 \
    --limit-request-line 8000 \
    test_project.wsgi:application
