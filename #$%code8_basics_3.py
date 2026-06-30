# Day {3}

# Challenge {1}
# input_integer = int(input("Enter an integer: "))

# if input_integer % 2 == 0:
#     print("This is an even number:")
# else:
#     print("This is an odd number")
    
# Challenge {2}

age = int(input("Please, enter your age: "))
height = int(input("Please, enter your height "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    if age < 12:
        bill += 5
        print("Child ticket are $5")
        
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7")
        
    elif age > 18 and age < 45:
        bill += 12
        print("Adult tickets are $12")
        
    elif age >= 45 and age <=55:
        print("you do not need to pay, you have a midlife crisis")
        
    want_photo = input("Do want a photo? Write Y for yes")
    if want_photo == "Y":
        bill += 3
else:
    print("Unfortunately, you can not ride the rollercoaster")

    