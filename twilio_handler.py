import os
from twilio.rest import Client

class TwilioManager:
    def __init__(self, account_sid, auth_token, from_number):
        # Initialize the Twilio client with account credentials
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_wellness_reminder(self, to_number, habit_name):
        # Crafting the TwiML response for the voice call
        # This uses high-quality TTS to speak to the user
        twiml = f"""
        <Response>
            <Say language="en-US" voice="alice">
                Hello, this is your ZenCall assistant. It is time for your {habit_name}. 
                Please press 1 if you have completed this task.
            </Say>
            <Gather numDigits="1" action="/voice-response" method="POST" timeout="10">
                <Say language="en-US">Press 1 to confirm completion.</Say>
            </Gather>
        </Response>
        """
        
        # Trigger the actual phone call
        call = self.client.calls.create(
            twiml=twiml,
            to=to_number,
            from_=self.from_number
        )
        return call.sid
