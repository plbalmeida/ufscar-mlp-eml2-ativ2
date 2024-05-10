import joblib
import numpy as np
import sys
from functools import lru_cache
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


@lru_cache(maxsize=1)
def get_model():
    return joblib.load('iris_model.pkl')


def train_and_save_model():
    data = load_iris()
    X = data['data']
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    joblib.dump(model, 'iris_model.pkl')


def predict(features):
    model = get_model()
    features = np.array(features).reshape(1, -1)
    return model.predict(features)[0]


def validate():
    model = get_model()
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


train_and_save_model()
