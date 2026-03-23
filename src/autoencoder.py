import torch
import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Linear(1, 8)
        self.decoder = nn.Linear(8, 1)

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
