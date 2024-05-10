import joblib
import os
import pytest
from sklearn.datasets import load_iris
from src.model import train_and_save_model


@pytest.fixture(scope="module")
def iris_data():
    return load_iris(return_X_y=True)


@pytest.fixture(scope="module")
def trained_model():
    train_and_save_model()
    return joblib.load('iris_model.pkl')


def test_model_file_exists():
    """Testa se o arquivo do modelo é criado."""
    train_and_save_model()
    assert os.path.isfile('iris_model.pkl')


def test_model_not_none(trained_model):
    """Testa se o modelo carregado não é None."""
    assert trained_model is not None


def test_model_attributes(trained_model):
    """Verifica se os atributos principais do modelo estão presentes."""
    assert hasattr(trained_model, 'coef_')
    assert hasattr(trained_model, 'intercept_')


def test_model_reproducibility():
    """Verifica se o modelo é reprodutível."""
    train_and_save_model()
    model1 = joblib.load('iris_model.pkl')
    train_and_save_model()
    model2 = joblib.load('iris_model.pkl')
    assert model1.get_params() == model2.get_params()
    assert all(model1.coef_ == model2.coef_)
