#AN EMPTY LIST CALLED MY_LIST
my_list =[]

#APPENDING 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#INSERTING 15 AT THE SECOND POSITION IN THE LIST
my_list.insert(1, 15)

#EXTENDING MY_LIST WITH OTHER_LIST
other_list = [50, 60, 70]
my_list.extend(other_list)

#REMOVING THE LAST ITEM FROM MY_LIST
del my_list[-1]

#SORTING LIST IN AN ASCENDING ORDER
my_list.sort()

#FINDING AND PRINTING THE VALUE OF 30
digit = my_list.index(30)
print(my_list[digit])