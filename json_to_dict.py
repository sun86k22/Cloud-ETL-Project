import json
with open('sample_emp.json') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))

print(data)