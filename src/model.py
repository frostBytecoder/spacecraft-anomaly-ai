import numpy as np
from sklearn.ensemble import IsolationForest

# Example telemetry data (sensor values)
data = np.array([10, 12, 11, 13, 50, 12, 11]).reshape(-1, 1)

# Train model
model = IsolationForest(contamination=0.2)
model.fit(data)

# Predict anomalies
predictions = model.predict(data)

print("Telemetry:", data.flatten())

print("Anomaly Detection Results:")
for i, val in enumerate(data):
    if predictions[i] == -1:
        print(val[0], "-> Anomaly 🚨")
    else:
        print(val[0], "-> Normal ✅")
