import json

emp_Dict = {
    "name": "tinku",
    "age": 27,
    "phone": 9876543210,
    "salary": 55000
}

# converting dictionary to json using dumps() function
emp_Json = json.dumps(emp_Dict)
print("Using dumps() function emp_json: ", emp_Json)

# creating sample.json file
with open("sample.json", "w") as out_json_file:
    json.dump(emp_Dict, out_json_file)

# converting json to dictionary
# Opening JSON file
with open('sample.json') as json_file:
    emp_data = json.load(json_file)
    print(emp_data)