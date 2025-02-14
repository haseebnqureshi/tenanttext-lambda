# Lambda Dependencies Checker

A serverless function that verifies the successful import of dependencies in an AWS Lambda environment.

## Endpoint

The function is deployed at:
https://[api-id].execute-api.us-east-1.amazonaws.com/hello

## Prerequisites

- Node.js and npm (for Serverless Framework)
- Docker
- AWS CLI configured with appropriate credentials
- Serverless Framework installed (`npm install -g serverless`)

## Project Structure

- handler.py              # Lambda function handler
- requirements.txt        # Python dependencies
- serverless.yml         # Serverless Framework configuration
- build_layer.sh         # Script to build Lambda layer
- Dockerfile             # For building dependencies

## Setup & Deployment

1. Install Serverless Framework (if not already installed):
   
   npm install -g serverless

2. Build the Lambda Layer:
   
   chmod +x build_layer.sh
   ./build_layer.sh

3. Deploy to AWS:
   
   serverless deploy

## Testing

After deployment, you can test the endpoint using curl:

curl https://[api-id].execute-api.us-east-1.amazonaws.com/hello

Expected response:

{
  "message": "Dependencies check completed",
  "available_modules": {
    "pinecone": "5.0.1",
    "pinecone_text": "Imported successfully",
    "langchain": "0.3.0",
    "langchain_openai": "Imported successfully"
  }
}

## Development

To update dependencies:
1. Modify requirements.txt
2. Rebuild the layer using ./build_layer.sh
3. Redeploy using serverless deploy

## Notes

- Region: us-east-1
- Runtime: Python 3.11
- Dependencies are packaged in a Lambda layer
- Default timeout: 29 seconds 