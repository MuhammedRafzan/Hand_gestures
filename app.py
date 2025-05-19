from flask import Flask, request
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Twilio credentials (get these from your Twilio account)
account_sid = 'YOUR_TWILIO_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'
client = Client(account_sid, auth_token)

@app.route('/send', methods=['POST'])
def send_sms():
    data = request.json
    phone = data['phone']
    message = data['message']
    
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=phone
    )
    return {'status': 'sent'}

if __name__ == '__main__':
    app.run(debug=True)
