"""MY FIRST ASSIGNMENT""" #SWAP THE VARIABLE

fisrt_name = "John"
last_name = "Doe"

temp = fisrt_name
fisrt_name = last_name
last_name = temp




print (fisrt_name + " " + last_name)


#ASSIGNMENT

'''1. Create a BMI calculator, has the user to input their height,
 then ask for there weight then print out the BMI,
use format string to present your answer
BMI = weight (kg) ÷ height ** 2 (m) .

'''


weight = float(input("Enter your weight, in (kg): "))

height = float(input("Enter your height, in (m): "))

BMI = weight / (height ** 2)

print(BMI)



"""2. Write a Python program that calculates the area of
 a circle based on the radius entered by the user.
Area = PI * R ** 2
"""

import math

PI = math.pi

R = float(input("Enter Radius: "))
Area = PI * (R ** 2)
print(Area)

"""3. Write a Python program that Capitalize the first letter of every strings,
 you must get the string from user input"""

text = input("Enetr your words: ")
print(text.capitalize())

"""Write a Python program that Capitalize the every occurrence of “a” in a strings,
 you must get the string from user input"""

text = input("Enter your world: ")
print(text.replace("a", "A"))


"""Write a Python program that reverse a strings, you must get the string from user input.
"""


text = "Enetr your words: "
reverse_text = text[::-1]
print(reverse_text)


#ASSIGNMENT
"""1. Write a Python program that accepts a sequence of comma-separated numbers from
the user and generates a list and a tuple of those numbers."""

list_numbers = input("Enetr your number: ")
user_input = input("enter your number: ")
print(list[user_input.split(",")])
print(tuple(user_input.split(",")))

#2. Write a Python program that accepts user input and reverses the string.
str1 = input("Enter your string: ")
print(str1[::-1])

"""3. Write a Python program that accepts user input and converts the string to a list of
characters."""
user_input = input("input your string: ")
print(list(user_input))

#4. Write a Python program to get the smallest number from a list.
numbers = [10, 52, 28, 47, 90]
minimum_of_numbers = min(numbers)
print(minimum_of_numbers)

#5. Write a Python program to remove duplicates from a list.
list5 = ["age", "school","age", "bag", "phone", "powerbank"]
duplicate_list = set(list5)
print(list(duplicate_list))


#6. Write a Python program to check if a list is empty or not.
empty_list = []
print(empty_list)


#7. Write a Python program to select an item randomly from a list.

import random
random_list = ["age", "school","age", "bag", "phone", "powerbank"]
print(random.choice(random_list))

#8. Write a Python program to find common items in two lists.

items_w = ["cane corso", "golden retriver", "german shepard"]
items_w2 = ["german shepard", "rottweiler", "caucasian", "pibull"]
common_items =[]

for dog in items_w:
    for dogs in items_w2:
        if dog == dogs:
            common_items.append(dog)

print(common_items)




"""9. Write a Python program to convert a list of multiple integers into a single
integer."""

"""int_list = [1, 2, 3, 5, 6, 7, ]
print(int(int_list))"""

"""10. Write a Python program to select the odd numbers from a list, and create a 
new list from the odd numbers."""
the_list = [3, 4, 5, 6, 7, 8, 9]
odd_num = [odd for odd in the_list if odd % 2 != 0]
print(odd_num)




"""11. Write a Python program to print the following string in a specific format (see the
output)."""
sample_string = """Poodles are one of the most intelligent
and versatile dog breeds, \nmaking them an excellent choice 
for families. \nKnown for their distinctive curly coats and elegant 
appearance, \npoodles come in three sizes: Standard, Miniature, and Toy. """
print(sample_string)

#12. Write a Python program that accepts user input and reverses the string.
user = input("Enetr your words: ")
print(user[::-1])

#13. Write a Python program that reverses the list and tuples.

list_items = ["age", "school","age", "bag", "phone", "powerbank"]
tuple_items = ("age", "school","age", "bag", "phone", "powerbank")

print(list_items[::-1])
print(tuple_items[::-1])





"""
1. Write a Python program to find those numbers that are divisible by 7 and
multiples of 5, between 1500 and 2700 (both included).
Create a list of the answers

"""
"""new_list = []
for numbers in range(1500, 2700):
    if numbers % 7 == 0 and numbers % 5 == 0:
       new_list.append(numbers)
print(new_list)

def my_function():
    result_list = []
    for number in range(1500, 2700):
        if number % 7 == 0 and number % 5 == 0:
            result_list.append(number)
    return result_list"""


"""
2. Write a Python program to guess a number between 1 and 9.
Note: The user is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on a successful guess, the user
will get a "Well guessed!" message, and the program will exit.
Hint: Use the while loop and the random module in Python





import random
while True:
    user_input = int(input("Guess a number between 1 and 9 : "))
    if user_input == 3:
        print("Well guessed!")
        break"""



"""
3. Write a Python program to count the number of even and odd numbers in a
series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4



series_of_number = (1,2,3,4,5,6,7,8,9)
even_count = 0
for even in series_of_number:
    if even % 2 == 0:
        even_count +=1
print("Number of even numbers :", even_count)

odd_count = 0
for odd in series_of_number:
    if odd % 2 == 1:
        odd_count += 1
print("Number of odd numbers :", odd_count)"""

"""
4. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20


list_number = (1,2,3,4,5,6,7,8,9)
sum_list = sum(list_number)
print(sum_list)"""

"""1. Write a Python program to find those numbers that are divisible by 7 and
multiples of 5, between 1500 and 2700 (both included).
Create a list of the answers"""


def num_div_et_mul():
    new_list = []
    for num in range(1500, 2701):
        if num % 5 == 0 and num % 7 == 0:
            new_list.append(num)
            print(new_list)

num_div_et_mul()


"""2. Write a Python program to guess a number between 1 and 9.
Note: The user is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on a successful guess, the user
will get a "Well guessed!" message, and the program will exit.
Hint: Use the while loop and the random module in Python"""


import random
def guess_num():
    correct_guess = 3
    while True:
        user_input = int(input("Enter a guess between 1 and 9: "))
        if user_input == correct_guess:
            print("Correct guess!")
            return "You guessed it right!"


guess_num()

"""    3. Write a Python program to count the number of even and odd numbers in a
series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""



def count_even_et_odd(*numbers):
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"Number of even numbers: {even_count}\nNumber of odd numbers: {odd_count}"


result = count_even_et_odd(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(result)




"""4. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

def sum_all(*numbers): 
    total = 0
    for sumn in numbers:
        total = total + sumn
    return f"Expected Output : {total}"

print(sum_all(8, 2, 3, 0, 7))




"""5. Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument."""

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(5))


"""6. Write a Python function that accepts a string and counts the number of upper
and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""


def count_upper_and_lower(sample_string):
    upper_count = 0
    lower_count = 0
    sample_string = 'The quick Brow Fox'
    for letter in sample_string:
        if letter.isupper():
            upper_count+=1
        elif letter.islower():
            lower_count+=1
        
    return (f"No. of Upper case characters :{upper_count}")
    return (f"No. of Lower case characters :{lower_count}")
    

print(count_upper_and_lower())
