# Create this Python dictionary:
import json
employee = {
    "name": "Rahul",
    "age": 30,
    "department": "Sales"
}
result=json.dumps(employee)
print(result)


# What will this code print?

import json

data = '{"name": "Priya", "age": 28}'

person = json.loads(data)

print(person["name"])#Priya
print(person["age"])#28

