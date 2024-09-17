from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

# Webhook endpoint to receive HTML and extract company names
@app.route('/extract', methods=['POST'])
def extract_company_names():
    # Get the 'html_code' from the POST request form data (x-www-form-urlencoded)
    html_code = request.form.get('html_code', '')  # Extract the html_code parameter from form data
    
    if not html_code:
        return jsonify({'error': 'No HTML code provided'}), 400

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_code, 'html.parser')

    # Extract all text from the HTML
    text = soup.get_text()

    # Use a regex pattern to match likely company names (example based on given data)
    # The assumption is company names will follow a pattern like:
    # Opendns, LLC, Provector.pl, etc.
    company_names = re.findall(r'\b[A-Za-z\s,\.]+(?:LLC|Group|pl|I|Company|Apartments|Development)\b', text)

    # Return the extracted company names as JSON
    return jsonify({'company_names': company_names})

if __name__ == '__main__':
    app.run(debug=True)
