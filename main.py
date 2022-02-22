def get_a_password():
    import random
    from random import randint

    # Create two arrays with uppercase and lowercase letters 
    upper_cases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_cases = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # Create an array with specials characters  
    special_signs = ['>','$','%','?','.','€','#','@','=']

    # Shuffle the letters for it to be randomly placed 
    random.shuffle(upper_cases)
    random.shuffle(lower_cases)

    #New array which will contain the password
    new_password = []

    # The result of this variable will be used as an index. This index will decide which special sign is chosen
    random_special_sign = randint(0,8) 

    # 4 iterations for the password to have 20 characters. 
    for i in range(4):

        # Chose 1 number between 0 and 25 because there are 26 characters in the array letters 
        random_number_upper_cases = randint(0,25)
        random_number_lower_cases = randint(0,25)

        # New_password is added the letter corresponding to the number chosen randomly by random_number
        new_password.append(upper_cases[random_number_upper_cases])
        new_password.append(str(randint(0,9))) 
        new_password.append(lower_cases[random_number_lower_cases])
  
 
        random_number_for_special_sign = randint(0,1)

        # If random_number_for_special_sign == 1, a number is added to the array new_password
        if random_number_for_special_sign == 1 : 

            # Convert the int to a str for the array not to be composed of str and int but only str
            new_password.append(str(randint(0,9)))
        
        # Else if random_number_for_special_sign == 0, a special sign is added to the array new_password
        else : 
            # The index used to chose the special sign was given by the array special_sign
            new_password.append(special_signs[random_special_sign])
        
        # For having a more secure password, if random_number_for_special_sign == 1, we still add a special sign
        new_password.append(special_signs[random_special_sign])

        # Both are re declared in the loop, otherwise the random number will always be the same 
        random_special_sign = randint(0,8)
        random_number_for_special_signs = randint(0,1)


    # Join the elements of the array with empty quotes for each element to be following each other and not being surrounded by : ''
    str_new_password = "".join(new_password)

    return(str_new_password)


my_password = get_a_password()
print("Your password is",my_password)


