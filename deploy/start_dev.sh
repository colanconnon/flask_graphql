cd /src/graphql_app
export FLASK_APP=wsgi.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0 --port=8000