# Project {2} bill calculator

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? $ 10, 12, or 15? ")
num_of_individuals = input("How many people to split the bill? ")

bill_per_individual = (float(bill) + (float(tip_percentage)/100)*float(bill))/(int(num_of_individuals))

print(f"Each person should pay: ${round(bill_per_individual, 2)}")