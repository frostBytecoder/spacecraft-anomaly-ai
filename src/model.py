import numpy as np

def detect_anomaly(data):
    mean = np.mean(data)
    std = np.std(data)
    
    threshold = mean + 2*std
    
    anomalies = []
    
    for value in data:
        if value > threshold:
            anomalies.append(value)
    
    return anomalies


# Example telemetry data
telemetry = [10, 12, 11, 13, 50, 12, 11]

anomalies = detect_anomaly(telemetry)

print("Anomalies detected:", anomalies)
