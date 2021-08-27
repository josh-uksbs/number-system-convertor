def is_valid_number(convertor, system_from, number):
    if len(number) < 1:
        return False
    
    if system_from == 0: # is binary
        for n in number: # loop for each char
            if str(n) != "0": # if char isn't 0
                if str(n) != "1": # and it isn't 1 either
                    return False
                
        return True
            
    elif system_from == 1: # is decimal
        return number.isnumeric()
    
    elif system_from == 2: # is hexadecimal
        for n in number: # loop for every char
            if n not in convertor.hex_map.keys(): # if it's not in the list of valid hex keys
                return False

        return True
    
    else: # this shouldn't happen but just in case
        return False
