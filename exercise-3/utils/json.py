def makeResponse(success: bool, message: str, data):
    response = {"success": success, "message": message, "data": data}
    return response
