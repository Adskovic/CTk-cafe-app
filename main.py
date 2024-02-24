# Modules

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image, ImageDraw
from new_frame import *
from images import *
from settings import *


class App(ctk.CTk):
    def __init__(self):
        
        

        # window setup
        super().__init__(fg_color=(WHITE, BLACK)) 
        self.maxsize(WIDTH, HEIGHT)
        self.minsize(WIDTH, HEIGHT)
        


        # layout
        self.start = Starting_screen(self, self.get_started)
        

    def run(self):
        self.mainloop()
     
    def get_started(self):
        self.start.pack_forget()
        self.frame_main = Header_frame(self)
        self.frame = Frame1(self)
        self.menu = BottomMenu(self, self.home_screen, self.cart_panel, self.profile_panel)
        self.cart = CartAnimatedPanel(self, -1, 0)
        self.profile = UserProfilePanel(self, 1, 0)


    def home_screen(self):
        Starting_screen(self, self.get_started)
        self.frame_main.pack_forget
        self.frame.pack_forget
        self.menu.pack_forget
        # self.cart.pack_forget

    def cart_panel(self):
        self.cart.animate()

    def profile_panel(self):
        self.profile.animate()




app = App()
app.run()