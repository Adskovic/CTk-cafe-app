import customtkinter as ctk
from PIL import ImageTk, Image



# Button images

image_cappuccino = ctk.CTkImage(light_image=Image.open("images/cappuccino.png"), dark_image=Image.open("images/cappuccino.png"), size=(80,80))
image_cappuccino_small = ctk.CTkImage(light_image=Image.open("images/cappuccino.png"), dark_image=Image.open("images/cappuccino.png"), size=(40,40))
image_latte = ctk.CTkImage(light_image=Image.open("images/latte.png"), dark_image=Image.open("images/latte.png"), size=(80,80))
image_espresso = ctk.CTkImage(light_image=Image.open("images/espresso.png"), dark_image=Image.open("images/espresso.png"), size=(80,80))
image_americano = ctk.CTkImage(light_image=Image.open("images/americano.png"), dark_image=Image.open("images/americano.png"), size=(80,80))

image_black = ctk.CTkImage(light_image=Image.open("images/black_tea.png"), dark_image=Image.open("images/black_tea.png"), size=(80,80))
image_green = ctk.CTkImage(light_image=Image.open("images/green_tea.png"), dark_image=Image.open("images/green_tea.png"), size=(80,80))
image_yellow = ctk.CTkImage(light_image=Image.open("images/yellow_tea.png"), dark_image=Image.open("images/yellow_tea.png"), size=(80,80))
image_forest = ctk.CTkImage(light_image=Image.open("images/forest_fruits.png"), dark_image=Image.open("images/forest_fruits.png"), size=(80,80))

image_donut = ctk.CTkImage(light_image=Image.open("images/donut.png"), dark_image=Image.open("images/donut.png"), size=(80,80))
image_croissant = ctk.CTkImage(light_image=Image.open("images/croissant.png"), dark_image=Image.open("images/croissant.png"), size=(80,80))
image_cake = ctk.CTkImage(light_image=Image.open("images/piece-of-cake.png"), dark_image=Image.open("images/piece-of-cake.png"), size=(80,80))
image_sandwich = ctk.CTkImage(light_image=Image.open("images/sandwich.png"), dark_image=Image.open("images/sandwich.png"), size=(80,80))

# Top frame images

search_image = ctk.CTkImage(light_image=Image.open("images/search_icon.png"), dark_image=Image.open("images/search_icon.png"), size=(15, 15))
# image_beans_background = ctk.CTkImage(light_image=Image.open("images/beans.png"), dark_image=Image.open("images/beans.png"), size=(500,400))
# header_background = ctk.CTkImage(light_image=Image.open("images/header_black.png"), dark_image=Image.open("images/header_white.png"), size=(600,400))

# Home screen image

home_frame_image= ctk.CTkImage(light_image=Image.open("images/home_background_white.png"), dark_image=Image.open("images/home_background_black.png"), size=(400,600))

# Bottom menu images

image_profile= ctk.CTkImage(light_image=Image.open("images/user_black.png"), dark_image=Image.open("images/user_white.png"), size=(18,18))
image_home= ctk.CTkImage(light_image=Image.open("images/house_black.png"), dark_image=Image.open("images/house_white.png"), size=(18,18))
image_cart= ctk.CTkImage(light_image=Image.open("images/basket_black.png"), dark_image=Image.open("images/basket_white.png"), size=(18,18))

# Other images

image_sun= ctk.CTkImage(light_image=Image.open("images/light-on-96.png"), dark_image=Image.open("images/light-off-96.png"), size=(23,23))
image_heart1= ctk.CTkImage(light_image=Image.open("images/heart_black.png"), dark_image=Image.open("images/heart_white.png"), size=(10,10))
image_heart_red= ctk.CTkImage(light_image=Image.open("images/heart_fill_red.png"), dark_image=Image.open("images/heart_fill_red.png"), size=(10,10))
image_trash= ctk.CTkImage(light_image=Image.open("images/trash_black.png"), dark_image=Image.open("images/trash_white.png"), size=(18,18))