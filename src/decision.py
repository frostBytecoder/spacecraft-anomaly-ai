def decision_system(anomaly):
    if anomaly:
        return "ALERT: Switch to backup system"
    else:
        return "System operating normally"


# Example
if __name__ == "__main__":
    print(decision_system(True))
