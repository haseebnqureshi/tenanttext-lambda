#!/bin/bash

# Create a temporary build directory
rm -rf layers/python
mkdir -p layers/python/python/lib/python3.11/site-packages

# Use Lambda-specific Docker image and ensure x86_64 build
docker run --rm --platform linux/amd64 -v $(pwd):/var/task public.ecr.aws/sam/build-python3.11:latest \
    pip install --upgrade -r requirements.txt -t /var/task/layers/python/python/lib/python3.11/site-packages

# More selective cleanup
cd layers/python
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name "*.dist-info" -exec rm -rf {} +
# Don't remove egg-info as it might contain necessary metadata 