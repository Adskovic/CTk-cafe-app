import tkinter as tk
from tkinter import ttk
from typing import Optional, Tuple, Union
import customtkinter as ctk
from PIL import ImageTk, Image, ImageDraw
from images import *
from settings import *
import time
from random import randint

class UserProfilePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)
        global inner_frame

        # General
        self.start_pos = start_pos 
        self.end_pos = end_pos 
        self.width = abs(start_pos-end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Favourite logic
        self.is_favourite = False

        # Layout
        self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=0.91)


        class InnerFrame(ctk.CTkFrame):
            def __init__(self, parent, **kwargs):
                super().__init__(parent, **kwargs)

        inner_frame = InnerFrame(self)
        inner_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        fav_label = ctk.CTkLabel(self, text="Favorites:", font=("Helvetica", 20))
        fav_label.pack(pady=10)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.05
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=0.91)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.05
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=0.91)
            self.after(10, self.animate_backwards)
            button_cart.configure(state="normal")
        else:
            self.in_start_pos = True

    def adding_to_favourite(self, position_name):
        global fav_position_frame
        fav_position_frame = ctk.CTkFrame(inner_frame, fg_color=(TONNYS_PINK, FOLLOW_BROWN))
        fav_position_frame.pack(fill="x",padx=20, pady=10)
        fav_position_label = ctk.CTkLabel(fav_position_frame, text=position_name, compound="left")
        fav_position_frame.pack(fill="x",padx=20, pady=10)
        fav_position_label.pack(side="left", expand=True, fill="both", padx=10)
     


class CartAnimatedPanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)
        global cart_frame, bottom_buttons_frame, order_button, cart_label, empty_label

        # General
        self.start_pos = start_pos 
        self.end_pos = end_pos 
        self.width = abs(start_pos-end_pos)

        # Animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # Layout
        self.place(relx=self.start_pos, rely=0, relwidth=self.width, relheight=0.91)

        cart_frame = ctk.CTkFrame(self, fg_color=(LIGHT_GREY, HOVER_DARK_GREY), corner_radius=0)
        bottom_buttons_frame = ctk.CTkFrame(self, fg_color=(LIGHT_GREY, HOVER_DARK_GREY), corner_radius=0)
        order_button = ctk.CTkButton(bottom_buttons_frame, text="Order", width=190, state="disabled", fg_color=PERSIAN_RED, hover_color=INDIAN_RED, command=self.ordering)
        order_button.pack(padx=5)
        cart_label = ctk.CTkLabel(cart_frame, text="Your cart:", font=("Helvetica", 15))
        cart_label.pack()
            
        if len(cart_frame.winfo_children()) <= 1:
            empty_label = ctk.CTkLabel(cart_frame, text="No positions added")
            empty_label.pack()  
        
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
            bottom_buttons_frame.pack(side="bottom", fill="x")
            cart_frame.pack(expand=True, fill="both")
        else:
            self.animate_backwards()


    def animate_forward(self):
        if self.pos < self.end_pos:
            self.pos += 0.05
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=0.91)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos > self.start_pos:
            self.pos -= 0.05
            self.place(relx=self.pos, rely=0, relwidth=self.width, relheight=0.91)
            self.after(10, self.animate_backwards)
            button_cart.configure(state="normal")
        else:
            self.in_start_pos = True


    def adding_position(self, position, image):
        global position_frame
        position_frame = ctk.CTkFrame(cart_frame)
        position_frame.pack(fill="x",padx=20, pady=10)
        image_label = ctk.CTkLabel(position_frame, text=None, image=image, compound="left", width=10, height=10)
        image_label.pack(side="left", expand=True, fill="both", padx=10)
        position_label = ctk.CTkLabel(position_frame, text=position, compound="left")
        position_label.pack(side="left", expand=True, fill="both", padx=10)
        segemented_button = ctk.CTkSegmentedButton(position_frame, values=["S", "M", "L"], selected_color=DARK_GREY, selected_hover_color=HOVER_DARK_GREY)
        segemented_button.pack(padx=10, pady=5)
        spinbox = tk.Spinbox(position_frame, values=[1,2,3,5], width=6)
        spinbox.pack(padx=5, pady=5,side="left")
        delete_position_button = ctk.CTkButton(position_frame, text=None, command=position_frame.destroy, width=20, height=20, image=image_trash, fg_color=PERSIAN_RED, hover_color=INDIAN_RED)
        delete_position_button.pack(padx=5, pady=5, side="right")
        order_button.configure(state="normal")
        if len(cart_frame.winfo_children()) > 1:
            empty_label.pack_forget()

        
    def ordering(self):

        # Deleting all positions
        cart_label.pack_forget()
        children = cart_frame.winfo_children()
        for child in children:
            if isinstance(child, ctk.CTkFrame):
                child.destroy()  

        # Creating order info
        order_label = ctk.CTkLabel(cart_frame, text="Thank you for ordering!")
        order_label.place(relx=0.5, rely=0.4, anchor="center")
        time.sleep(1)
        order_label2 = ctk.CTkLabel(cart_frame, text="Your order is being prepared.")
        order_label2.place(relx=0.5, rely=0.5, anchor="center")
        order_number = randint(000, 999)
        order_number_label = ctk.CTkLabel(cart_frame, text=f"Order number: {order_number}", font=("Helvetica", 20))
        order_number_label.place(relx=0.5, rely=0.6, anchor="center")
        order_button.configure(state="disabled")

        
