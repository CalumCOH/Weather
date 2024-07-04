import requests
import pytest
import main

def test_get_endpoint():
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': 'Berlin',
        'appid': '569a7ed269a96cc6f08a1facf32affaf',  
        'units': 'metric'
    }

    #
    response = requests.get(url, params=params)

    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    json_data = response.json()


    assert 'main' in json_data, "'main' key not found in response"
    
    assert 'temp_min' in json_data['main'], "'temp_min' key not found in 'main'"
    assert isinstance(json_data['main']['temp_min'], (float, int)), "Minimum temperature is not a float or int"

    assert 'temp_max' in json_data['main'], "'temp_max' key not found in 'main'"
    assert isinstance(json_data['main']['temp_max'], (float, int)), "Maximum temperature is not a float or int"

    temp_min = json_data['main']['temp_min']
    temp_max = json_data['main']['temp_max']
    average_temp = (temp_min + temp_max) / 2

    print(f"Average temperature: {average_temp}")
    assert isinstance(average_temp, (float, int)), "Average temperature is not a float or int"


if __name__ == "__main__":
    pytest.main()


