# Create a dictionary named student with these values:
# Name: "Aman"
# Age: 22
# City: "Jalandhar"
# Print the student's name and age.

student={
    "Name": "Aman",
    "Age": 22,
    "City": "Jalandhar"
}

print(student.get("Name","not Provided"))
print(student.get("Age","not Provided"))

# Create a dictionary named lead with "name": "Rahul" and "status": "New". Then:
# Update the status to "Interested".
# Add "city": "Jalandhar".
# Print the final dictionary.

lead={
    'name':"Rahul",
    "status":"New",
}

lead["status"]="Interested"

lead['city']="jalandhar"

print(lead)