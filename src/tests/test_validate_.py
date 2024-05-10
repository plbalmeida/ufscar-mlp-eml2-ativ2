import pytest
from src.validate import validate_model
from unittest.mock import patch, MagicMock


def test_validate_model_high_accuracy(capsys):
    """Testa se o fluxo continua quando a acurácia é alta."""
    with patch('joblib.load') as mock_load:
        model = MagicMock()
        model.predict.return_value = [0] * 30
        mock_load.return_value = model

        with patch('src.validate.accuracy_score', return_value=0.95):
            validate_model()
            captured = capsys.readouterr()
            assert "Model accuracy: 0.95" in captured.out
            assert "continuing CI/CD pipeline." in captured.out


def test_validate_model_low_accuracy(capsys):
    """Testa se o fluxo para quando a acurácia é baixa."""
    with patch('joblib.load') as mock_load:
        model = MagicMock()
        model.predict.return_value = [0] * 30
        mock_load.return_value = model

        with patch('src.validate.accuracy_score', return_value=0.85):
            with pytest.raises(SystemExit) as e:
                validate_model()
            assert e.type == SystemExit
            assert e.value.code == 1
            captured = capsys.readouterr()
            assert "Model accuracy: 0.85" in captured.out
            assert "stopping the CI/CD pipeline." in captured.out


@pytest.mark.parametrize("accuracy", [0.9, 0.91, 0.89, 0.75, 0.99])
def test_validate_model_edge_cases(capsys, accuracy):
    """Testa casos limite de acurácia e verifica saídas correspondentes."""
    with patch('joblib.load') as mock_load:
        model = MagicMock()
        model.predict.return_value = [0] * 30
        mock_load.return_value = model

        with patch('src.validate.accuracy_score', return_value=accuracy):
            with pytest.raises(SystemExit) as sys_exit:
                validate_model()
            assert sys_exit.type == SystemExit
            if accuracy < 0.9:
                assert sys_exit.value.code == 1
                captured = capsys.readouterr()
                assert f"Model accuracy: {accuracy:.2f}" in captured.out
                assert "Model accuracy below 90%, stopping the CI/CD pipeline." in captured.out  # noqa e401
            else:
                captured = capsys.readouterr()
                assert f"Model accuracy: {accuracy:.2f}" in captured.out
                assert "continuing CI/CD pipeline." in captured.out
