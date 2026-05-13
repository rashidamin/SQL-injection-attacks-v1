
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from knn_model import build_knn

def train():
    df = pd.read_csv("../data/processed/nsl_kdd_processed.csv")
    X = df.drop('label', axis=1)
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = build_knn()
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)

    print("KNN Accuracy:", accuracy_score(y_test, preds))

if __name__ == "__main__":
    train()
