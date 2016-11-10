from twilio.rest import TwilioRestClient

account_sid = "AC0deaeaacabb6abf64e3f0d0e3c8a08fa" # Your Account SID from www.twilio.com/console
auth_token  = "         ***       "  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Testing Twilio from python",
    to="+5565992510498",    # Replace with your phone number
    from_="+553139587769") # Replace with your Twilio number

print(message.sid)
