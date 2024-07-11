1. Write a Python program to find those numbers that are divisible by 7 and
multiples of 5, between 1500 and 2700 (both included).
Create a list of the answers

new_list = []
for numbers in range(1500, 2701):
    if numbers % 7 == 0 and numbers % 5 == 0:
       new_list.append(numbers)
print(new_list)

def Number_div_et_mul():
    result_list = []
    for number in range(1500, 2700):
        if number % 7 == 0 and number % 5 == 0:
            result_list.append(number)
    return result_list


"""2. Write a Python program to guess a number between 1 and 9.
Note: The user is prompted to enter a guess. If the user guesses wrong then the
prompt appears again until the guess is correct, on a successful guess, the user
will get a "Well guessed!" message, and the program will exit.
Hint: Use the while loop and the random module in Python"""





import random
while True:
    user_input = int(input("Guess a number between 1 and 9 : "))
    if user_input == 3:
        print("Well guessed!")
        break




"""3. Write a Python program to count the number of even and odd numbers in a
series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""



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
print("Number of odd numbers :", odd_count)


"""4. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20"""


list_number = (1,2,3,4,5,6,7,8,9)
sum_list = sum(list_number)
print(sum_list)




"""6. Write a Python function that accepts a string and counts the number of upper
and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""



user_string = input()
def upper_and_lower(n):
    upper_count = 0
    lower_count = 0
    for nums in n:
        if nums.isupper():
            upper_count+=1
    return upper_count


n = 10
i = 0
while i <= 10:
    if i == 7:
        i += 1
    print(i)
    break
    

giant_breed = ["German Shepard", "Cane Corso", "Kangal Shepard", "St Benard"]
toy_breed = ["Poodle", "Lhasa", "Eskimo", "Pomerian", "Pug"]
giant_breed.extend(toy_breed)
print(giant_breed)

def fullname(fname,lname):
    print("My Name is "+ fname, lname)
fullname("john", "joe")

