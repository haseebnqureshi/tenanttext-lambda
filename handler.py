import json
import logging
import traceback

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    try:
        # Import each dependency separately to identify which one might fail
        logger.info("Starting to import dependencies...")
        
        import boto3
        logger.info("boto3 imported successfully")
        
        import pinecone
        logger.info("pinecone imported successfully")
        
        import docx2txt
        logger.info("docx2txt imported successfully")
        
        from pypdf import PdfReader
        logger.info("pypdf imported successfully")
        
        from langchain_community.llms import OpenAI
        logger.info("langchain_community imported successfully")
        
        from langchain.chains import LLMChain
        logger.info("langchain imported successfully")

        # Create a list of available modules
        available_modules = {
            'langchain_community': 'Imported successfully',
            'boto3 version': boto3.__version__,
            'pinecone': pinecone.__version__,
            'pypdf': 'Imported successfully',
            'docx2txt': 'Imported successfully'
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Dependencies loaded successfully!',
                'available_modules': available_modules
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
        
    except Exception as e:
        # Log the full error with traceback
        logger.error(f"Error occurred: {str(e)}")
        logger.error(traceback.format_exc())
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e),
                'traceback': traceback.format_exc()
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        } 