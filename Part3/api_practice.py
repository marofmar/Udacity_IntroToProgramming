import requests

r = requests.get("https://api.github.com/eventsblargh")
print(r)

try:
    req = requests.get("http://www.udacity.com") 
    print(req.status_code)
except ConnectionError:
    print("Could not connect to server.") 
