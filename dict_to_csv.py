# import csv module

import csv
# creating list of field names
field_names = ["No", "Company", "Car Model"]
# Creating a list of python dictionaries
cars = [
{'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
{'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
{'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
{'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
{'No': 5, 'Company': 'BMW', 'Car Model': 'BMW X7'},
]
# Writing content of dictionaries to CSV file
with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(cars)
filename = "Names.csv"

# opening the file using "with"
# statement
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        print(line)
