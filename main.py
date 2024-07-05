from fastapi import FastAPI, Request
import uvicorn
import requests, json


app = FastAPI()
appid = "569a7ed269a96cc6f08a1facf32affaf"
appurl = "https://api.openweathermap.org/data/2.5/weather"



def get_weather_data(city_name):
    print('entered get_weather_data')
    param = {"q": city_name, "appid": appid, "units": "metric"}
    response = requests.get(appurl, param)
    print(response.status_code)
    if response.status_code == 200:
        data = dict(json.loads(response.text))
        temp=data["main"]["temp"]
        min=data["main"]["temp_min"]
        max = data["main"]["temp_max"]
        avg = round((float(min)+float(max))/2, 2)
        humidity = data["main"]["humidity"]
        return{
            'temperature':temp,
            'min temperature':min,
            'max temperature':max,
            'average temperature':avg,
            'humidity':humidity
               
               
               
               }
    elif response.status_code == 404:
        return("pick a valid city")

@app.get("/")
async def read_root():
    return{"message": "hello World"}

@app.get("/city")
async def read_root(city_name: str, request: Request):
    get_data = get_weather_data(city_name)
    print('name:')
    print(city_name)

    return get_data







    