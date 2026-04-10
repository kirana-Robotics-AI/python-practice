#dubling each element in a list
number = [1,2,3,45]
dubled = []
for num in number:
    dubled .append(num*2)
    print(dubled)

#looping through a dictionary
my_dict = {"name":"john","age":30,"city":"new york"}
for key in my_dict:
    print(key,my_dict[key])
    
#for loop with range()

students = ["kirana","manju","raghu"]
marks = [70,80,50]

student_marks = {}

for i in range(1,len(students),2): #step:steep:stop
    student_marks[students[i]] = marks[i]

print(student_marks)


for index, student in enumerate(students):
    student_marks[student] = marks[index]

print(student_marks)

for i in range(3):
    student_marks[students[i]] = marks[i]

print(student_marks)


#List comprehension in For  Loop 

l = [1,2,4,6]
dl = [item**2 for item in l] #[expresion for item in collection]

print(dl)

m = [n for n in range(1,12)]

ml = [n**2 for n in m if n%2 == 0]

print(ml)

r = ["kirana","mango","apple"]
print(r)

cl = [x[1] for x in r]
print(cl)

#dictionary comprrehansion

city = {
    "bangalore":75,
    "shimoga":55,
    "hubli":90
};

lc = {key:value for key,value in city.items() if value>60}

print(lc)

#letters in a list

names = ["kirana","mango","apple"]

d = {name:len(name) for name in names}

print (d)