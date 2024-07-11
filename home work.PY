"""8. Create a `for` loop that prints numbers from 1 to 20, and uses `pass` for numbers
 divisible by 5 without affecting the output.

9. Implement a `for` loop that iterates through a list of integers and prints the sum 
of the numbers until it encounters a negative number, at which point it stops using `break`.

10. Write a `for` loop that prints the first 10 Fibonacci numbers, but skips printing 
the number 8 using `continue`."""



"""1. Write a `for` loop that prints numbers from 1 to 10, but stops if the number is 5 using 
`break`"""



list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in list_of_numbers:
    print(number)
    if number == 5:
            break

"""
        2. Create a `for` loop that prints all even numbers from 1 to 20, but skips the number 
10 using `continue`."""






"""3. Implement a `for` loop that iterates through a list of numbers and prints each number. 
Use `pass` inside the loop without affecting the output."""



"""4. Write a `for` loop that prints the squares of numbers from 1 to 15, but stops if the 
square is greater than 100 using `break`."""


      

      """5. Create a `for` loop that prints numbers from 1 to 30, but skips numbers divisible 
by 3 using `continue`."""



"""6. Implement a `for` loop that iterates over a string and prints each character,
 but skips printing the character 'a' using `continue`."""

string_charcter = ["German Shepard", "Poodle", "Golden retreiver", "St benard", "Pomerian"]
for character in string_charcter:
    if "a" in character:
          continue
    print(character)


"""7. Write a `for` loop that prints numbers from 1 to 50, but stops the loop if it
 encounters a number that is both divisible by 4 and 7 using `break`.
"""

