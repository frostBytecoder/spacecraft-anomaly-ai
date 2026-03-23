import numpy as np

def risk_score(value):
    if value > 40:
        return "CRITICAL"
    elif value > 20:
        return "WARNING"
    else:
        return "NORMAL"

data = [10, 25, 50]

for d in data:
    print(d, "->", risk_score(d))
