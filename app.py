from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# IMPORTANT: In a real production app, you would want to restrict the origins.
# For this deployment, we'll allow all origins for simplicity.
CORS(app) 

@app.route('/send_email', methods=['POST'])
def send_email():
    """
    This is a mock endpoint. In a real application, you would integrate
    an email sending service like SendGrid, Mailgun, or AWS SES here.
    For now, it just prints the received data to the console.
    """
    data = request.get_json()
    
    # Basic validation
    if not data or 'name' not in data or 'email' not in data or 'message' not in data:
        return jsonify({"message": "Missing data. Please fill out all fields."}), 400

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # --- MOCK EMAIL SENDING ---
    # In a real app, this is where you'd send an email.
    # For now, we just print to the server logs to confirm it's working.
    print("---------- CONTACT FORM SUBMISSION ----------")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")
    print("-------------------------------------------")
    
    # Return a success response
    return jsonify({"message": "Inquiry received successfully!"}), 200

if __name__ == '__main__':
    # Render will use a production WSGI server like Gunicorn, 
    # so this __main__ block is mostly for local testing.
    # The port is dynamically set by Render.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

