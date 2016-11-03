import json
from twilio.rest import TwilioRestClient

# Import config
with open('config.json') as data_file:    
    data = json.load(data_file)

# Twilio auth
account_sid = data["auth"]["sid"] # Account SID from www.twilio.com/console
auth_token  = data["auth"]["token"] # Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

# Send message
message = client.messages.create(
    body  = "This is a test sms message.",
    to    = data["numbers"]["mobile"], # Mobile number
    from_ = data["numbers"]["twilio"]) # Twilio number