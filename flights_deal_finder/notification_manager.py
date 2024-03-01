from twilio.rest import Client  # Import Client class from Twilio package

# Twilio API credentials and phone numbers
TWILIO_SID = "SID"
TWILIO_AUTH_TOKEN = "AUTH_TOKEN"
TWILIO_VIRTUAL_NUMBER = "VIR_NUMB"
TWILIO_VERIFIED_NUMBER = "VER_NUMB"

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)  # Initialize Twilio client

    def send_sms(self, message):
        # Send SMS using Twilio client
        message = self.client.messages.create(
            body=message,  # SMS body
            from_=TWILIO_VIRTUAL_NUMBER,  # Virtual Twilio phone number
            to=TWILIO_VERIFIED_NUMBER  # Verified recipient phone number
        )
        print(message.sid)  # Print message SID for reference
