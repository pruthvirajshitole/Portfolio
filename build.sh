#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput

# Only run migrations if database exists (for production)
if [ "$RENDER" = "true" ]; then
    echo "Running on Render, skipping migrations for now"
else
    python manage.py migrate
fi
