bill = float(input("Welcome to the tip calculator!\nWhat was the total bill? €"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percentage_0 = tip / 100
percentage_1 = bill * percentage_0
percentage_total = bill + percentage_1

total_each = percentage_total / people

rounded = round(total_each, 2)
rounded = "{:.2f}".format(total_each)

print(f"Each person should pay: €{rounded}")