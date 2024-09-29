import unittest
import json
from app import app
from utils.db import PostgresClient


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        self.db_client = PostgresClient(
            dbname="detektor",
            user="user",
            password="pass",
            host="database",
        )
        
        
    def tearDown(self):
        self.db_client.close()


    def testInsertData(self):
        """Prueba la inserción de datos correctamente."""
        response = self.client.post(
            "/v1/gps",
            data=json.dumps(
                {
                    "device_id": 1,
                    "latitude": 47.7749,
                    "longitude": -122.4194,
                    "altitude": 30.5,
                    "speed": 20,
                    "timestamp": 1727566206,
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)


    def testMisingFields(self):
        """Prueba la respuesta cuando faltan campos requeridos."""
        response = self.client.post(
            "/v1/gps",
            data=json.dumps(
                {
                    "latitude": 51.5074,
                    "longitude": 0.1278,
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)


    def testGetRecord(self):
        """Prueba la obtención de registros."""
        # Inserta un registro primero
        self.client.post(
            "/v1/gps",
            data=json.dumps(
                {
                    "device_id": 2,
                    "latitude": 47.7749,
                    "longitude": -122.4194,
                    "altitude": 30.5,
                    "speed": 20,
                    "timestamp": 1727566206,
                }
            ),
            content_type="application/json",
        )

        response = self.client.get('/v1/getData')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
