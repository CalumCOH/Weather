import pytest
from main import get_weather_data
import requests
from unittest.mock import patch

def test_get_weather_data():
    mock_response = (15,13,17,15,67)

    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "current" : {
                "temperature": mock_response[0],
                "min temperature":mock_response[1],
                "max temperature":mock_response[2],
                "average temperature":mock_response[3],
                "humidity":mock_response[4]
            }
        }

        mock_data = get_weather_data()

        assert mock_data == mock_response

def main():
    test_get_weather_data()

if __name__ == '__main__':
    main()