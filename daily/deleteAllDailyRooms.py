import requests
import json

secretsF = open("./secrets.json", "r")
secrets = json.load(secretsF)
key = secrets["daily_api"]
url = "https://api.daily.co/v1/rooms"
headers = {"Content-Type": "application/json", "Authorization": "Bearer " + key}

r = requests.get(url, headers=headers)

rooms = r.json()["data"]
for r in rooms:
  name = r["name"]
  if name not in ["jtest", "private", "hello", "test-call"]:
    requests.delete("https://api.daily.co/v1/rooms/" + name, headers=headers)
    print(name)
print("Deleted all api rooms")