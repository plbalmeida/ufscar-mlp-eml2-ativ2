import sys
import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def validate_model():
    model = joblib.load('iris_model.pkl')
    data = load_iris()
    X = data['data']
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.2f}")
    if accuracy < 0.9:
        print("Model accuracy below 90%, stopping the CI/CD pipeline.")
        sys.exit(1)
    print("Model accuracy is satisfactory, continuing CI/CD pipeline.")


if __name__ == "__main__":
    validate_model()
