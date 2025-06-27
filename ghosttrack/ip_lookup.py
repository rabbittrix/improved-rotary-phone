import requests
import json
import time

def get_ip_info(ip_address):
    """
    Fetches detailed information about an IP address using ipwho.is API.
    
    Parameters:
        ip_address (str): The IP address to look up
        
    Returns:
        dict: Dictionary containing IP details or error message
    """
    api_url = f"http://ipwho.is/{ip_address}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        ip_data = response.json()

        if not ip_data.get("success", True):
            return {"error": ip_data.get("message", "Unknown error from API")}

        # Extract relevant fields
        result = {
            "ip": ip_address,
            "type": ip_data.get("type"),
            "country": ip_data.get("country"),
            "country_code": ip_data.get("country_code"),
            "city": ip_data.get("city"),
            "continent": ip_data.get("continent"),
            "continent_code": ip_data.get("continent_code"),
            "region": ip_data.get("region"),
            "region_code": ip_data.get("region_code"),
            "latitude": ip_data.get("latitude"),
            "longitude": ip_data.get("longitude"),
            "maps_link": f"https://www.google.com/maps/@{ip_data.get('latitude')},{ip_data.get('longitude')},8z"  if ip_data.get("latitude") and ip_data.get("longitude") else None,
            "is_eu": ip_data.get("is_eu"),
            "postal": ip_data.get("postal"),
            "calling_code": ip_data.get("calling_code"),
            "capital": ip_data.get("capital"),
            "borders": ip_data.get("borders"),
            "country_flag": ip_data.get("flag", {}).get("emoji"),
            "asn": ip_data.get("connection", {}).get("asn"),
            "organization": ip_data.get("connection", {}).get("org"),
            "isp": ip_data.get("connection", {}).get("isp"),
            "domain": ip_data.get("connection", {}).get("domain"),
            "timezone_id": ip_data.get("timezone", {}).get("id"),
            "timezone_abbr": ip_data.get("timezone", {}).get("abbr"),
            "is_dst": ip_data.get("timezone", {}).get("is_dst"),
            "timezone_offset": ip_data.get("timezone", {}).get("offset"),
            "utc": ip_data.get("timezone", {}).get("utc"),
            "current_time": ip_data.get("timezone", {}).get("current_time")
        }

        time.sleep(1)  # Rate limit friendly
        return result

    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}