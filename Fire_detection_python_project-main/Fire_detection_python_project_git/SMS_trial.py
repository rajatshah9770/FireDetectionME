from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7b5949051acd06410eab673fd4e10057"
# Your Auth Token from twilio.com/console
auth_token  = "a096c164b331cb5c64cdf30018bc2b87"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918624049464", 
    from_="+16075644952",
    body="Hello from Python!")

print(message.sid)
