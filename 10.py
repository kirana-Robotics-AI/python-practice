#while loop

is_faild = True
i = 1
while is_faild :#and i<=100:
    if i%2!=0: #is not even 
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

   