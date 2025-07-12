import requests

#------------------------------API REQUESTS CODES----------------------
#-------------------------------1XX HOLD ON----------------------------
#-------------------------------2XX SUCCESS----------------------------
#-------------------------------3XX GO AWAY----------------------------
#-------------------------------4XX YOU SCREWED UP---------------------
#-------------------------------5XX SERVER MESSED UP-------------------

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()


longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(f"The position for this is {iss_position}\n With Longitude: {longitude}\n And with Latitude: {latitude} .")