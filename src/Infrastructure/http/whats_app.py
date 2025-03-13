from twilio.rest import Client

account_sid = 'sid code'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

verification = client.verify \
    .v2 \
    .services('service code') \
    .verifications \
    .create(to='phone number', channel='sms')

print(verification.sid)
