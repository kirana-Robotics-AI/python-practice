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

for i in range(len(students)):
    student_marks[students[i]] = marks[i]

print(student_marks)


for index, student in enumerate(students):
    student_marks[student] = marks[index]

print(student_marks)

for i in range(3):
    student_marks[students[i]] = marks[i]

print(student_marks)
               