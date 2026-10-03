# Write code using with open() to create a file named student.txt and write "My name is Aman" into it.

with open("student.txt",'w') as file:
    file.write("My name is Aman")

# Write code using with open() to read student.txt and print its contents.

with open("student.txt","r") as file:
    result =file.read()
    print(result)