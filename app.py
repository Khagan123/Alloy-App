from flask import Flask, Response, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
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

    response = application(name_first, name_last, address_line_1, address_line_2, address_city, address_state, address_postal_code, address_country_code, document_ssn, email_address, birth_date)
    result = process_response(response)

    return render_template('index.html', result=result)

def application(name_first, name_last, address_line_1, address_line_2, address_city, address_state, address_postal_code, address_country_code, document_ssn, email_address, birth_date):
    url = "https://sandbox.alloy.co/v1/evaluations"
    headers = {
        "Content-Type": "application/json"
    }
    applicant_data = {
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

    auth = ("bvy7Xi6u0MPna139eHZ8IXS7pe1kHIan", "InWcJP9jmD2nIoPvf6zuBZiR2VuVBU0l")

    response = requests.post(url, headers=headers, auth=auth, json=applicant_data)
    return response

def process_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    app.run()
