"""4. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

#define the function,,,,we use pass  *args for multiples parameters
def sum_num_in_list(*numbers):
#loop through
    total = 0
    for nums in numbers:
        total += nums
#returns the variable
    return total


print(sum_num_in_list(8, 2, 3, 0, 7))


"""6. Write a Python function that accepts a string and counts the number of upper
and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12"""

def count_nums_upp_n_lwr(sample_strings):
    for up in sample_strings:
        for lw in sample_strings:
            print("No. of Upper case character:".isupper + up)
            print("No. of Lower characters :".islower + lw)
    return 


count_nums_upp_n_lwr("The quick Brow Fox")


