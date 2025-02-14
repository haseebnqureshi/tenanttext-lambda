import json
import logging
import traceback

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    # Initialize dependencies dictionary
    available_modules = {}
    
    try:
        # Import each dependency separately to identify which one might fail
        logger.info("Starting to import dependencies...")
        
        try:
            import boto3
            available_modules['boto3'] = boto3.__version__
            logger.info("boto3 imported successfully")
        except Exception as e:
            available_modules['boto3'] = f"Failed to import: {str(e)}"
            
        try:
            import docx2txt
            available_modules['docx2txt'] = 'Imported successfully'
            logger.info("docx2txt imported successfully")
        except Exception as e:
            available_modules['docx2txt'] = f"Failed to import: {str(e)}"
            
        try:
            from pypdf import PdfReader
            available_modules['pypdf'] = 'Imported successfully'
            logger.info("pypdf imported successfully")
        except Exception as e:
            available_modules['pypdf'] = f"Failed to import: {str(e)}"
            
        try:
            from langchain_community.llms import OpenAI
            available_modules['langchain_community'] = 'Imported successfully'
            logger.info("langchain_community imported successfully")
        except Exception as e:
            available_modules['langchain_community'] = f"Failed to import: {str(e)}"
        
        try:
            from langchain.chains import LLMChain
            available_modules['langchain'] = 'Imported successfully'
            logger.info("langchain imported successfully")
        except Exception as e:
            available_modules['langchain'] = f"Failed to import: {str(e)}"

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Dependencies check completed',
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
                'traceback': traceback.format_exc(),
                'available_modules': available_modules  # Include available modules even on error
            }),
            'headers': {
                'Content-Type': 'application/json'
            }
        } 