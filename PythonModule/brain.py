# brain.py
import torch
import torch.nn as nn
import torch.nn.functional as F
import math, time

class BonnieMemoryBuffer:
    def __init__(self, max_len=32):
        self.max_len = max_len
        self.buffer = []

    def add_input(self, text):
        vec = self._encode_text(text)
        self.buffer.append(vec)
        if len(self.buffer) > self.max_len:
            self.buffer.pop(0)

    def _encode_text(self, text):
        return [ord(c) / 255.0 for c in text[:64]] + [0.0] * max(0, 64 - len(text))

    def get_tensor(self):
        return torch.tensor(self.buffer).unsqueeze(0)  # Shape: [1, T, 64]

class BonnieNet(nn.Module):
    def __init__(self, output_size):
        super().__init__()
        self.conv1 = nn.Conv1d(64, 128, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(128, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64, 32)
        self.fc2 = nn.Linear(32, output_size)

    def forward(self, x):
        x = x.permute(0, 2, 1)  # [B, 64, T]
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = torch.mean(x, dim=2)
        x = F.relu(self.fc1(x))
        return self.fc2(x)

class BonnieOracle:
    def __init__(self, options):
        self.options = options
        self.memory = BonnieMemoryBuffer()
        self.model = BonnieNet(len(options))
        self.softmax = nn.Softmax(dim=-1)

    def collect_entropy_vector(self, size=16):
        entropy = []
        for _ in range(size):
            t1 = time.perf_counter_ns()
            _ = sum(math.sin(i) for i in range(1, 100))
            t2 = time.perf_counter_ns()
            jitter = (t2 - t1) % 1000
            entropy.append(jitter / 1000.0)
        return entropy

    def ask(self, question):
        self.memory.add_input(question)
        input_tensor = self.memory.get_tensor().float()

        entropy_tensor = torch.tensor(self.collect_entropy_vector()).float().unsqueeze(0)
        input_tensor = torch.cat([input_tensor, entropy_tensor.unsqueeze(0)], dim=1)

        with torch.no_grad():
            logits = self.model(input_tensor)
            probs = self.softmax(logits).squeeze()
        idx = torch.argmax(probs).item()
        return self.options[idx]
