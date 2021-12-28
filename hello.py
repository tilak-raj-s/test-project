import requests

r = requests.get('http://www.google.com')
print("Status Code : {}".format(r.status_code))
print(r.ok)