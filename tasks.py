from twilio.rest import TwilioRestClient
from invoke import task
import os


@task
def lunch_reminder(ctx):
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    client.messages.create(to=os.environ['MAX_PHONE'], from_=os.environ['TWILIO_PHONE'], body="Bring your lunch to work. It's in the fridge.")

@task
def rubbish_reminder(ctx, recycling=False):
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    if recycling:
        message = "Recycling and general rubbish needs to go out tonight."
        client.messages.create(to=os.environ['HOUSE_PHONES'], from_=os.environ['TWILIO_PHONE'], body=message)
    else:
        message = "The rubbish bin needs to go out tonight. No recycling this week."
        client.messages.create(to=os.environ['HOUSE_PHONES'], from_=os.environ['TWILIO_PHONE'], body=message)

@task
def test(ctx, recycling=False):
    client = TwilioRestClient(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    if recycling:
        message = "TEST Recycling and general rubbish needs to go out tonight."
        client.messages.create(to=os.environ['LILLY_PHONE'], from_=os.environ['TWILIO_PHONE'], body=message)
    else:
        message = "TEST The rubbish bin needs to go out tonight. No recycling this week."
        client.messages.create(to=os.environ['LILLY_PHONE'], from_=os.environ['TWILIO_PHONE'], body=message)
