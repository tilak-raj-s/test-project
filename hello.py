import sys
import requests

print("----------------------")
print("hello world !")
print("hello india")
# print(sys.version)
# print(sys.executable)

def greet(person):
    whotogreet = "Hello {}".format(person)
    return(whotogreet)

# print(greet("Ram"))
# print(greet("Siva"))

print("----------------------")

r = requests.get('http://www.google.com')
print("Status Code : {}".format(r.status_code))
