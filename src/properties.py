import xml
import xml.etree.ElementTree as ET
from cars import save_data_into_json as s_json
from cars import save_data_into_csv as s_csv


data = ET.parse('./data/properties.xml')
root = data.getroot()

print(root)

properties_data = {key.tag: {key2.tag: {key3.tag: {key4.tag: key4.text for key4 in key3} for key3 in key2} for key2 in key} for i, key in enumerate(root)}
# z = 
# print(properties_data['rent']['detached'])
print([(key, value) for key, value in properties_data['rent']['detached'].items()])
print('end')
print([key for key, value in properties_data.items()])
print([key for key, value in properties_data['rent'].items()])
print([key for key, value in properties_data['rent']['detached'].items()])
data_list = []
for i, bussines_type in enumerate([key for key, value in properties_data.items()]):
    for k, property_type in enumerate([key for key, value in properties_data[bussines_type].items()]):
        for j, property_name in enumerate([key for key, value in properties_data[bussines_type][property_type].items()]):
            properties_data[bussines_type][property_type][property_name]['name'] = property_name + '_' + property_type + '_' + bussines_type
            properties_data[bussines_type][property_type][property_name]['property_type'] = property_type
            properties_data[bussines_type][property_type][property_name]['bussines_type'] = bussines_type
            data_list.append(properties_data[bussines_type][property_type][property_name])
            # print(properties_data[bussines_type][property_type][property_name]['name'])

# for i in data_list:
#     print(i['name'], i['bedrooms'], i['bathrooms'], i['property_type'], i['bussines_type'])
# s_json('./data/properties.json', data_list)
# s_csv('./data/properties.csv', data_list)