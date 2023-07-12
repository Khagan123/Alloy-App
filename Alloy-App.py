import requests

def submit_application(name_first, name_last, address_line_1, address_line_2, address_city, address_state, address_postal_code, address_country_code, document_ssn, email_address, birth_date):
    url = "https://sandbox.alloy.co/v1/evaluations/"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "first_name": name_first,
        "last_name": name_last,
        "address": {
        "line1": address_line_1,
        "line2": address_line_2,
        "city": address_city,
        "state": address_state,
        "zip_code": address_postal_code,
        "country": address_country_code
        },
        "ssn": document_ssn,
        "email": email_address,
        "date_of_birth": birth_date
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

def submit(name_first, name_last, address_line_1, address_line_2, address_city, address_state, address_postal_code, address_country_code, document_ssn, email_address, birth_date):
    url = "https://sandbox.alloy.co/v1/evaluations"
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "name_first": name_first,
        "name_last": name_last,
        "address_line_1": address_line_1,
        "address_line_2": address_line_2,
        "address_city": address_city,
        "address_state": address_state,
        "address_postal_code": address_postal_code,
        "address_country_code": address_country_code,
        "document_ssn": document_ssn,
        "email_address": email_address,
        "birth_date": birth_date
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        return None

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

 if response.status_code == 201:
    if response.json().get("outcome") == "Approved":
        return "Success"
    elif response.json().get("outcome") == "Manual Review":
        return "Thanks for submitting your application, we will be in touch shortly"
    elif response.json().get("outcome") == "Denied":
        return "Sorry, your application was not successful"
    else:
        return "Unknown outcome"
 elif response.status_code == 400:
     return "Invalid request. Please check the provided data."
 elif response.status_code == 401:
     return "Unauthorized. Please check your authentication credentials."
 else:
     return "Failed to submit application. An error occurred."

