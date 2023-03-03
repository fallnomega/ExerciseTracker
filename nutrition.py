import requests
import datetime
import os


class Nutritionix:
    def __init__(self, my_age, my_gender, my_height, my_weight):
        self.nutrition_key = os.environ.get('NUTRIT_KEY')
        self.nutrition_id = os.environ.get('NUTRIT_ID')
        self.website = 'https://trackapi.nutritionix.com'
        self.dev_mode = '0'
        self.gender = my_gender
        self.age = my_age
        self.height = my_height
        self.weight = my_weight

    def get_exercise_info(self):
        end_point = f'{self.website}/v2/natural/exercise'
        print(end_point)
        head = {'x-app-id': self.nutrition_id, 'x-app-key': self.nutrition_key, 'x-remote-user-id': self.dev_mode}
        json_body = {"query": "ran 2 miles and walked for 3km",
                     "gender": "female",
                     "weight_kg": 72.5,
                     "height_cm": 167.64,
                     "age": 30}
        requestor = requests.post(url=end_point, headers=head,json=json_body)
        requestor.raise_for_status()
        print(requestor.text)
