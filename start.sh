#!/bin/bash
set -e
echo "Starting IoT Home Automation Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9120 --workers 1
