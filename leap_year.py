year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ("Leap year.")
        else:
            print ("Not leap year.") #divided by 4
    else:
        print ("Leap year.") #divided by 100
else:
    print ("Not leap year.") #divided by 400