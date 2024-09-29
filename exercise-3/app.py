from flask import Flask, request, jsonify
import logging
from datetime import datetime
from utils.db import PostgresClient
from utils.json import makeResponse
from gps.service import validations

app = Flask(__name__)


@app.post("/v1/gps")
def createGPS():
    app.logger.info("create GPS")
    data = request.get_json()
    isValidate, errorMessage = validations(data)

    if not isValidate:
        return makeResponse(False, errorMessage, {"error": errorMessage}), 400

    timestamp = datetime.utcfromtimestamp(int(data["timestamp"]))

    try:
        db_client = PostgresClient()
        if db_client.connection is None:
            return makeResponse(False, "error", {"error": "Unable to connect to the database"}), 400
        db_client.executeQuery(
            """INSERT INTO 
            records (device_id, longitude, latitude, altitude, speed, created_at) 
            VALUES (%s,%s,%s,%s,%s,%s)""",
            (
                data["device_id"],
                data["latitude"],
                data["longitude"],
                data["altitude"],
                data["speed"],
                timestamp,
            ),
        )
        db_client.close()
        return makeResponse(True, "success", data), 200
    except Exception as e:
        return makeResponse(False, "error", {"error": e}), 400


@app.get("/v1/getData")
def getGPS():
    app.logger.info("get all GPS")
    try:
        db_client = PostgresClient()
        if db_client.connection is None:
            return makeResponse(False, "error", {"error": "Unable to connect to the database"}), 400
        data = db_client.fetchQuery("""SELECT * FROM records""",)
        if data is None:
            return jsonify({"error": "Records could not be obtained"}), 500
        db_client.close()
        return makeResponse(True, "success", data), 200
    except Exception as e:
        return makeResponse(False, "error", {"error": e}), 400


if __name__ == "__main__":
    app.run(debug=True)
