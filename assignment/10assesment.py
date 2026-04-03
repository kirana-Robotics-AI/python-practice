'''Basic Counting with while Loop:
Write a program that counts from 1 to 10 using a while loop.'''

count=1
while count <=10:
    print(count)
    count+=1

'''Odd Numbers Printer:
Create a program that prints all odd numbers between 1 and 20 using a while loop.'''

i = 1
while i<=20:
    i%2==0 
    print(i)
    i+=2

#Ticket Booking Simulation:

available_seats = 8
booked_seats = 0

print("Welcome to the Bus Ticket Booking System!")
print(f"Total seats available: {available_seats}\n")

while available_seats > 0:
    print(f"Seats remaining: {available_seats}")
    passenger = input("Enter passenger name to book a seat: ")
    
    booked_seats += 1
    available_seats -= 1
    
    print(f"Seat {booked_seats} successfully booked for {passenger}!")
    print("-" * 40)

print("\nAll seats are booked.")
print(f"Total passengers booked: {booked_seats}")

'''Countdown Timer:
Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.'''

# Step 1: Initialize the counter variable
count = 10          # The countdown starts at 10

# Step 2: while loop — keeps running as long as count >= 1
while count >= 1:
    print(count)    # Step 3: Print the current number
    count -= 1      # Step 4: Decrease count by 1 each iteration

# Step 5: Loop has ended — print the final message
print("Happy New Year!")