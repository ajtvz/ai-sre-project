# 🛡️ Log Parser: Containerized System Log Analyzer for SREs

## Overview

**Log Parser** is a lightweight, containerized tool that reads and parses system logs from your host machine — specifically `/var/log/syslog` on Ubuntu — and outputs structured JSON for analysis, monitoring, and anomaly detection. It’s built for Site Reliability Engineers (SREs) who need portable, automated visibility into system behavior.

---

## 🔥 Why This Tool Matters for SREs

As an SRE, your job is to ensure reliability, detect issues early, and automate observability. This tool helps you:

- ✅ **Monitor system activity** in real time (cron jobs, service restarts, kernel events)
- ✅ **Parse logs into structured JSON** for dashboards, alerts, or ML models
- ✅ **Run anywhere** — local, CI/CD, cloud — thanks to Docker
- ✅ **Extend easily** with categorization or ML
- ✅ **Automate insights** into host behavior without installing agents or heavyweight tools

---

## 🚀 Features

- Reads `/var/log/syslog` from your host machine
- Parses each line into structured JSON
- Outputs to `logs/parsed.json`
- Runs inside a Docker container
- Mounts host logs via `-v /var/log:/var/log`
- Easy to extend with categorization or ML

---

## 🧱 Project Structure

```
.
├── docker/
│   └── Dockerfile
├── src/
│   └── log_parser.py
├── logs/
│   └── parsed.json (output)
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup

### 1. Build the Docker Image

```bash
docker build --no-cache -t log-parser -f docker/Dockerfile .
```

### 2. Run the Parser

```bash
docker run --rm -v /var/log:/var/log log-parser
```

This mounts your host’s `/var/log` directory into the container so it can read `syslog`.

### 3. View the Output

```bash
cat logs/parsed.json
```

---

## 🧠 How It Works

Inside `log_parser.py`:

- Checks if `/var/log/syslog` exists
- Reads all lines
- Parses each line into a JSON object with line number and message
- Saves to `logs/parsed.json`

---

## 🌍 Portability

This tool runs anywhere Docker runs:

- ✅ Linux (Ubuntu, CentOS, etc.)
- ✅ Windows (with exported logs)
- ✅ macOS
- ✅ CI/CD pipelines
- ✅ Cloud VMs or containers

Just mount the appropriate log file and run the container.

---

## 🪟 Windows Support (Optional)

Windows logs are stored in `.evtx` format. To use this tool:

1. Export logs via PowerShell:

```powershell
Get-WinEvent -LogName System | Out-File C:\Logs\system.txt
```

2. Mount the logs:

```bash
docker run --rm -v C:/Logs:/logs log-parser /logs/system.txt
```

3. Update `log_parser.py` to read `/logs/system.txt`

---

## 🧪 Extending the Tool

### 🧠 Add Anomaly Detection

Use scikit-learn:

```python
from sklearn.ensemble import IsolationForest
```

Train on normal logs, flag outliers, and write suspicious entries to a separate file.

---

## 📦 Future Ideas

- CLI wrapper for log selection
- Integration with Prometheus/Grafana
- Slack alerts for anomalies
- REST API wrapper for remote log ingestion

---

## 🙌 Author

Built by Aaron a detail-oriented, growth-driven SRE with a passion for making technical tools accessible and reliable