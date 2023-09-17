import requests
import json
import webbrowser

API = "AIzaSyBF9neN0flONQNlOrMnzzgnsQcmtSmmTlw"
ID = "1280c2d1a93454710"
search = "codezilla cours"
url = f"https://www.googleapis.com/customsearch/v1"
parms = {"q":search, "key":API, "cx":ID}
res = requests.get(url, params=parms)
result = res.json()
webbrowser.open(result['items'][0]["link"])
print(result['items'][0]["link"])