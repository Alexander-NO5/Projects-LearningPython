def get_item(option):
  if option == 1:
    item = '🍔 Cheeseburger'
  elif option == 2:
    item = '🍟 Fries'
  elif option == 3:
    item = '🥤 Soda'
  elif option == 4:
    item = '🍦 Ice Cream'
  elif option == 5:
    item = '🍪 Cookie'
  return item

def welcome():
  print('Welcome to our fast food!')
  print('Menu')
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4 🍦 Ice Cream')
  print('5 🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))
