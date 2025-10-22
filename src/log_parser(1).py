import os
import sys
import json
import numpy as np
from sklearn.ensemble import IsolationForest

log_path = "/var/log/syslog"
print("✅ Starting log parser...")

if not os.path.exists(log_path):
    print(f"❌ Log file not found: {log_path}")
    sys.exit(1)

with open(log_path) as f:
    lines = f.readlines()

print(f"📄 Total lines read: {len(lines)}")

# Convert log lines to features (length of message)
features = np.array([[len(line.strip())] for line in lines])

# Train Isolation Forest
model = IsolationForest(contamination=0.01, random_state=42)
predictions = model.fit_predict(features)

parsed_logs = []
anomalies = []

for i, line in enumerate(lines):
    entry = {
        "line": i,
        "length": len(line.strip()),
        "message": line.strip()
    }
    parsed_logs.append(entry)
    if predictions[i] == -1:
        anomalies.append(entry)

# Ensure output directory exists
output_dir = "logs"
os.makedirs(output_dir, exist_ok=True)

# Save full logs
with open(os.path.join(output_dir, "parsed.json"), "w") as f:
    json.dump(parsed_logs, f, indent=2)

# Save anomalies
with open(os.path.join(output_dir, "anomalies.json"), "w") as f:
    json.dump(anomalies, f, indent=2)

print(f"✅ Parsing complete. Output saved to logs/parsed.json")
print(f"🚨 Anomalies detected: {len(anomalies)} saved to logs/anomalies.json")