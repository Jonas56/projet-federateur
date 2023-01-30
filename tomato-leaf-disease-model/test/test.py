import requests

url = 'http://localhost:5000/predict'

r = requests.post(url, files= {'file': open('healthy.jpg', 'rb')})

print(r.json())