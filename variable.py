age = input("Age: ")
print(age)

boy_name= input("Boy name: ")
boy_age= int(input("Boy age: "))
girl_name= input("Girl name: ")
girl_age= int(input("Girl_age: "))

age_diff =abs(boy_age - girl_age)
 
print(boy_name + " loves "+girl_name + " age diffrence is " + str(age_diff))

print(f"{boy_name} loves {girl_name}. Age diffrenece {age_diff}")