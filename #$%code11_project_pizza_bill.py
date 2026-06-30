
print("Welcome to Python Pizza Deliveries!")
pizza_size = input("What size pizza do you want? S, M, or L ")
pepperoni_choice = input("Do you want pepperoni? Y or N ")
extra_cheese_choice = input("Do you want extra cheese? Y or N ")

extra_cheese_cost = 0
    
if extra_cheese_choice == "Y":
    extra_cheese_cost = 1
    

pizza_size_cost = 0
final_bill = 0
pepperoni_cost = 3

if pizza_size == "S":
    pizza_size_cost = 15
    if pepperoni_choice == "Y":
        pepperoni_cost = 2

elif pizza_size == "M":
    pizza_size_cost = 20

else:
    pizza_size_cost = 25

final_bill = pizza_size_cost + pepperoni_cost + extra_cheese_cost

print(f"Your final bill is: ${final_bill}")
