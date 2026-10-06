# Write code using with open() to create a file named student.txt and write "My name is Aman" into it.

with open("student.txt",'w') as file:
    file.write("My name is Aman")

# Write code using with open() to read student.txt and print its contents.

with open("student.txt","r") as file:
    result =file.read()
    print(result)


import json
employee = {
    "name": "Rahul",
    "age": 30,
    "department": "Sales"
}
with open("employee.json","w") as file:
    file.write(json.dumps(employee))


customer = {
    "name": "Aman",
    "phone": "9876543210",
    "country": "Canada"
}

with open("customer.json","w") as file:
    file.write(json.dumps(customer))

# Write Python code to open customer.json, read the JSON data using json.load(), and print the customer's name.

with open("customer.json","r") as file:
    resultValue=json.loads(file.read())
    print(resultValue.get('name',"name not provided"))
    