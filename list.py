#Nested for loop, List
ticket_ids = [1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011, [1008, 1009, 1010, 1011]]

ticket_ids[len(ticket_ids)-1]
ticket_ids[len(ticket_ids)-1][-1]
print(ticket_ids)

#ticket_ids[len(ticket_ids)-1][len(ticket_ids[len(ticket_ids)-1])]
len(ticket_ids[len(ticket_ids)-1])
print(ticket_ids)

len(ticket_ids[len(ticket_ids)-1])-1
print(ticket_ids)

ticket_ids[len(ticket_ids)-1][len(ticket_ids[len(ticket_ids)-1])-1]
print(ticket_ids)

ticket_ids[len(ticket_ids)-1][int(len(ticket_ids[len(ticket_ids)-1])/2)]
print(ticket_ids)

ticket_ids = [1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011]
print(ticket_ids)

ticket_ids.pop()

print(ticket_ids)
ticket_ids.pop(5)

print(ticket_ids)

