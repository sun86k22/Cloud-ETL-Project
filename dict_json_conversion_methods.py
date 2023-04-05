# 1) Using dumps() function

import json

Fruit_Dict = {
  'name': 'Apple',
  'color': 'Red',
  'quantity': 10,
  'price': 60
}
Fruit_Json = json.dumps(Fruit_Dict)
print("Using dumps() function: ", Fruit_Json)

# 2) Converting nested dictionary to JSON

#  import json (Already we imported json library)
dictionary = {
 'fruit':{"Grapes": "10","color": "green"},
 'vegetable':{"chilli": "4","color": "red"},
}
result = json.dumps(dictionary, indent = 3)
print("Converting nested dictionary to JSON: ", result)

# 3) Convert dictionary to JSON quotes

# import json (Already we imported json library)


class fruits(dict):
    def __str__(self):
        return json.dumps(self)


collect = [['apple', 'grapes']]
result = fruits(collect)
print("Convert dictionary to JSON quotes: ", result)

# 4) Convert dictionary to JSON array
# import json (Already we imported json library)
dictionary = {'Apple': 3, 'Grapes': 1}
array = [ {'key' : i, 'value' : dictionary[i]} for i in dictionary]
print("Convert dictionary to JSON array: ", json.dumps(array))

# 5) Convert dictionary to JSON using sort_keys
# import json (Already we imported json library)
dictionary ={"Name": "jack", "Branch": "IT", "CGPA": "8.6"}
result = json.dumps(dictionary, indent = 3, sort_keys = True)
print("Convert dictionary to JSON using sort_keys: ", result)