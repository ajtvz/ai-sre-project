#!/bin/bash

set -e  # Exit on error

#  Build the Docker image
docker build -t ai-log-parser:latest .

#  Detect OS and set default log path
if [[ "$OSTYPE" == "linux"* ]]; then
    LOG_PATH="/var/log"
elif [[ "$OSTYPE" == "macOS"* ]]; then
    LOG_PATH="/var/log"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows with Git Bash / Docker Desktop
    LOG_PATH="/c/Windows/System32/winevt/Logs"
else
    # Fallback for unknown systems
    LOG_PATH="$(pwd)/logs"
fi

#  Allow override: ./run_docker.sh /path/to/logs
if [ -n "$1" ]; then
    LOG_PATH="$1"
fi

#  Run the container with mounted logs
docker run --rm \
  -v "$LOG_PATH":/logs \
  ai-log-parser:latest