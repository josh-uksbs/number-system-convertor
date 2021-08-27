class Convertor:
    def __init__(self, main_instance): # constructor - called when class is instantiated
        self.main_instance = main_instance
        self.hex_map = { # map of hex keys and decimal values 
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "A": 10,
            "B": 11,
            "C": 12,
            "D": 13,
            "E": 14,
            "F": 15
        }
    

    def convert(self, system_from, system_to, number):
        if system_from == 0: # if from binary
            if system_to == 1: # if to decimal
                return self.binary_to_decimal(number)

            elif system_to == 2: # if to hex
                return self.binary_to_hexadecimal(number)

            else: # fallback
                return None

        elif system_from == 1: # if from decimal
            if system_to == 0: # if to binary
                return self.decimal_to_binary(number)

            elif system_to == 2: # if to hex
                return self.decimal_to_hexadecimal(number)

            else: # fallback
                return None

        elif system_from == 2: # if from hex
            if system_to == 0: # if to binary
                return self.hexadecimal_to_binary(number)

            elif system_to == 1: # if to decimal
                return self.hexadecimal_to_decimal(number)

            else: # fallback
                return None

        else: # fallback
            return None


    def binary_to_decimal(self, number):
        numbers = list(str(number))[::-1] # convert binary string into list, and invert
        to_add = []

        for i in range(len(numbers)): # loop for amount of numbers in list
            _number = int(numbers[i]) # get item at position and cast to integer
            if _number == 1:
                to_add.append(2 ** i) # append power of index to list

        return sum(to_add) # return sum of list


    def binary_to_hexadecimal(self, number):
        numbers = list(str(number)) # convert binary string into list

        while len(numbers) % 4 != 0: # while the length of the list isn't divisible by 4
            numbers.insert(0, "0") # add a 0 at start of list

        binary = ''.join([str(number) for number in numbers]) # change back into string
        nibble_sectors = [binary[i:i+4] for i in range(0, len(binary), 4)] # split into nibbles
    
        decimal_values = []
        for nibble in nibble_sectors:
            decimal_values.append(self.binary_to_decimal(nibble)) # append decimal conversion of binary to list

        to_return = ""
        for decimal in decimal_values:
            for key, value in self.hex_map.items(): # for each key & value in hex_map
                if decimal == value: # if decimal equals the value in map
                    to_return += key # concatenate the key into to_return string

        return to_return


    def decimal_to_binary(self, number):
        _number = int(number) # create new reference of parameter
        binary = []

        while _number != 0:
            binary.append(str(_number % 2)) # cast modulo result of number / 2
            _number = _number // 2 # reassign number floor division by 2

        binary = binary[::-1] # reassign inverted binary

        while len(binary) % 4 != 0:
            binary.insert(0, "0")

        return ''.join([str(bit) for bit in binary]) # return binary list as string


    def decimal_to_hexadecimal(self, number):
        return self.binary_to_hexadecimal(self.decimal_to_binary(number)) # convert decimal to binary, then convert binary to hex and return


    def hexadecimal_to_binary(self, number):
        numbers = list(str(number)) # form list from string
        to_return = ""

        for number in numbers:
            to_return += self.decimal_to_binary(self.hex_map[number]) # convert decimal to binary with hex value lookup
            
        return to_return


    def hexadecimal_to_decimal(self, number):
        return self.binary_to_decimal(self.hexadecimal_to_binary(number)) # convert hex to binary, then convert binary to decimal and return

