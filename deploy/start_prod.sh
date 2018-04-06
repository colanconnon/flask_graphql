cd /src/
/usr/local/bin/gunicorn graphql_app.wsgi -w 8 -b :8000 --worker-class=meinheld.gmeinheld.MeinheldWorker --reload;