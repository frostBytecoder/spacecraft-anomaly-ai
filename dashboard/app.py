import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.title("🚀 Spacecraft Mission Control Dashboard")

df = pd.read_csv("data/sample_data.csv")

model = IsolationForest(contamination=0.2)
df["Anomaly"] = model.fit_predict(df)

fig = px.line(df, y="sensor", title="Telemetry Data")
st.plotly_chart(fig)

st.subheader("Anomaly Alerts")

for i, row in df.iterrows():
    if row["Anomaly"] == -1:
        st.error(f"🚨 Anomaly at {row['sensor']}")

risk = "CRITICAL 🚨" if -1 in df["Anomaly"].values else "NORMAL ✅"
st.metric("Risk Level", risk)
