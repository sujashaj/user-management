from mailjet_rest import Client
import os

API_KEY = os.environ['MJ_APIKEY_PUBLIC']
API_SECRET = os.environ['MJ_APIKEY_PRIVATE']

class MailJetClient:

    def __init(self):
        self.mailjet = Client(auth=(API_KEY, API_SECRET)