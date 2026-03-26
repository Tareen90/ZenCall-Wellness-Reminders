from flask import Flask, request, jsonify
from twilio_handler import TwilioManager

app = Flask(__name__)

# Placeholder credentials for the review process
TWILIO_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxx'
TWILIO_TOKEN = 'your_auth_token_here'
TWILIO_NUMBER = '+1234567890'

# Initialize the Twilio Manager
twilio_manager = TwilioManager(TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER)

# Endpoint to schedule a new wellness call
@app.route('/schedule-call', methods=['POST'])
def schedule_call():
    data = request.json
    user_phone = data.get('phone')
    habit = data.get('habit') # e.g., "Hydration" or "Stretching"
    
    # Execute the Twilio call logic
    sid = twilio_manager.send_wellness_reminder(user_phone, habit)
    return jsonify({
        "status": "Success",
        "message": "Call Initiated",
        "sid": sid
    })

# Endpoint to handle user feedback during the call (DTMF)
@app.route('/voice-response', methods=['POST'])
def voice_response():
    digit = request.values.get('Digits') # The key pressed by the user
    if digit == '1':
        return "<Response><Say>Excellent! Your progress has been logged. Have a healthy day.</Say></Response>"
    
    return "<Response><Say>Thank you, we will remind you next time.</Say></Response>"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
