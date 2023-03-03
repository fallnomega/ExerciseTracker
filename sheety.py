import os
import requests


class Sheety:
    def __init__(self):
        self.endpoint = os.environ.get('ENDPOINT')
        self.token = os.environ.get('SHEETY_TOKEN')
        self.sheety_headers = {'Authorization': f'Bearer {self.token}'}

    def get_data(self):
        requestor = requests.get(url=self.endpoint,headers=self.sheety_headers)
        requestor.raise_for_status()
        # print(requestor.text)

    def post_date(self, the_payload):
        post_to_sheety = requests.post(url=self.endpoint, json=the_payload, headers=self.sheety_headers)
        post_to_sheety.raise_for_status()
        # print(post_to_sheety.text)
