# 🛡️ AI-Powered Log Parser: Containerized System Log Analyzer for SREs

## Overview

AI-Powered Log Parser is a lightweight, containerized tool that reads and parses system logs from your host machine — specifically /var/log/syslog on Ubuntu — and outputs structured JSON for analysis, monitoring, and anomaly detection. It’s built for Site Reliability Engineers (SREs) who need portable, automated visibility into system behavior, and want to explore infrastructure-as-code, cloud deployment, and AI-assisted observability.

🧠 What Makes This Tool AI-Powered

This project uses machine learning to detect anomalies in system logs. Instead of relying on hardcoded rules, it applies an Isolation Forest model to learn patterns from the data and flag unusual behavior. That means it can catch subtle issues that traditional monitoring might miss — like a service behaving oddly but not crashing.
This is a form of unsupervised learning, which is commonly used in SRE tools to surface silent failures, performance hiccups, or unexpected system behavior.


## 🔥 Why This Tool Matters for SREs

As an SRE, your job is to ensure reliability, detect issues early, and automate observability. This tool helps you:

- ✅ Monitor system activity in real time (cron jobs, service restarts, kernel events)
- ✅ Detect anomalies using machine learning (Isolation Forest)
- ✅ Parse logs into structured JSON for dashboards, alerts, or ML models
- ✅ Run anywhere — local, CI/CD, cloud — thanks to Docker
- ✅ Extend easily with categorization, keyword detection, or AI summarization
- ✅ Automate insights into host behavior without installing agents or heavyweight tools

## 🚀 Features

- Reads /var/log/syslog from your host machine
- Parses each line into structured JSON with line number and message
- Flags anomalies based on line length using Isolation Forest
- Outputs:
  - logs/parsed.json
  - logs/anomalies.json
- Runs inside a Docker container
- Mounts host logs via -v /var/log:/var/log
- Easy to extend with keyword detection, timestamps, or service classification
- Future support for:
  - AWS EC2 deployment via Terraform
  - S3 storage for anomaly reports
  - AI-powered log summaries
  - Slack/email alerting

## 🧱 Project Structure

.
├── docker/
│   └── Dockerfile
├── src/
│   └── log_parser.py
├── logs/
│   ├── parsed.json
│   └── anomalies.json
├── requirements.txt
└── README.md

## 🛠️ Setup

1. Clone the Repository

git clone https://github.com/ajtvz/ai-sre-project.git
cd ai-sre-project

2. Create a Virtual Environment (for portability)

python3 -m venv ai-sre-env
source ai-sre-env/bin/activate   # On Windows: ai-sre-env\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run Locally

python src/log_parser.py

## 🐳 Docker Usage

1. Build the Docker Image

docker build --no-cache -t log-parser -f docker/Dockerfile .

2. Run the Parser

docker run --rm -v /var/log:/var/log log-parser

3. View the Output

cat logs/anomalies.json

## 🧠 How It Works

Inside log_parser.py:

- Checks if /var/log/syslog exists
- Reads all lines
- Parses each line into a JSON object with line number and message
- Calculates line length and applies Isolation Forest
- Flags anomalies and saves to logs/anomalies.json

## 🌍 Portability

This tool runs anywhere Docker runs:

- ✅ Linux (Ubuntu, CentOS, etc.)
- ✅ Windows (with exported logs)
- ✅ macOS
- ✅ CI/CD pipelines
- ✅ Cloud VMs or containers

Just mount the appropriate log file and run the container.

## 🧪 Extending the Tool

Add Keyword Detection:
Flag lines containing words like error, fail, unauthorized, denied, etc.

Add Timestamp Analysis:
Detect bursts, silence, or time gaps between events.

Add Service Classification:
Group anomalies by systemd, kernel, cron, etc.

## 📦 Future Ideas

- Terraform module to deploy EC2 + S3
- Push anomaly reports to S3
- Slack alerts for anomalies
- AI summaries using transformers or OpenAI
- REST API wrapper for remote log ingestion
- Prometheus/Grafana integration

## 📬 About the Author

Built by Aaron — a U.S. Army soldier transitioning into tech with a focus on reliability engineering, automation, and human centered documentation. Passionate about making technical tools accessible, scalable, and production ready.
