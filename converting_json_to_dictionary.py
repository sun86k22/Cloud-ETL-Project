people_dict = {
    "people1": [
        {
            "name": "Nikhil",
            "age": 33,
            "from": "Delhi"
        },
        {
            "name": "Akhil",
            "age": 35,
            "from": "Pune"
        }
    ],
    "people2": [
        {
            "name": "Vihas",
            "age": 29,
            "from": "Chennai"
        }
    ]
}
print(people_dict)
# importing the module
import json

# converting dictionary to json using dumps() function
people_Json = json.dumps(people_dict)
print("Using dumps() function emp_json: ", people_Json)
# creating sample.json file

with open("people_sample.json", "w") as out_json_file:
    json.dump(people_Json, out_json_file)

# Conversion of JSON data to dictionary

# Opening JSON file
with open('people_sample.json') as json_file:
    data = json.load(json_file)
    print(data)


# How to save a Python Dictionary to a CSV File?
# import csv

field_names = ['No', 'Company', 'Car Model']

cars = [
    {'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
    {'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
    {'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
    {'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
    {'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
]

with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)