#!/bin/sh
set -e

if [ "$1" = 'api' ]; then
    python3 manage.py migrate --noinput
    exec uwsgi --ini uwsgi.ini
fi

exec "$@"
