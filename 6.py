#list operstion: collection of iteams in orderd 
items=["Bru","sugar","milk","Bru"]
print(items[-1])
items.pop()
print(items)
items.append("mango")
print(items)
items.remove("sugar")
print(items)
items.insert(1,"mango")
print(items)
items[1] = "coffe powder"
print(items)
items.clear()
print(items)


#slicing= start:end:step
l=[10,20,300,400,4,10]
print(l[0::2])

print(len(items))
print(sorted(l))

sorted_items= sorted(l)
print(sorted_items)

print(sum(l))
print(l.index(300))
print(l.count(10))
print(l.reverse())

m = [20,5,60,3,2,1]
sortd=sorted(m)
print(sortd)
print(reversed(m))
m.sort()
print(m)

#matrix
j=[[1,2],[3,4],[3,5]] #nesting
print(j)

print(j[2][1])
