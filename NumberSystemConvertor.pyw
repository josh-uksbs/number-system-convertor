# imports
from convertor.Convertor import Convertor
from gui.GUI import GUI
from gui.listener.GUIListener import GUIListener

class NumberSystemConvertor:
    def __init__(self): # constructor - called when class is instantiated
        self.convertor = Convertor(self) # instantiate Convertor class
        
        self.gui_listener = GUIListener(self) # instantiate GUI listener
        self.gui = GUI(self) # instantiate GUI class


NumberSystemConvertor() # instantiate main class
