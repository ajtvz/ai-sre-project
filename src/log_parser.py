import os
import sys
import json
import platform
from sklearn.ensemble import IsolationForest

#  Detects the operating system and returns the most likely system log path
def detect_log_path():
    system = platform.system()
    if system == "Linux":
        return "/var/log/syslog" if os.path.exists("/var/log/syslog") else "/var/log/messages"
    elif system == "Darwin":  # macOS
        return "/var/log/system.log"
    elif system == "Windows":
        return "C:\\Windows\\System32\\LogFiles\\SomeLog.log"  # Replace with actual path if needed
    return "logs/sample.log"  # Fallback for unknown systems

#  Loads optional config from config.json (e.g., contamination rate, output directory)
def load_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except:
        return {}

#  Core parser logic: takes raw log lines and returns parsed entries + anomalies
def parse_logs(lines, config=None):
    config = config or {}
    parsed = []
    lengths = []

    #  Parse each line into a structured JSON object
    for i, line in enumerate(lines):
        entry = {
            "line_number": i + 1,
            "message": line.strip()
        }
        entry["length"] = len(entry["message"])
        parsed.append(entry)
        lengths.append(entry["length"])

    #  Apply Isolation Forest to detect anomalies based on line length
    model = IsolationForest(contamination=config.get("contamination", 0.05))
    preds = model.fit_predict([[l] for l in lengths])
    anomalies = [parsed[i] for i, p in enumerate(preds) if p == -1]

    return parsed, anomalies

#  Reads a log file from disk and passes its lines to the parser
def parse_file(path, config=None):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    return parse_logs(lines, config)

#  CLI entry point: runs when you execute `python log_parser.py`
if __name__ == "__main__":
    config = load_config()  # Load config settings
    log_path = sys.argv[1] if len(sys.argv) > 1 else detect_log_path()  # Use CLI arg or auto-detect
    system = platform.system()  # Identify OS

    #  Show environment info for debugging and verification
    print(f"🖥️ Detected OS: {system}")
    print(f"📄 Using log file: {log_path}")

    #  Parse the log file and detect anomalies
    parsed, anomalies = parse_file(log_path, config)

    #  Ensure output directory exists
    output_dir = config.get("output_dir", "logs")
    os.makedirs(output_dir, exist_ok=True)

    #  Save parsed logs and anomalies to disk
    with open(f"{output_dir}/parsed.json", "w") as f:
        json.dump(parsed, f, indent=2)

    with open(f"{output_dir}/anomalies.json", "w") as f:
        json.dump(anomalies, f, indent=2)

    #  Show summary of results
    print(f"✅ Parsed {len(parsed)} lines from {log_path}")
    print(f"⚠️ Found {len(anomalies)} anomalies")