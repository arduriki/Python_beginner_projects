print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#convert names into lower case
name_lower_case = name1.lower() + name2.lower()

#true count
t = name_lower_case.count("t")
r = name_lower_case.count("r")
u = name_lower_case.count("u")
e = name_lower_case.count("e")

true = int(t+r+u+e)

#love count

l = name_lower_case.count("l")
o = name_lower_case.count("o")
v = name_lower_case.count("v")
e = name_lower_case.count("e")

love = int(l+o+v+e)

#total score
score = int(str(true)+str(love))

#conditionals
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")