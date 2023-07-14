import requests

def submit_application(name_first, name_last, address_line_1, address_line_2, address_city, address_state, address_postal_code, address_country_code, document_ssn, email_address, birth_date):
    url = "https://sandbox.alloy.co/v1/evaluations/"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "Jessica": name_first,
        "Deny": name_last,
        "address": {
        "123 Main St": address_line_1,
        "Apt 4B": address_line_2,
        "New York": address_city,
        "NY": address_state,
        "10001": address_postal_code,
        "US": address_country_code
        },
        "123456789": document_ssn,
        "johndoe@example.com": email_address,
        "1990-05-15": birth_date
    }

#Basic Authentication for Alloy API

    url = "https://sandbox.alloy.co/v1/evaluations"
    headers = {
        "Content-Type": "application/json"
    }

    auth = ("bvy7Xi6u0MPna139eHZ8IXS7pe1kHIan", "InWcJP9jmD2nIoPvf6zuBZiR2VuVBU0l")  
    data = {
        "name_first": "Jessica",
        "name_last": "Deny",
        "address_line_1": "123 Main St",
        "address_line_2": "Apt 4B",
        "address_city": "New York",
        "address_state": "NY",
        "address_postal_code": "10001",
        "address_country_code": "US",
        "document_ssn": "123456789",
        "email_address": "johndoe@example.com",
        "birth_date": "1990-05-15"
    }

    response = requests.post(url, headers=headers, auth=auth, json=data)
    print(response.json())

# Example usage
name_first = "Jessica"
name_last = "Deny"
address_line_1 = "123 Main St"
address_line_2 = "Apt 4B"
address_city = "New York"
address_state = "NY"
address_postal_code = "10001"
address_country_code = "US"
document_ssn = "123456789"
email_address = "johndoe@example.com"
birth_date = "1990-05-15"

response = submit_application(name_first, name_last, address_line_1, address_line_2, address_city, address_state, address_postal_code, address_country_code, document_ssn, email_address, birth_date)

def process_response(response):

    if response:
        return response.text
    