class Starting_screen(ctk.CTkFrame):
    def __init__(self, parent, import_func):
        super().__init__(parent, fg_color=(WHITE, BLACK))
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.import_func = import_func
        self.HomeFrame()

        start_button = ctk.CTkButton(self, 
                                     text="GET STARTED", 
                                     corner_radius=50, 
                                     height=35, 
                                     command=self.start, 
                                     fg_color=PATTERN_BROWN, 
                                     text_color=WHITE, 
                                     hover_color=(HOVER_GREY,HOVER_START_BROWN)
                                     )
        start_button.place(relx=0.5, rely=0.85, anchor="center")

    def HomeFrame(self):
        self.home_frame = ctk.CTkLabel(self, width=100, height=100, image=home_frame_image, text=None).place(relx=0, rely=0, relwidth=1, relheight=1)


    def start(self):
        self.import_func()


class BottomMenu(ctk.CTkFrame):
    def __init__(self, parent, import_fun, import_fun2, import_fun3):
        super().__init__(parent, fg_color=(WHITE,DARK_GREY))
        self.place(relx=0, rely=1, relwidth=1, relheight=0.09, anchor="sw")
        self.import_fun = import_fun
        self.import_fun2 = import_fun2
        self.import_fun3 = import_fun3
        global button_cart
        

        button_home = ctk.CTkButton(self, text=None, fg_color="transparent", image=image_home, command=self.home, hover_color=(HOVER_GREY,HOVER_DARK_GREY), corner_radius=25, width=50)
        button_home.pack(side="left",padx=10, expand=True)

        button_cart = ctk.CTkButton(self, text="", fg_color="transparent", image=image_cart, hover_color=(HOVER_GREY,HOVER_DARK_GREY), corner_radius=25,width=50, command=self.animate_cart)
        button_cart.pack(side="left",padx=10, expand=True)

        button_profile = ctk.CTkButton(self, text=None, fg_color="transparent", image=image_profile, hover_color=(HOVER_GREY,HOVER_DARK_GREY), corner_radius=25, width=50, command=self.animate_profile)
        button_profile.pack(side="left",padx=10, expand=True)

    def home(self):
        self.import_fun()

    def animate_cart(self):
        self.import_fun2()

    def animate_profile(self):
        self.import_fun3()
        




class Header_frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=(WHITE, BLACK))
        self.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.4, anchor="center")

        # widgets
        
        label = ctk.CTkLabel(self, text="Find your perfect coffee here...", text_color=(BLACK, WHITE), font=("MADE Gentle", 22), bg_color="transparent")
        label.place(relx=0, rely=-0.1, relwidth=0.9, relheight=1)

        entry = ctk.CTkEntry(self, placeholder_text="Browse your favourite drink", placeholder_text_color="#5c5c5c", fg_color=(LIGHT_GREY,DARK_GREY), border_width=0, bg_color="transparent")
        entry.place(relx=0.2, rely=0.75, relwidth= 0.7)

        search_btn = ctk.CTkButton(self, text=None, image=search_image, fg_color=(LIGHT_GREY,DARK_GREY), background_corner_colors=None, bg_color="transparent", hover_color=(HOVER_GREY, HOVER_DARK_GREY))
        search_btn.place(relx=0.105, rely=0.75, relwidth= 0.08,)

        # Changing appearance mode dark/light

        appearance_mode = ctk.StringVar(value="dark")

        def toggle_appearance():
            if appearance_mode.get() == "dark":
                appearance_mode.set("light")
                ctk.set_appearance_mode("light")
            else:
                appearance_mode.set("dark")
                ctk.set_appearance_mode("dark")

        mode_switch_btn = ctk.CTkButton(self,
                                        bg_color="transparent", 
                                        text_color="black",
                                        text=None,
                                        fg_color="transparent",
                                        hover=None,
                                        image=image_sun,
                                        command= lambda: toggle_appearance()
                                        )
        mode_switch_btn.place(relx= 0.91, 
                              rely=0.27, 
                              relwidth=0.1, 
                              relheight=0.1, 
                              anchor="nw"
                              )

