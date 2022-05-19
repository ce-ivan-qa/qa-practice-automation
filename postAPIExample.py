import json
import configparser
from payLoad import *
from configparser import *
import requests
from utilities.configurations import *
from utilities.resources import *
url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
addBook_response = requests.post(url, json= addBookPayload("asdasdsa235cx"),headers = headers,)


print(addBook_response.json())
response_json = addBook_response.json()

print(type(response_json))

bookID = response_json['ID']




#Delete the book

url1 = getConfig()['API']['endpoint'] + ApiResources.deleteBook

deleteBook_response = requests.post(url1,
        json={
                "ID" : bookID
            },headers = headers,)

assert deleteBook_response.status_code == 200

#print(deleteBook_response.status_code)

res_json = deleteBook_response.json()
print(res_json["msg"]) == "book is successfully deleted"


#Authentication
url3 = "https://api.github.com/user"
github_response = requests.get(url3,verify=False,auth=('rahulshettyacademy', getPassword()))

print(github_response.status_code)


