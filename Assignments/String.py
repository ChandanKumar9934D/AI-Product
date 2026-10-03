# Create a variable named name with the value "   aman kumar   ". Remove the extra spaces and print the name in title case.

name="   aman kumar   "
print(name.strip().title())

# Create a variable status = "Lead Status: New". Replace "New" with "Interested" and print the updated message.

# Expected output: Lead Status: Interested

status = "Lead Status: New"
print(status.replace("New","Interested"))

text = "  Python Programming  "
print(text.find("Pro"))