import csv

# import csv data into a list
def import_csv_data_into_a_list():
    data_holder = []
    with open('./data/pizza.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data_holder.append(row)
    return data_holder

data_holder = import_csv_data_into_a_list()

# organise the data in a list of dictioneries

def organise_data_into_list_of_dictionaries(data_list):
    dictionary_list = []
    for i, row in enumerate(data_list):
        if i == 0:
            continue
        dictionary_format = {}
        for k, key in enumerate(data_list[0]):
            dictionary_format[key] = row[k]
        dictionary_list.append(dictionary_format)
    return dictionary_list

pizza_dictionary_list = organise_data_into_list_of_dictionaries(data_holder)

# search cost by pizza name

def cost_by_name(pizza_name, pizza_data):
    for pizza in pizza_data:
        if pizza['Pizza'] == pizza_name:
            return pizza['Cost']

if __name__ == '__main__':    
    print(cost_by_name('Capri', pizza_dictionary_list))
    print('end')

# prints a list with each ingredient given the pizza name 

def ingredients_by_name(pizza_name, pizza_data):
    for pizza in pizza_data:
        if pizza['Pizza'] == pizza_name:
            if 'and' in pizza['Description']:
                ingredients = pizza['Description'].split(', ')
                for i, item in enumerate(ingredients):
                    if 'and' in item:
                        ingredients.append(item.split(' and ')[1])
                        ingredients[i] = item.split(' and ')[0]
                return ingredients    
            return pizza['Description'].split(', ')
            
if __name__ == '__main__':
    print(ingredients_by_name('Sorrento', pizza_dictionary_list))
    print(ingredients_by_name('Capri', pizza_dictionary_list))
    print('end')

# returns a list of all pizzas for given ingredients 

def pizzas_by_ingredient(ingredient, pizza_data):
    matching_pizzas = []
    for pizza in pizza_data:
        if ingredient in ingredients_by_name(pizza['Pizza'], pizza_data):
            matching_pizzas.append(pizza)
    return matching_pizzas

if __name__ == '__main__':
    for i in pizzas_by_ingredient('mushrooms', pizza_dictionary_list):
        print(i)
    print('end')

# Prints all of the pizzas under a 'Cost' from price low to high

def pizzas_with_cost_under(cost: int, pizza_data: list) -> list:
    matching_pizzas = []
    for pizza in pizza_data:
        pizza_cost = list(pizza['Cost'])
        pizza_cost.pop(0)
        pizza_cost = ''.join(pizza_cost)
        if float(pizza_cost) <= cost:
            matching_pizzas.append(pizza)
    return sorted(matching_pizzas, key=lambda d: d['Cost'])

if __name__ == '__main__':
    for i in pizzas_with_cost_under(8.9, pizza_dictionary_list):
        print(i)
    print('end')

# add Pizza 

def add_pizza(name: str, cost: str, description: str, calories: str, pizza_data: list) -> list:
    pizza_data.append({'Pizza': name, 'Cost': cost, 'Description': description, 'Calories': calories})
    return pizza_data

if __name__ == '__main__':
    add_pizza('sea food pizza', '£9.90', 'Cheese, tomato, prawns and tuna', '660kcal', pizza_dictionary_list)
    for i in pizza_dictionary_list:
        print(i)
    print('end')
    print(dir())