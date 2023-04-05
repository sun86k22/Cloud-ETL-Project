# Load CSV data into List and Dictionary using Python


# importing module
import csv

# csv file used id Names.csv
filename = "Names.csv"

# opening the file using "with"
# statement
# with open(filename, 'r') as data:
#     for line in csv.reader(data):
#         print(line)

# then data is read line by line
# using csv.reader the printed
# result will be in a list format
# which is easy to interpret


# open file in read mode
with open("Names.csv", 'r') as f:
    dict_reader = csv.DictReader(f)
    print("printing dict reader: ", dict_reader)

    list_of_dict = list(dict_reader)

    print(list_of_dict)
    for i in list_of_dict:
        print("each line is: ", i)
