import json
import random
import uuid
from cars import print_data
from cars import csv_to_json
from cars import add_car
from cars import list_all_by_key
from cars import save_data_into_csv
from cars import save_data_into_json
from cars import import_json_data


with open('./data/cars.json', 'r', encoding='utf-8') as f:
    cars_data = json.load(f)['cars']


cars_make = list_all_by_key('make', cars_data)
cars_make.extend(['Abarth', 'Alfa Romeo', 'Audi', 'BMW', 'Bentley'])
cars_make = list(set(cars_make))
cars_colour = list_all_by_key('colour', cars_data)
cars_colour.extend(['White', 'Black', 'Silver', 'Blue', 'Dark Blue', 'Green', 'Dark green', 'Light green', 'Gray', 'Gold', 'Orange'])
cars_colour = list(set(cars_colour))
cars_model = list_all_by_key('model', cars_data)




def generate_cars(make_list, models_list, colours_list, number_of_cars=10, range_of_years=[1990, 2023]):
    new_data_list = []
    for i in range(1, (number_of_cars + 1)):
        vin = str(uuid.uuid4())[0:17]
        make = random.choice(make_list)
        model = random.choice(models_list)
        year = random.choice(range(range_of_years[0], (range_of_years[1] + 1)))
        colour = random.choice(colours_list)
        new_data_list.append({'vin': vin, 'make': make, 'model': model, 'year': year, 'colour': colour})
    return new_data_list




new_data = generate_cars(cars_make, cars_model, cars_colour, 1000, [2004, 2023])
save_data_into_csv('./seeding_data/cars_data_1.csv', new_data)
save_data_into_json('./seeding_data/cars_data_1.json', new_data)

