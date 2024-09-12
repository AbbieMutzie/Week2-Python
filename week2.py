#Create an empty list
my_list = []

#Appending itesm to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting 15 at the second position of the list
my_list.insert(1,15)

#List extension
my_list.extend([50, 60, 70])

#Remove the last item from the list
my_list.pop()

#Sorting list in an ascending order
my_list.sort()

# Finding and printing the index of 30 in my_list
index_of_30 = my_list.index(30)
print("Sorted list is:", my_list)
print("The index of 30 is:",index_of_30 )
