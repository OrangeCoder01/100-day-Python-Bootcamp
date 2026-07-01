letter_ascii = []
for i in range(65, 91, 1): #Upper Case Letter
    letter_ascii.append(chr(i))

for i in range(97,123 ,1): #Lower Case Letter
    letter_ascii.append(chr(i))

letter_ascii.append(" ")
    


def user_validation():
    while True:
        user_type_input = input("Type \'encode\' to encrypt, type \'decode\' to decrypt: ").lower()
        if user_type_input == "encode":
            break       
        elif user_type_input == "decode":
            break      
        else:
            print("Wrong input, try again")
    
    
    while True:
        is_message_valid = True
        message = input("\nType your message: ")
        for char in message:
            if char not in letter_ascii:
                is_message_valid = is_message_valid and False
                break
        if not is_message_valid:
            print("Wrong input message")
        if is_message_valid:
            break
                
    while True:
        while True:
            shifting_input = input("\nType the shift number: ")
            try:
                shifting = int(shifting_input)
                break
            except ValueError:
                print("Invalid input")
                
        if -26 <= shifting <= 26:
            break
        else:
            print("The shifting is out of limit, try again")
        
    return user_type_input, message, shifting






def mapping_the_shifting(message, shifting):

    output = []

    for char in message:
        output.append(ord(char))

    for i in range(len(output)):
        element = output[i]
        if element != 32: # Ascii decimal equivalent for space
            if 65 <= element <= 90:
                element += shifting

                if element > 90:
                    element -= 26
                elif element < 65:
                    element += 26

            elif 97 <= element <= 122:
                element += shifting

                if element > 122:
                    element -= 26
                elif element < 97:
                    element += 26

        output[i] = element

    output_message = ""

    for value in output:
        output_message += chr(value)

    return output_message
  

def caesar_cipher():
    user_type_input, message_K, shifting_K = user_validation()

    if user_type_input == "decode":
        shifting_K = -1 * shifting_K
    
    output_message = mapping_the_shifting(shifting=shifting_K, message=message_K) #Applying Python's Key logic
    
    print(f"Here's the {user_type_input}d word and the result is: {output_message}")  
    
        

def endless_user_input_looping():
    choice = "yes"
    while True:
        if choice == "yes":
            caesar_cipher()
        
        choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if choice == "yes":
            continue
        elif choice == "no":
            break
        else:
            print("Illegal input, try again")
            
            
            

endless_user_input_looping()

    
    
    
    

    