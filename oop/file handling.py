# Reading a file using with statement
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a file using with statement
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
