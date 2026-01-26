def fortune():

  import random
  number = random.randint(0, 7)
  
  #if number == 0:
  #  print("Don't pursue happiness – create it.")
  #elif number == 1:
  #  print("All things are difficult before they are easy.")
  #elif number == 2:
  #  print("The early bird gets the worm, but the second mouse gets the cheese.")
  #elif number == 3:
  #  print("Someone in your life needs a letter from you.")
  #elif number == 4:
  #  print("Don't just think. Act!")
  #elif number == 5:
  #  print("Your heart will skip a beat.")
  #elif number == 6:
  #  print("The fortune you search for is in another cookie.")
  #elif number == 7:
  #  print("Help! I'm being held prisoner in a Chinese bakery!")

  fortune = [
    "Don't pursue happiness – create it.",
    "All things are difficult before they are easy.",
    "The early bird gets the worm, but the second mouse gets the cheese.",
    "Someone in your life needs a letter from you.",
    "Don't just think. Act!",
    "Your heart will skip a beat.",
    "The fortune you search for is in another cookie.",
    "Help! I'm being held prisoner in a Chinese bakery!"
  ]

  print(fortune[number])

fortune()
fortune()
fortune()
