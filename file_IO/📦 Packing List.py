import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
packing_list = os.path.join(script_dir, 'packing_list.csv')

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open(packing_list, 'r', encoding='utf8') as file:
    
        csv_reader = csv.reader(file)

        for line in csv_reader:
            print(line)

except FileNotFoundError:
    # if file doesnt exist then:
    print("Packing list file not found. Creating a new one.")

    with open(packing_list, 'w', newline='', encoding='utf8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
