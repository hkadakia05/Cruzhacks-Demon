import requests

BASE = "http://127.0.0.1:5000/"

repsonse = requests.post(BASE + "helloworld")

print(repsonse.json())

#make sure data is json serializable