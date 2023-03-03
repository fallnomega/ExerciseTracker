import os
import nutrition
import sheety

my_weight = os.environ.get('WEIGHT')  # kilograms
my_height = os.environ.get('HEIGHT')  # centimeters
my_gender = os.environ.get('GENDER')
my_age = os.environ.get('AGE')
my_exercise = nutrition.Nutritionix(my_age, my_gender, my_height, my_weight)
my_exercise.post_exercise_info()
