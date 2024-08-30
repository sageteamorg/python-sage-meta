import requests
import logging

logger = logging.getLogger(__name__)

def get_request(url: str, params: dict) -> dict:
    """
    Perform a GET request and return the response JSON.
    
    Args:
        url (str): The URL for the GET request.
        params (dict): The parameters for the GET request.
    
    Returns:
        dict: The response JSON or an empty dictionary if an error occurs.
    """
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error("Error occurred: %s", e)
        return {}

def post_request(url: str, data: dict) -> dict:
    """
    Perform a POST request and return the response JSON.
    
    Args:
        url (str): The URL for the POST request.
        data (dict): The data for the POST request.
    
    Returns:
        dict: The response JSON or an empty dictionary if an error occurs.
    """
    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error("Error occurred: %s", e)
        return {"error": str(e)}

def delete_request(url: str, params: dict) -> dict:
    """
    Perform a DELETE request and return the response JSON.
    
    Args:
        url (str): The URL for the DELETE request.
        params (dict): The parameters for the DELETE request.
    
    Returns:
        dict: The response JSON or an empty dictionary if an error occurs.
    """
    try:
        response = requests.delete(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error("Error occurred: %s", e)
        return {"error": str(e)}
