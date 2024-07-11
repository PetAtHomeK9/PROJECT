def num_div_et_mul():
    list_of_numbers = []
    for numbers in range (1500, 2701):
        if numbers % 5 == 0 and numbers % 7 == 0:
            list_of_numbers.append(numbers)
    return list_of_numbers