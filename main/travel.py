import json
import requests

access_token = "1150962428.7ca37f7.9c3a05714437440297c4b06885520f6f"

def getLocationId(lat, lng):
	url = "https://api.instagram.com/v1/locations/search?lat={lat}&lng={lng}&access_token={access_token}".format(lat=lat, 
																												 lng=lng,
																												 access_token=access_token)
	r = requests.get(url)
	return r.json()["data"]

def getRecentMedia(id):
	url = "https://api.instagram.com/v1/locations/{locationid}/media/recent?access_token={access_token}".format(locationid=id,
																												access_token=access_token)
	r = requests.get(url)
	return r.json()["data"]