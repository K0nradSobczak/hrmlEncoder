from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

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

    # Extract company names that are in the specific div class 'x_x_lead-name'
    company_names = [tag.get_text(strip=True) for tag in soup.find_all('div', class_='x_x_lead-name')]

    # Return the extracted company names as JSON
    return jsonify({'company_names': company_names})

if __name__ == '__main__':
    app.run(debug=True)
