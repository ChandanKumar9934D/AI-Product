# Task 1 — GET request

# Write Python code that:

# Imports requests
# Sends a GET request to:
# https://example.com
# Prints the status_code.

import requests

response=requests.get("http://example.com")
print(response.status_code)