#FOR LOOP
i = 1
for i in range(1, 11):
    print(i , end=" ")
print("")


bag=("red","green","yellow")


# STEP in FOR LOOP
for ball in bag:
    print(ball)
 
for i in range(1, 11 , 2):
    print(i , end=" ")
print("")


#using enumerate

name = "kirana"

for index, letter in enumerate(name):
    print(letter*(index+1))

l= [12,13,56,33,44]

for index, num in enumerate(l):
    print(f"{num}is in {index}th index")


#using break in a for loop 

cities= ["bengalore","mysore","udupi","hubbali"]
for city in cities:
    if city == "shivamogga":
        print(f"found {city}!")
        break
else:
    print("not found")
print("")

for city in cities:
    if city == "shivamogga":
        continue
    print(city)

#FOOR LOOP ON DICTIONARY

d = {
    "NAME":"KIRANA",
    "AGE":23,
    "INCOME":1
}

for key,value in d.items():
    print(key, " ",value)

#5 table using for loop
num = 5 
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")


# create table from 1 to 10 using nested for lop
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("")