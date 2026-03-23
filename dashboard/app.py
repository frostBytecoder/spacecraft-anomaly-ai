import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

st.title("🚀 Spacecraft Health Monitoring Dashboard")

# Sample telemetry data
data = np.array([10, 12, 11, 13, 50, 12, 11])

df = pd.DataFrame(data, columns=["Sensor Value"])

# Train anomaly model
model = IsolationForest(contamination=0.2)
model.fit(df)

df["Anomaly"] = model.predict(df)

# Plot graph
fig = px.line(df, y="Sensor Value", title="Telemetry Data")
st.plotly_chart(fig)

# Show anomalies
st.subheader("Anomaly Detection")
for i, row in df.iterrows():
    if row["Anomaly"] == -1:
        st.write(f"🚨 Anomaly detected at value {row['Sensor Value']}")

# Risk level
if -1 in df["Anomaly"].values:
    risk = "WARNING ⚠️"
else:
    risk = "NORMAL ✅"

st.metric("Current Risk Level", risk)
