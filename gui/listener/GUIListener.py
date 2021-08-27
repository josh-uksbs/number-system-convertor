# imports
import tkinter as tk
from util import NumberUtils
from time import sleep

class GUIListener:
    def __init__(self, main_instance): # constructor - called when class is instantiated
        self.convertor = main_instance.convertor # assign convertor locally in class from main


    def on_combobox_update(self, combobox, is_from, information, system_values):
        split = information["text"].split(" to ") # split the information value into an array of 2
        
        if is_from: # check which number system combobox was changed
            split[0] = f"Converting from {system_values[combobox.current()]}" # replace first part of split
        else:
            split[1] = str(system_values[combobox.current()]) # replace second part of split

        information.config(text=f"{split[0]} to {split[1]}") # set information text to combined split


    def on_input_click(self, inp):
        if inp.get() == "Enter a number to convert...":
            inp.delete(0, tk.END) # clear the input box


    def on_input_update(self, inp, x, system_from, system_to, output):
        key = x.char # character entered

        if len(key) == 0: # if it's not a valid character
            return

        if ord(key) > 96 and ord(key) < 103: # if is a - f
            inp.delete(len(inp.get()) - 1, tk.END) # delete the character
            new_char = chr(ord(key) - 32) # get the uppercase version
            inp.insert(tk.INSERT, new_char) # insert
            key = new_char # reassign the key with uppercase
        
        if ord(key) > 70 or ord(key) < 65: # if not A - F
            if ord(key) > 57 or ord(key) < 48: # if not 0 - 9
                inp.delete(len(inp.get()) - 1, tk.END) # delete character
                return
        
        to_convert = inp.get() # get contents of input box
        is_valid = NumberUtils.is_valid_number(self.convertor, system_from.current(), to_convert) # return boolean for number and system

        replace = "Invalid number for conversion." # default string if invalid

        if is_valid:
            converted = self.convertor.convert(system_from.current(), system_to.current(), inp.get()) # convert number as it's valid
            replace = f"{to_convert} = {converted}" # replace if valid
        
        output.config(text=replace) # set output text

