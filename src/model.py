import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train_and_save_model():
    data = load_iris()
    X = data['data']
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    joblib.dump(model, 'iris_model.pkl')


if __name__ == "__main__":
    train_and_save_model()
