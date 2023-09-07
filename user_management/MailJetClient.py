from mailjet_rest import Client
import os

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['API_SECRET']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_NAME = os.environ['SENDER_NAME']



class MailJetClient:

    def __init(self):
        self.mailjet = Client(auth=(API_KEY, API_SECRET), version='v.31')


    def send_email(self, receiver_email, receiver_name):
        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "{}".format(SENDER_EMAIL),
                        "Name": "{}".format(SENDER_NAME)
                    },
                    "To": [
                        {
                            "Email": "{}".format(receiver_email),
                            "Name": "{}".format(receiver_name)
                        }
                    ],
                    "Subject": "Please verify your email address!",
                    "TextPart": "Greetings from user management application!",
                    "HTMLPart": "May the delivery force be with you!"
                }
            ]
        }
        result = self.mailjet.send.create(data=data)
        return result.status_code



