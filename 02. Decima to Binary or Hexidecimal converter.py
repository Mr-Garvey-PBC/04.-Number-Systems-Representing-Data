def decimal_to_binary():
    decimal_val=int(input('Enter a decimal value to convert to binary: '))   # Accept user input
    original_val=decimal_val   # Storing user input in a variable so i can recall the original input for a later
    binary_val=[]   # Declare an empty list to store binary values in

    while decimal_val >=1: 
        
        print(f'{decimal_val}/2 is {decimal_val//2} with remainder {decimal_val%2}')
        remainder=(decimal_val%2)  # Getting the modulus, it will always either be 0 or 1
        binary_val.append(remainder) # Adding modulus to the list
        decimal_val=decimal_val//2   # // is floor division, it returns a rounded down value from a division e.g 5//2 = 2 and not 2.5
        #input()

    binary_val.reverse()  # Reverse the binary list
    print('\n')
    print(f'{original_val} in binary form is {binary_val}') # Call on the original input storied in line 2 and display the contents of the reversed list

def decimal_to_hexadecimal():
    
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                        4: '4', 5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B',
                        12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    decimal_val=int(input('Enter a decimal value to convert to hex: '))   # Accept user input
    original_val=decimal_val   # Storing user input in a variable so i can recall the original input for a later
    hex_val=[]   # Declare an empty list to store hex values in

    while decimal_val >=1:
        print(f'{decimal_val}/16 is {decimal_val//16} with remainder {decimal_val%16}')
        remainder=(decimal_val%16)  # Getting the modulus, it will always be between 0 - 15
        remainder_convert=conversion_table[remainder] # Converting the remainder value into its corresponding hex val from the conversion table
                                                      # If the remainder was 15 then remainder_convert would be F
        hex_val.append(remainder_convert) # Adding modulus to the list
        decimal_val=decimal_val//16   # // is floor division, it returns a rounded down value from a division e.g 5//2 = 2 and not 2.5
        #input()
    hex_val.reverse()
    print(f'{original_val} in hex form is {hex_val}')

user_in=str(input('Do you want to convert to (b)inary or (h)ex: '))
while user_in!='xxx':

    if user_in=='b':
        decimal_to_binary()
    elif user_in=='h':
        decimal_to_hexadecimal()
    user_in=str(input('Do you want to convert to (b)inary or (h)ex: '))
    

