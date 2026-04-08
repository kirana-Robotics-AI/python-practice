# Write a for loop that prints all multiples of 3 between 1 and 30.

for i in range(1,31):
    if i % 3 == 0:
        print(i, end=" ")
print("")

#another way
for i in range(3,31,3):
    print(i ,end=" ")
print("")


#Write a program using a for loop that calculates the sum of numbers from 1 to 10.

total_sum = 0
for i in range(1,11):
    total_sum += i
print(f"The sum of numbers from 1 to 10 is: {total_sum}")

#Write a program that takes your name as input and prints each letter of your name using a for loop.
name = input("Enter your name: ")
for letter in name:
    print(letter)

#Write a program that counts how many vowels are in a given string using a for loop.
input_string = input("Enter a string: ")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char in vowels:
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}")

#another way

vowel_count = 0
for char in input_string:
    if char.lower() in "aeiou":
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}")