import os
import sys
import json

# Set default log path
log_path = "/var/log/syslog"

# Print startup message
print("✅ Starting log parser...")

# Check if log file exists
if not os.path.exists(log_path):
    print(f"❌ Log file not found: {log_path}")
    sys.exit(1)

# Read log file
with open(log_path) as f:
    lines = f.readlines()

print(f"📄 Total lines read: {len(lines)}")

# Parse lines into structured format
parsed_logs = [{"line": i, "message": line.strip()} for i, line in enumerate(lines)]

# Ensure output directory exists
output_dir = "logs"
os.makedirs(output_dir, exist_ok=True)

# Write to JSON file
output_path = os.path.join(output_dir, "parsed.json")
with open(output_path, "w") as f:
    json.dump(parsed_logs, f, indent=2)

print(f"✅ Parsing complete. Output saved to {output_path}")