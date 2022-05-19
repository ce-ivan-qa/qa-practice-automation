import json

import requests

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'ivan'}, )

# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
#
# print(type(dict_response))
#
# print(dict_response[0]['isbn'])
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])

print(response.status_code)
assert response.status_code == 200

print(response.headers)

assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

print(response.cookies)

# Retrieve the book detals with isbn = KRL

for actualBook in json_response:
    # print(type(book)):
    if actualBook['isbn'] == 'KRL':
        print(actualBook)
        break



expectBook = {
    "book_name": "Chendamelam the sound of Kerala",
    "isbn": "KRL",
    "aisle": "7"
}

assert actualBook == expectBook