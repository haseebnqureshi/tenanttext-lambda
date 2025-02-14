#!/bin/bash

# Create a temporary build directory
rm -rf layers/python
mkdir -p layers/python/python/lib/python3.11/site-packages

# Create a Docker container that matches AWS Lambda's environment
docker run --rm -v $(pwd):/var/task public.ecr.aws/sam/build-python3.11:latest \
    pip install -r requirements.txt -t /var/task/layers/python/python/lib/python3.11/site-packages

# Clean up unnecessary files to reduce size
cd layers/python
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name "*.dist-info" -exec rm -rf {} +
find . -type d -name "*.egg-info" -exec rm -rf {} + 