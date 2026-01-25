import random

number = int(input("Please insert a number from 1-10 to create a list: "))
list = []

for item in range(1, number+1): 
  list.append(item)

list_max = max(list)

list_min = min(list)

list_nr = len(list)

total = sum(list)

print(f'The lowest number from your list is {list_min} and the highest one is {list_max} that means your list has {list_nr} items and if you sum all of the items you get {total}.')
