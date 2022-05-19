import json

courses = '{"name": "RahulShetty", "language": [ "Java", "Python"]}'

#Loads method parse json strings and it returns dictionary

dict_courses = json.loads(courses)

# print(type(dict_courses))
#
# print(dict_courses)
#
# list_language = dict_courses['language']
# print(type(list_language))
#
# print(list_language[0])

print(dict_courses['language'][0])


#**** Parse content present in Json file
with open('C:\\Users\\ivander_kumu\\Desktop\\courses.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['dashboard']['website'])
    print(type(data['dashboard']))




for dashboard in data['dashboard']:
    print(dashboard)

#Price of RPA

print(type(data['courses']))
for course in data['courses']:
    print(course)
    if course['title'] == 'RPA':
        print(course['price'])
        assert course['price'] == 45

#Open another json file

with open('C:\\Users\\ivander_kumu\\Desktop\\courses1.json') as fi:
    data2 = json.load(fi)
    assert data == data2 #This is to compare if two json files are the same








