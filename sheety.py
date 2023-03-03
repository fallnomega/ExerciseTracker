import os
import requests


class Sheety:
    def __init__(self):
        self.endpoint = os.environ.get('ENDPOINT')

    def get_data(self):
        requestor = requests.get(url=self.endpoint)
        requestor.raise_for_status()
        print(requestor.text)

    def post_date(self, the_payload):
        print(the_payload)
        post_to_sheety = requests.post(url=self.endpoint, json=the_payload)
        post_to_sheety.raise_for_status()
        print(post_to_sheety.text)