class Frame1(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(parent,
                         fg_color=(WHITE, BLACK), 
                         segmented_button_selected_color=(LIGHT_GREY,BLACK), 
                         segmented_button_selected_hover_color=(LIGHT_GREY,BLACK), 
                         text_color=(BLACK, WHITE)
                         )
        self.place(relx=0.5, rely=0.6, relwidth=1, relheight=0.62, anchor="center", )


        #tabs
        self.add("Coffee")
        self.add("Tea")
        self.add("Meal")

        #widgets
        CoffeePanel(self.tab("Coffee"))
        TeaPanel(self.tab("Tea"))
        MealPanel(self.tab("Meal"))


class CoffeePanel(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=(WHITE, BLACK))
        self.pack(expand=True, fill="both")
        
    # Grid setup

        self.columnconfigure((0,1), weight=6, uniform="a")
        self.rowconfigure((0,1), weight=6, uniform="a")

    # Buttons

        self.create_buttons(0, 0, "Espresso        $2", image_espresso)
        self.create_buttons(0, 1, "Cappucino        $4", image_cappuccino)
        self.create_buttons(1, 0, "Latte        $5", image_latte)
        self.create_buttons(1, 1, "Americano        $3", image_americano)

    
    def create_buttons(self, row, column, text, image):
        global button_var
        frame = ctk.CTkFrame(self, 
                             fg_color=(LIGHT_GREY, DARK_GREY), 
                             corner_radius=10
                             )
        frame.grid(row=row, 
                   column=column, 
                   sticky="SE",
                   ipadx=10,
                   ipady=30,
                   padx=10,
                   pady=10
                   )
        button = ctk.CTkButton(frame, text=text,
                               fg_color=(LIGHT_GREY, DARK_GREY),
                                 text_color=(BLACK,WHITE), 
                                 hover_color=(HOVER_GREY, HOVER_DARK_GREY), 
                                 corner_radius=25, 
                                 image=image, 
                                 compound="top",
                                 command=lambda: add_to_cart(self, position=text, image=image)
                                 )
        button.pack(expand=True, 
                    fill="both", 
                    padx=17.5, 
                    pady=17.5
                    )
        
        button_var = ctk.StringVar(self, text)

        # Adding to favourite

        fav_state = ctk.StringVar(value="False")
        

        def fav_click():
            nonlocal fav_button
            if fav_state.get() == "False":
                fav_button.configure(image=image_heart_red)
                fav_state.set("True")
                add_to_fav(self, position_name=button_var.get())
            else:
                fav_button.configure(image=image_heart1)
                fav_state.set("False")
                remove_from_fav()
                

        fav_button = ctk.CTkButton(frame, 
                                         text=None, 
                                         fg_color=(LIGHT_GREY, DARK_GREY),
                                         bg_color="transparent", 
                                         background_corner_colors=None, 
                                         image=image_heart1, 
                                         width=1,
                                         height=1,
                                         hover=None,
                                         command=fav_click
                                         )
        fav_button.place(relx=0.87, 
                          rely=0.02, 
                          anchor="nw"
                          )
        
        # Adding favourite to User Panel

        def add_to_fav(self, position_name):
            UserProfilePanel.adding_to_favourite(self, text)

        def remove_from_fav():
            if inner_frame is not None:
                fav_position_frame.destroy()

        # Adding positions to Cart

        def add_to_cart(self, position, image):
            CartAnimatedPanel.adding_position(self, position=position, image=image)

       

class TeaPanel(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=(WHITE, BLACK))
        self.pack(expand=True, fill="both")
        
    # Grid setup

        self.columnconfigure((0,1), weight=6, uniform="a")
        self.rowconfigure((0,1), weight=6, uniform="a")

    # Buttons

        self.create_buttons(0, 0, "Black        $2", image_black)
        self.create_buttons(0, 1, "Green        $3", image_green)
        self.create_buttons(1, 0, "Forest fruits        $4", image_forest)
        self.create_buttons(1, 1, "Yellow        $4", image_yellow)

    
    def create_buttons(self, row, column, text, image):
        global button_var
        frame = ctk.CTkFrame(self, 
                             fg_color=(LIGHT_GREY, DARK_GREY), 
                             corner_radius=10
                             )
        frame.grid(row=row, 
                   column=column, 
                   sticky="SE",
                   ipadx=10,
                   ipady=30,
                   padx=10,
                   pady=10
                   )
        button = ctk.CTkButton(frame, text=text,
                               fg_color=(LIGHT_GREY, DARK_GREY),
                                 text_color=(BLACK,WHITE), 
                                 hover_color=(HOVER_GREY, HOVER_DARK_GREY), 
                                 corner_radius=25, 
                                 image=image, 
                                 compound="top",
                                 command=lambda: add_to_cart(self, position=text, image=image)
                                 )
        button.pack(expand=True, 
                    fill="both", 
                    padx=17.5, 
                    pady=17.5
                    )
        
        button_var = ctk.StringVar(self, text)

        # Adding to favourite

        fav_state = ctk.StringVar(value="False")
        

        def fav_click():
            nonlocal fav_button
            if fav_state.get() == "False":
                fav_button.configure(image=image_heart_red)
                fav_state.set("True")
                add_to_fav(self, position_name=button_var.get())
            else:
                fav_button.configure(image=image_heart1)
                fav_state.set("False")
                remove_from_fav()
                

        fav_button = ctk.CTkButton(frame, 
                                         text=None, 
                                         fg_color=(LIGHT_GREY, DARK_GREY),
                                         bg_color="transparent", 
                                         background_corner_colors=None, 
                                         image=image_heart1, 
                                         width=1,
                                         height=1,
                                         hover=None,
                                         command=fav_click
                                         )
        fav_button.place(relx=0.87, 
                          rely=0.02, 
                          anchor="nw"
                          )
        
        # Adding favourite to User Panel

        def add_to_fav(self, position_name):
            UserProfilePanel.adding_to_favourite(self, text)

        def remove_from_fav():
            if inner_frame is not None:
                fav_position_frame.destroy()

        # Adding positions to Cart

        def add_to_cart(self, position, image):
            CartAnimatedPanel.adding_position(self, position=position, image=image)


class MealPanel(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=(WHITE, BLACK))
        self.pack(expand=True, fill="both")
        
    # Grid setup

        self.columnconfigure((0,1), weight=6, uniform="a")
        self.rowconfigure((0,1), weight=6, uniform="a")

    # Buttons

        self.create_buttons(0, 0, "Donut        $2", image_donut)
        self.create_buttons(0, 1, "Sandwich        $5", image_sandwich)
        self.create_buttons(1, 0, "Cake        $4", image_cake)
        self.create_buttons(1, 1, "Croissant        $3", image_croissant)

    
    def create_buttons(self, row, column, text, image):
        global button_var
        frame = ctk.CTkFrame(self, 
                             fg_color=(LIGHT_GREY, DARK_GREY), 
                             corner_radius=10
                             )
        frame.grid(row=row, 
                   column=column, 
                   sticky="SE",
                   ipadx=10,
                   ipady=30,
                   padx=10,
                   pady=10
                   )
        button = ctk.CTkButton(frame, text=text,
                               fg_color=(LIGHT_GREY, DARK_GREY),
                                 text_color=(BLACK,WHITE), 
                                 hover_color=(HOVER_GREY, HOVER_DARK_GREY), 
                                 corner_radius=25, 
                                 image=image, 
                                 compound="top",
                                 command=lambda: add_to_cart(self, position=text, image=image)
                                 )
        button.pack(expand=True, 
                    fill="both", 
                    padx=17.5, 
                    pady=17.5
                    )
        
        button_var = ctk.StringVar(self, text)

        # Adding to favourite

        fav_state = ctk.StringVar(value="False")
        

        def fav_click():
            nonlocal fav_button
            if fav_state.get() == "False":
                fav_button.configure(image=image_heart_red)
                fav_state.set("True")
                add_to_fav(self, position_name=button_var.get())
            else:
                fav_button.configure(image=image_heart1)
                fav_state.set("False")
                remove_from_fav()
                

        fav_button = ctk.CTkButton(frame, 
                                         text=None, 
                                         fg_color=(LIGHT_GREY, DARK_GREY),
                                         bg_color="transparent", 
                                         background_corner_colors=None, 
                                         image=image_heart1, 
                                         width=1,
                                         height=1,
                                         hover=None,
                                         command=fav_click
                                         )
        fav_button.place(relx=0.87, 
                          rely=0.02, 
                          anchor="nw"
                          )
        
        # Adding favourite to User Panel

        def add_to_fav(self, position_name):
            UserProfilePanel.adding_to_favourite(self, text)

        def remove_from_fav():
            if inner_frame is not None:
                fav_position_frame.destroy()

        # Adding positions to Cart

        def add_to_cart(self, position, image):
            CartAnimatedPanel.adding_position(self, position=position, image=image)





if __name__ == "__main__":
    print("Opening from frame file")
    import main
