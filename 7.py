#tuples and sets
genders=("male","female","other")



#sets in python
s={102,30,50}#set is unorder
a2 =((1,3))#if we use set() it also create set
print(a2)

#union  s1 u s2
s1 = {1,2,3}
s2 = {3,4,5,}

print(s1 | s2) #union | PIPE
print(s1 & s2) # INTERSECTION
print(s1 - s2) #diffrenceS
s1.add(4)
s1.discard(10)
s1.pop()
s1.clear()
print(s1)