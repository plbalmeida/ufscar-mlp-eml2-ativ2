import pytest
import json
from src.app import app as flask_app


@pytest.fixture
def client():
    """Configura um cliente de teste Flask."""
    flask_app.testing = True
    with flask_app.test_client() as client:
        yield client


def test_predict_endpoint(client):
    """Testa o endpoint de predição com dados corretos."""
    response = client.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert 'prediction' in json.loads(response.data)


def test_predict_endpoint_failure(client):
    """Testa o endpoint de predição com dados incorretos."""
    response = client.post('/predict', json={'wrong_key': 'value'})
    assert response.status_code == 400


def test_predict_endpoint_no_data(client):
    """Testa o endpoint de predição sem dados enviados."""
    response = client.post('/predict')
    assert response.status_code == 400
