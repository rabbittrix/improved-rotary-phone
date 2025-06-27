# ghosttrack_wrapper.py

from ghosttrack.ip_lookup import get_ip_info
from ghosttrack.phone_lookup import lookup_phone
from ghosttrack.username_lookup import lookup_username


def run_ip_lookup(ip_address):
    """
    Wrapper for IP lookup function.
    
    Args:
        ip_address (str): The IP address to look up
        
    Returns:
        dict: Structured information about the IP address
    """
    return get_ip_info(ip_address)


def run_phone_lookup(phone_number, default_region="ID"):
    """
    Wrapper for phone number lookup function.
    
    Args:
        phone_number (str): Phone number (e.g. '+628123456789')
        default_region (str): Default region code if number is local (default: 'ID')
        
    Returns:
        dict: Structured information about the phone number
    """
    return lookup_phone(phone_number, default_region)


def run_username_lookup(username):
    """
    Wrapper for username lookup function.
    
    Args:
        username (str): The username to search for
        
    Returns:
        dict: Dictionary with platform names and URLs where username was found
    """
    return lookup_username(username)