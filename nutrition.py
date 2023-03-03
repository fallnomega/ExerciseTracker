import requests
import datetime
import os
import sheety


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
        self.exercise = ''
        self.duration_min = ''
        self.date_time = datetime.datetime.now()
        self.calories = 0
        self.workout_day = ''
        self.workout_time = ''
        self.get_sheety()

    def post_exercise_info(self):
        end_point = f'{self.website}/v2/natural/exercise'
        head = {'x-app-id': self.nutrition_id, 'x-app-key': self.nutrition_key, 'x-remote-user-id': self.dev_mode}
        json_body = {"query": "ran 5k and cycled for 20 minutes",
                     "gender": "female",
                     "weight_kg": 72.5,
                     "height_cm": 167.64,
                     "age": 30}
        requestor = requests.post(url=end_point, headers=head, json=json_body)
        requestor.raise_for_status()
        response = requestor.json()
        for x in response['exercises']:
            self.exercise = x['user_input']
            self.duration_min = x['duration_min']
            self.calories = x['nf_calories']
            self.workout_day = self.date_time.strftime('%d/%m/%Y')
            self.workout_time = self.date_time.strftime('%H:%M:%S')
            self.post_sheety()

    def get_sheety(self):
        my_sheety = sheety.Sheety()
        my_sheety.get_data()

    def post_sheety(self):
        payload = {'workout': {'exercise': self.exercise.title(), 'date': self.workout_day, 'time': self.workout_time,
                               'duration': self.duration_min,
                               'calories': self.calories}}
        post_to_sheety = sheety.Sheety()
        post_to_sheety.post_date(payload)
