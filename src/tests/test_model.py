import numpy as np
import pytest
import joblib
from src.model import train_and_save_model, predict, validate


@pytest.fixture(scope="module")
def trained_model():
    """Treina o modelo e o salva para uso nos testes."""
    train_and_save_model()
    return joblib.load('iris_model.pkl')


def test_train_and_save_model():
    """Testa se o modelo é treinado e salvo corretamente."""
    train_and_save_model()
    loaded_model = joblib.load('iris_model.pkl')
    assert loaded_model is not None


def test_predict_valid(trained_model):
    """Testa a função de predição com dados válidos."""
    features = [5.9, 3.0, 5.1, 1.8]
    prediction = predict(features)
    assert isinstance(prediction, np.int64)


def test_predict_invalid(trained_model):
    """Testa a função de predição com dados inválidos para gerar exceções."""
    with pytest.raises(ValueError):
        predict([])


def test_validate_accuracy(trained_model, capsys):
    """Testa se a validação imprime a precisão esperada."""
    validate()
    captured = capsys.readouterr()
    assert "Model validation: PASS" in captured.out
