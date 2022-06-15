print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120: #height is more or equals to, colon for writing the rule.
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  #nested if statements / 1st block
  
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
    #elif = else if, we can add as much as we want
  elif age <= 18: #age is more than 12 or equals to 18
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55: #has to fulfill both conditions
      print ("Everything is going to be ok. Have a free ride on us!")
  else: #final statement, anybody more than 18
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo? Y or N. ")
  if wants_photo == "Y": #same indentation level
    bill += 3 #sums 3

  print(f"Your final bill is ${bill}")
    
else:
  print("Sorry, you have to grow taller before you can ride.")