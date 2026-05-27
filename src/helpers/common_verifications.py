import requests
import json
import logging

# Configure logger for verification messages
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Function to verify the HTTP status code of a response
# response - the requests.Response object
# expected_code - the expected status code (e.g., 200, 201)
def verify_status_code(response, expected_code):
    actual_code = response.status_code
    if actual_code == expected_code:
        logger.info(f"Status code verification passed: {actual_code}")
        return True
    else:
        logger.error(f"Status code verification failed: expected {expected_code}, got {actual_code}")
        return False


# Function to verify if a specific header is present in the response
# response - the requests.Response object
# header_name - the name of the header to check (e.g., 'Content-Type')
# expected_value - optional expected value for the header
def verify_header(response, header_name, expected_value=None):
    headers = response.headers
    if header_name in headers:
        actual_value = headers[header_name]
        if expected_value is None:
            logger.info(f"Header '{header_name}' is present: {actual_value}")
            return True
        elif actual_value == expected_value:
            logger.info(f"Header '{header_name}' verification passed: {actual_value}")
            return True
        else:
            logger.error(f"Header '{header_name}' verification failed: expected '{expected_value}', got '{actual_value}'")
            return False
    else:
        logger.error(f"Header '{header_name}' is not present in the response")
        return False


# Function to verify if a key exists in the JSON response body
# response - the requests.Response object
# key - the key to check in the JSON (e.g., 'id', 'name')
# expected_value - optional expected value for the key
def verify_json_key(response, key, expected_value=None):
    try:
        json_data = response.json()
        if key in json_data:
            actual_value = json_data[key]
            if expected_value is None:
                logger.info(f"JSON key '{key}' is present: {actual_value}")
                return True
            elif actual_value == expected_value:
                logger.info(f"JSON key '{key}' verification passed: {actual_value}")
                return True
            else:
                logger.error(f"JSON key '{key}' verification failed: expected '{expected_value}', got '{actual_value}'")
                return False
        else:
            logger.error(f"JSON key '{key}' is not present in the response")
            return False
    except json.JSONDecodeError:
        logger.error("Response is not valid JSON")
        return False


# Function to verify the structure of the JSON response (e.g., check if it's a list or dict)
# response - the requests.Response object
# expected_type - 'list' or 'dict'
def verify_json_structure(response, expected_type):
    try:
        json_data = response.json()
        if expected_type == 'list' and isinstance(json_data, list):
            logger.info("JSON structure verification passed: response is a list")
            return True
        elif expected_type == 'dict' and isinstance(json_data, dict):
            logger.info("JSON structure verification passed: response is a dict")
            return True
        else:
            logger.error(f"JSON structure verification failed: expected {expected_type}, got {type(json_data).__name__}")
            return False
    except json.JSONDecodeError:
        logger.error("Response is not valid JSON")
        return False