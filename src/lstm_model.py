import torch
import torch.nn as nn
import numpy as np

# Sample telemetry data (time series)
data = np.array([[10], [12], [11], [13], [50], [12], [11]], dtype=np.float32)

# Convert to tensor
data = torch.tensor(data).unsqueeze(0)  # shape (1, sequence, features)

# LSTM Model
class LSTMModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=16, batch_first=True)
        self.fc = nn.Linear(16, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out

model = LSTMModel()

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training
for epoch in range(100):
    output = model(data)
    loss = criterion(output, data)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Detect anomaly (simple threshold)
error = torch.mean((output - data)**2).item()

print("Reconstruction Error:", error)

if error > 50:
    print("Anomaly Detected 🚨")
else:
    print("System Normal ✅")
