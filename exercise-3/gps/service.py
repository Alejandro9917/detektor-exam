def validations(data):
    required_params = [
        "latitude",
        "longitude",
        "altitude",
        "speed",
        "timestamp",
        "device_id",
    ]

    if not data:
        return False, "No data provided"

    for param in required_params:
        if param not in data:
            return False, f"Missing parameter: {param}"

    if not (-90 <= data["latitude"] <= 90):
        return False, "Latitude must be between -90 and 90"
    if not (-180 <= data["longitude"] <= 180):
        return False, "Longitude must be between -180 and 180"

    return True, ""
