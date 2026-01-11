weight = float(input("Please insert your Earth weight: "))

planet = int(input("Please insert the planet number (1-7): "))

destination_weight = 0

if planet == 1:
  destination_weight = weight * 0.38 #Relative Gravity
  print("Your weight on Mercury will be: " + str(destination_weight))
elif planet == 2:
  destination_weight = weight * 0.91 #Relative Gravity
  print("Your weight on Venus will be: " + str(destination_weight))
elif planet == 3:
  destination_weight = weight * 0.38 #Relative Gravity
  print("Your weight on Mars will be: " + str(destination_weight))
elif planet == 4:
  destination_weight = weight * 2.53 #Relative Gravity
  print("Your weight on Jupiter will be: " + str(destination_weight))
elif planet == 5:
  destination_weight = weight * 1.07 #Relative Gravity
  print("Your weight on Saturn will be: " + str(destination_weight))
elif planet == 6:
  destination_weight = weight * 0.89 #Relative Gravity
  print("Your weight on Uranus will be: " + str(destination_weight))
elif planet == 7:
  destination_weight = weight * 1.14 #Relative Gravity
  print("Your weight on Neptune will be: " + str(destination_weight))
else:
  print("Invalid planedn number")
