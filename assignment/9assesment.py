#Bus pass eligibality

age=int(input("Enter your age: "))

if age < 5:
    print("Bus pass is FREE")
elif age >=60:
    print("Senior citizen discount applied")
else:
    print("Full price ticket")

#Meal time checker

time= int(input("Enter time(0-23): "))

if time == 8:
    print("it's breackfast time")
elif time ==13:
    print("IT's lunch time")
elif time == 20:
    print("It's dinner time")
else:
    print("It's not meal time")

#Library membership eligibality

age = int(input("Enter your age: "))

if age < 18 :
    print("student membership")
elif age >= 60:
    print("senior citizen membership")
else :
    print("Regular membership")


#breackfast checker

time = int(input("Enter time (0-23): "))

if 6 <= time <= 10:
    print("It's breakfast time")
elif 12 <= time <= 15:
    print("It's lunch time")
elif 19 <= time <= 22:
    print("It's dinner time")
else:
    print("It's not meal time")