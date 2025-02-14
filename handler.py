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
            import pinecone
            available_modules['pinecone'] = pinecone.__version__
            logger.info("pinecone imported successfully")
        except Exception as e:
            available_modules['pinecone'] = f"Failed to import: {str(e)}"
            
        try:
            import pinecone_text
            available_modules['pinecone_text'] = 'Imported successfully'
            logger.info("pinecone_text imported successfully")
        except Exception as e:
            available_modules['pinecone_text'] = f"Failed to import: {str(e)}"
            
        try:
            import langchain
            version = getattr(langchain, '__version__', 'Version not found')
            available_modules['langchain'] = version
            logger.info(f"langchain imported successfully with version {version}")
        except Exception as e:
            available_modules['langchain'] = f"Failed to import: {str(e)}"
            
        try:
            import langchain_openai
            available_modules['langchain_openai'] = 'Imported successfully'
            logger.info("langchain_openai imported successfully")
        except Exception as e:
            available_modules['langchain_openai'] = f"Failed to import: {str(e)}"

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