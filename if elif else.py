#if-elif-else is a conditional statement

signal=input("what is the colour of the signal:").lower()

if signal=="red":
    print("stop")
elif signal=="yellow":
    print("reday")
else:
    print("go")

#logical operater and or not
att=65
is_techer_friend=True

if att>=75 or is_techer_friend:
    print("take exam")
elif is_techer_friend==True:# here you can take or not take th true it automaticle check boolean
     print("take exam")
else:
    print("no exam")


#bus ticket in karnatka
gender= input("gender:").upper()
age=int(input("age:"))

if gender=="female":
    print("ticket is free")
else:
    if age<5:
        print("ticket is free")
    elif age <=12:
        print("you get a child discount.")
    elif age>=60:
        print("you get a senior citizen discount")
    else:
        print("you pay the full fare.")






