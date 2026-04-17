import requests
import json
import pytest
import logging

logging.basicConfig(level=logging.INFO) 
from src.constants.api_constant import get_all_user_url, get_user_by_id_url, post_user_url, put_user_url, delete_user_url, headers
from src.helpers.payload_manager import create_user_payload, update_user_payload, generate_user_payload  
from src.utils.utils import get_request, post_request, put_request, delete_request

def test_get_all_users():
    response = get_request(get_all_user_url, headers=headers)
    assert response.status_code == 200
    logging.info(f"GET All Users Response: {response.json()}")


def test_get_user_by_id():
    response = get_request(get_user_by_id_url, headers=headers)
    assert response.status_code == 200
    logging.info(f"GET User by ID Response: {response.json()}")    

def test_create_user():
    payload = generate_user_payload()
    print(f"Generated Payload: {payload}")
    response = post_request(post_user_url, data=payload, headers=headers)
    assert response.status_code == 201
    logging.info(f"POST Create User Response: {response.json()}")   

def put_update_user():
    response = put_request(get_user_by_id_url, data=update_user_payload, headers=headers)
    assert response.status_code == 200
    logging.info(f"PUT Update User Response: {response.json()}")

def test_delete_user():
    response = delete_request(get_user_by_id_url, headers=headers)
    assert response.status_code == 200
    logging.info(f"DELETE User Response: {response.status_code}")     


 