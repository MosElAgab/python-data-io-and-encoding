from pizza import pizza_dictionary_list
import json
import csv


def import_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        cars_data = json.load(f)
    return cars_data
cars_data = import_json_data('./data/cars.json')['cars']


def print_data(cars_data):
    print('data => ')
    for i in cars_data:
        print(i)
    
def print_keys(cars_data):
    cars_dict_keys = [key for key, value in cars_data[0].items()]
    print('keys => ')
    print(cars_dict_keys)
    return cars_dict_keys


# if __name__ == '__main__':
#     print_data(cars_data)

# import pizza data and save it as json dict

def csv_to_json(file_path, csv_file_path):
    csv_data = []
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for item in reader:
            csv_data.append(item)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(csv_data, f)

# if __name__ == '__main__':
#     csv_to_json('./data/pizza_dict.json', './data/pizza.csv')

# require all vin by make, model, year and  colour
# only make should be positional 
#  
# print(cars_data)
def get_car_by_vin():
    pass
def get_vin(cars_data, **keys):
    available_keys = [key for key, value in keys.items()]
    print('filtered by =>', available_keys)
    matching_cars = []
    for car in cars_data:
        pass_list = []
        for available_key in available_keys:
            if car[available_key] == keys[available_key]:
                pass_list.append(True)
            else:
                pass_list.append(False)
        if False not in pass_list:
            matching_cars.append(car['vin'])
    if len(matching_cars) == 0:
        return 'No matchinh :('
    return matching_cars

def get_cars(cars_data, **keys):
    available_keys = [key for key, value in keys.items()]
    print('filtered by =>', available_keys)
    matching_cars = []
    for car in cars_data:
        pass_list = []
        for available_key in available_keys:
            if car[available_key] == keys[available_key]:
                pass_list.append(True)
            else:
                pass_list.append(False)
        if False not in pass_list:
            matching_cars.append(car)
    if len(matching_cars) == 0:
        return 'No matchinh :('
    return matching_cars

# if __name__ == '__main__':
#     print(get_vin(cars_data, year=1999))

# add car 

def add_car(vin, make, model, year, colour, cars_data):
    new_car = {'vin': vin, 'make': make, 'model': model, 'year': year, 'colour': colour}
    cars_data.append(new_car)

if __name__ == '__main__':
    add_car('WVGAV3AX5EW889345', 'Ford', 'Fiesta', 2011, 'Silver', cars_data)
    add_car('WVGAV3AX5EW8WE34Q', 'VW', 'Golf', 2018, 'Dark Blue', cars_data)

# edit data given vin

def edit_car_given_vin(vin, cars_data, **keys):
    valid_keys = [key for key, value in cars_data[0].items()]
    available_keys = [key for key, value in keys.items() if key in valid_keys]
    print('AA', available_keys)
    for i, car in enumerate(cars_data):
        if car['vin'] == vin:
            for available_key in available_keys:
                cars_data[i][available_key] = keys[available_key]
            return cars_data
    return 'either invalid venv or invalid keys to edit'

if __name__ == '__main__':
    print('edit_car_given')
    print(edit_car_given_vin('WVGAV3AX5EW889767', cars_data, make='VW', model='Golf', dog='how'))

# prints all different make we have 

def list_all_make(cars_data):
    make_list = []
    for car in cars_data:
        make_list.append(car['make'])
    make_list = list(set(make_list))
    return make_list

if __name__ == '__main__':
    print('list_all_make')
    print(list_all_make(cars_data))

# List all values by key 

def list_all_by_key(key, cars_data):
    if key not in [key for key, value in cars_data[0].items()]:
        raise Exception('invalid key')
    values_list = []
    for car in cars_data:
        values_list.append(car[key])
    values_list = list(set(values_list))
    return values_list

if __name__ == '__main__':
    print('list_all_by_key')
    print(list_all_by_key('make', cars_data))
# save data as json file (update)
def save_data_into_json(file_path, cars_data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(cars_data, f)

if __name__ == '__main__':
    save_data_into_json('./data/new_cars.json', cars_data)
# save data as csv file 

def save_data_into_csv(file_path, cars_data):
    header_keys = [key for key, value in cars_data[0].items()]
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header_keys)
        writer.writeheader()
        for car in cars_data:
            writer.writerow(car)

if __name__ == '__main__':
    save_data_into_csv('./data/new_car.csv', cars_data)

