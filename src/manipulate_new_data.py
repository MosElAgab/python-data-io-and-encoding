
from cars import import_json_data
from cars import print_data
from cars import print_keys
from cars import get_vin
from cars import get_cars

cars_data = import_json_data('./seeding_data/cars_data_1.json')

print(len(cars_data))
print(type(cars_data))
print_keys(cars_data)

my_list =  get_vin(cars_data, make='Ford')
my_other_list = get_cars(cars_data, make='Ford', colour = 'Light green')
# print(my_list)
for i in my_other_list:
    print(i)