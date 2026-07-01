# Day {8}
# Challeng# {1}:

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}")

greet_with("Yassin", "Cairo")

print("\n"*2)
# Challenege {2}
greet_with("Nowhere", "Jack Bauer") 
print("\n"*2)

# Challenge {3} Keyword Argument:

greet_with(location="Cairo", name="Yassin")

name_L = input("Enter your name: ")
location_L = input("Enter your location: ")

greet_with(name=f"{name_L}",location=f"{location_L}")
greet_with(location=f"{location_L}",name=f"{name_L}")