# AI Log Parser: Containerized System Log Analyzer for SREs

## 1. Overview

This is a lightweight, containerized tool that reads and parses system logs from your host machine—specifically `/var/log/syslog` on Ubuntu—and outputs structured JSON for analysis, monitoring, and anomaly detection. It’s designed for Site Reliability Engineers (SREs) who want automated visibility into system behavior, and are exploring infrastructure-as-code, cloud deployment, and AI-assisted observability.

## 2. Why I Chose to Make This My First Project

• I wanted to build something practical that reflects real SRE workflows  
• Logs are noisy, this tool helps surface meaningful patterns using AI  
• It gave me hands-on experience with Python, Docker, and shell scripting  
• It’s a foundation for learning Terraform, AWS, and cloud-native deployment  
• I wanted a portfolio project that’s recruiter-ready and technically sound  
• It reinforces automation, observability, and anomaly detection—core SRE skills

## 3. Tools Used and Planning to Be Used

Used:
• Python (log parsing and anomaly detection)  
• Docker (containerization)  
• Shell scripting (`run_docker.sh` for automation)  
• Isolation Forest (unsupervised ML for anomaly detection)

Planning to use:
• Terraform (for AWS EC2 + S3 deployment)  
• AWS (cloud hosting and storage)  
• GitHub Actions (CI/CD pipeline)  
• NLP (for log summarization and alerting)  
• Slack/email integration (for anomaly notifications)

## 4. Features Currently

• Reads logs from host  
• Parses each line into structured JSON with line number and message  
• Flags anomalies using Isolation Forest based on line length 
• Outputs:
  - `logs/parsed.json`
  - `logs/anomalies.json`  
• Runs inside Docker  
• Mounts host logs via `-v /var/log:/var/log`  
• Easy to extend with keyword detection, timestamps, or service classification

## 5. What This Tool Does

Inside `log_parser.py`:
• Checks if `/var/log/syslog` exists  
• Reads all lines  
• Parses each line into a JSON object  
• Calculates line length and applies Isolation Forest  
• Flags anomalies and saves to `logs/anomalies.json`

## 6. How to Make It Portable

This tool runs anywhere Docker runs:

• Linux (Ubuntu, CentOS, etc.)  
• Windows (with exported logs)  
• macOS  
• CI/CD pipelines  
• Cloud VMs or containers

To run it:

1. Clone the repo  
   git clone https://github.com/ajtvz/ai-sre-project.git  
   cd ai-sre-project

2. Build the Docker image  
   docker build --no-cache -t log-parser -f docker/Dockerfile .

3. Run the parser  
   docker run --rm -v /var/log:/var/log log-parser

4. View the output  
   cat logs/anomalies.json

Just mount the appropriate log file and run the container. No agents, no setup overhead—just plug and parse.