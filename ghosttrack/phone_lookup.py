import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def lookup_phone(phone_number, default_region="ID"):
    """
    Parses and returns detailed information about a phone number.
    
    Parameters:
        phone_number (str): Phone number (e.g. '+628123456789')
        default_region (str): Default region code if number is local (default: 'ID')

    Returns:
        dict: Dictionary containing parsed phone number details
    """
    try:
        parsed_number = phonenumbers.parse(phone_number, default_region)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return {"error": str(e)}

    is_valid = phonenumbers.is_valid_number(parsed_number)
    is_possible = phonenumbers.is_possible_number(parsed_number)

    result = {
        "input_number": phone_number,
        "valid": is_valid,
        "possible": is_possible,
        "national_number": parsed_number.national_number,
        "country_code": parsed_number.country_code,
        "international_format": phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        ),
        "e164_format": phonenumbers.format_number(
            parsed_number, phonenumbers.PhoneNumberFormat.E164
        ),
        "mobile_format": phonenumbers.format_number_for_mobile_dialing(
            parsed_number, default_region, with_formatting=True
        ),
        "location": geocoder.description_for_number(parsed_number, "en"),
        "country_code_iso": phonenumbers.region_code_for_number(parsed_number),
        "timezone": ', '.join(timezone.time_zones_for_number(parsed_number)),
        "carrier": carrier.name_for_number(parsed_number, "en"),
    }

    # Number Type
    num_type = phonenumbers.number_type(parsed_number)
    type_desc = {
        0: "Fixed line",
        1: "Mobile",
        2: "Fixed or mobile",
        3: "Toll-free",
        4: "Premium rate",
        5: "Shared cost",
        6: "VoIP",
        7: "Personal number",
        8: "Pager",
        9: "Universal product code",
        10: "Voicemail",
        11: "Short code",
        12: "Application specific",
    }
    result["number_type_code"] = num_type
    result["number_type_description"] = type_desc.get(num_type, "Unknown")

    return result