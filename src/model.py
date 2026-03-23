from sklearn.ensemble import IsolationForest
import pandas as pd

def train_model(data):
    model = IsolationForest(contamination=0.2)
    model.fit(data)
    return model

def predict(model, data):
    return model.predict(data)

if __name__ == "__main__":
    df = pd.read_csv("data/sample_data.csv")
    model = train_model(df)
    predictions = predict(model, df)

    print("Predictions:", predictions)
