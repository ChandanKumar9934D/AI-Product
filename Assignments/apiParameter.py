# Task 1

# Create a params dictionary containing:

# country = India
# page = 2
# limit = 10

# Then send those parameters using requests.get() to:

# https://example.com/users

import requests

params={
    "country":"India",
    "page":2,
    "limit":10

}

response=requests.get("https://example.com/users",
             params=params
             )

print(response.url)

# Task 1

# Write a POST request to:

# https://example.com/api/leads

# Send this data as JSON:
# import requests
lead={
    "name": "Rahul",
    "country": "Canada",
    "lead_origin": "Facebook"
}

response=requests.post("https://example.com/api/leads",json=lead)

print(response.status_code)

# Print the response status code.

datas=[
    {
        "id": 1,
        "name": "Aman"
    },
    {
        "id": 2,
        "name": "Rahul"
    },
    {
        "id": 3,
        "name": "Priya"
    }
]

for data in datas:
    print(data["name"])