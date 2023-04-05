# converting dictionary to json using dumps() function
import json

emp1_detail_dict = {
    "name": "sudeep",
    "age": 32,
    "salary": 10000,
    "phone": 3456789321
}

# emp1_detail_json = json.dumps(emp1_detail_dict)
# print("printing after convert json: ", emp1_detail_json)

# creating json file
with open("sample_emp.json", "w") as out_json_file:
    json.dump(emp1_detail_dict, out_json_file)
