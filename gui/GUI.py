# imports
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkf

class GUI:
    def __init__(self, main_instance): # constructor - called when class is instantiated
        self.gui_listener = main_instance.gui_listener # assign listener locally in class from main
        self.gui = tk.Tk() # instantiate gui
        self.font = tkf.Font(family="Consolas", size=14) # declare font
        self.__build() # call local build method
        self.gui.mainloop()

    def __build(self):
        self.gui.minsize(450, 200)

        self.gui.title("Number System Convertor")
        self.gui.iconphoto(False, tk.PhotoImage(file="asset/icon.png"))

        system_values = ["Binary", "Decimal", "Hexadecimal"]
        self.__box_system_from(system_values)
        self.__box_system_to(system_values)

        self.__input_to_convert()
        self.__label_information()
        self.__label_output()


    def __box_system_from(self, system_values):
        self.system_from = ttk.Combobox(self.gui,
                                        values=system_values,
                                        state="readonly",
                                        width=30) # create combobox
        
        self.system_from.set("Select a system from...") # set value in box
        self.system_from.grid(row=0, column=0, padx=10, pady=10) # alter display

        # bind listener/event
        self.system_from.bind("<<ComboboxSelected>>", lambda x: self.gui_listener.on_combobox_update(self.system_from, True, self.information, system_values))


    def __box_system_to(self, system_values):
        self.system_to = ttk.Combobox(self.gui,
                                        values=system_values,
                                        state="readonly",
                                        width=30) # create combobox
        
        self.system_to.set("Select a system to...") # set value in box
        self.system_to.grid(row=0, column=1, padx=10, pady=10) # alter display

        # bind listener/event
        self.system_to.bind("<<ComboboxSelected>>", lambda x: self.gui_listener.on_combobox_update(self.system_to, False, self.information, system_values))


    def __input_to_convert(self):
        self.to_convert = tk.Entry(self.gui,
                                   width=35) # create input box
        
        self.to_convert.insert(tk.INSERT, "Enter a number to convert...") # set value in box
        self.to_convert.grid(row=1, column=0, columnspan=2, padx=10, pady=10) # alter display

        # bind listeners/events
        self.to_convert.bind("<Button-1>", lambda x: self.gui_listener.on_input_click(self.to_convert))
        self.to_convert.bind("<KeyRelease>", lambda x: self.gui_listener.on_input_update(self.to_convert, x, self.system_from, self.system_to, self.output))
        
    def __label_information(self):
        self.information = tk.Label(self.gui,
                                    font=self.font,
                                    text="Converting from - to -") # create label
        
        self.information.grid(row=2, column=0, columnspan=2, padx=10, pady=10) # alter display

    def __label_output(self):
        self.output = tk.Label(self.gui,
                               font=self.font,
                               text="- = -") # create label
        
        self.output.grid(row=3, column=0, columnspan=2, padx=10, pady=10) # alter display
        
