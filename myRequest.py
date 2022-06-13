import requests

response=requests.get("http://localhost/todo")

print(response.text)