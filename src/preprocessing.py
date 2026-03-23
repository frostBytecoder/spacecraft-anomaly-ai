import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data():
    df = pd.read_csv("data/sample_data.csv")
    scaler = StandardScaler()
    df["sensor"] = scaler.fit_transform(df[["sensor"]])
    return df
