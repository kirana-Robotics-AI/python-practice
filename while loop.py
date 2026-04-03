#while loop 

is_faild = True
i = 1
while is_faild :#and i<=100:
    if i%2!= 0: #is not even 
       i= i + 1
       continue
    print(f"try{i}")
    i= i + 1
    if i>100:
        break

print("i gave up")


#counting
i=0

while i<=10:
    print(i)
    i +=1

    
#nested while loops

w = 0

while w <=10:
    x = 0
    while x<w:
        print("kiran", end="_")
        x+=1
    print("")
    w +=1
 
 #ATM PIN

pin = "1234"
trials = 1

while trials<=3:
    input_pin = input(f"Trail-{trials} | PIN :")
    trials +=1
    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
    





