# alexa_NotifyMe

This code is for an AWS Lambda to prompt your Amazon Alexa devices to run routines
This uses AWS SNS (or another event trigger for your Lambda), Lambda, Secrets Manager, and Virtual Buttons (https://www.patreon.com/posts/getting-started-31849096)

Virtual Button:
Register with Virtual Buttons to recieve one free button

Secrets Manager:
Create a new secret as 'SecretString': <api_key>
Name: VirtualButton-alexa
Make a note of which region you're using

Lambda:
Create a new Lambda, chose Python 3.6 or higher
Copy/Paste the code
In IAM for your current role add SecretsManager Read/Write (Preferred: create a custom role for just READ)

SNS:
Create new topic for your use case
Set to trigger, Lambda: <yourLambdaARN>
