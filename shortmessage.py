#!python
# -*- coding: UTF-8 -*-

# http://twilio.com/
# pip install twilio

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # get from http://twilio.com/
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # get from http://twilio.com/
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+185xxxxxxxx', # get from http://twilio.com/
                              body='test123',
                              to='+86185xxxxxxxx' # your number
                          )

print(message.sid)