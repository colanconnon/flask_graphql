import json
import os
import tempfile

import pytest

from graphql_app import create_app, db


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # create a temporary file to isolate the database for each test
    # create the app with common test config
    app = create_app()

    # create the database and load test data
    with app.app_context():
        db.create_all()

    yield app



@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()

def test_it_can_fetch_autors(client, app):
    query = """
    {
        authors{
            id
            books
            {
                id
            }
        }
    }
    """
    response = client.post('/graphql',            
                data=json.dumps({'query': query}),
                content_type='application/json'
            )
    assert response.status_code == 200
    assert json.loads(response.data)['data']['authors'] == []