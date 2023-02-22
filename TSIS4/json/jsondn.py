
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")

import json


with open('c:/Users/User/Desktop/python/TSIS4/json/sample-data.json', 'r') as file:
    data = json.load(file)

for obj in data['imdata']:
    print(obj['l1PhysIf']['attributes']['dn'], "                              inherit   9150 ")
