import pytest
import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def get_request(endpoint, headers=None):
    logging.info(f"Sending GET request to {endpoint}")
    response = requests.get(endpoint, headers=headers)
    pretty_response = json.dumps(response.json(), indent=4)
    print(pretty_response)
    logging.info(f"Response: {response.status_code}")
    print(response.status_code)
    return response



def post_request(endpoint, data=None, headers=None):
    logging.info(f"Sending POST request to {endpoint} with data: {data}")
    response = requests.post(endpoint, json=data, headers=headers)
    logging.info(f"Response: {response.status_code}")
    print(response.status_code)
    return response

def put_request(endpoint, data=None, headers=None):
    logging.info(f"Sending PUT request to {endpoint} with data: {data}")
    response = requests.put(endpoint, json=data, headers=headers)
    logging.info(f"Response: {response.status_code}")
    print(response.status_code)
    return response

def delete_request(endpoint, headers=None):
    logging.info(f"Sending DELETE request to {endpoint}")
    response = requests.delete(endpoint, headers=headers)
    logging.info(f"Response: {response.status_code}")
    print(response.status_code)
    return response 
