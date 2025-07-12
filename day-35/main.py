import requests
#our connectiona nnd contact to the api_key{data identity} and Endpoints(the website(s))
owm_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = #"I insert the api key here"


#SETTING UP THE PARAMETERS. Look at the api docs on parameters and how to implement
LOC_LAT = None
LOC_LON = None
weather_params = {
    "lat": LOC_LAT
    "lon": LOC_LON
    "appid": api_key

}

response = requests.get(owm_Endpoint, params=weather_params)
print(response.status_code)