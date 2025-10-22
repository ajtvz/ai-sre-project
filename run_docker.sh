#!/bin/bash

echo "🔧 Building Docker image..."
docker build --no-cache -t log-parser -f docker/Dockerfile .

echo "🚀 Running log parser container..."
docker run --rm -v /var/log:/var/log log-parser