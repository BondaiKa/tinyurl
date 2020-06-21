import os

import pytest
from app import app

@pytest.fixture
def client():
    # db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            app.init_db()
        yield client

    # os.close(db_fd)
    # os.unlink(app.app.config['DATABASE'])

def test_login(client):
    response =  client.post('/', data=dict(
        full_link='https://yandex.ru/'
    ), follow_redirects=True)
    print(response.data)
    print(response.status_code)
    assert 1 == 2
