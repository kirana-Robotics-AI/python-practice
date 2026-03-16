#create a list of 5 items
my_list= [10,20,40,50]
print("origenal list:",my_list)

#add item at the end
my_list.append(60)
print("affter adding at end:",my_list)

#add item at 2nd position
my_list.insert(1,15)
print("after inserting at second position:",my_list)

#remove the third item from the list
my_list.pop(2)
print("after removing third item:",my_list)


number= [1,6,8,9]
#sort in decending order
number.sort(reverse=True)
print("sorted list in decending order:",number)

#reverse the sorted list
number.reverse()
print("reversed list:",number)
