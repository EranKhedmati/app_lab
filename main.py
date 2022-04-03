# -----------------------------------
# Imports
# -----------------------------------
from guizero import App, PushButton, Box, Picture, Text, Window, MenuBar
import os
# -----------------------------------
# Variables
# -----------------------------------

# -----------------------------------
# Functions
# -----------------------------------

# -----------------------------------
# creat board
# -----------------------------------


def board():
    buttons = Box(app, layout="grid")
    for x in range(2):
        for y in range(3):
            button = PushButton(buttons, grid=[x, y], padx=60, pady=60)

    # -------------------------------
    # Open buttons
    # --------------------------------
    def open_window(name: str):
        if name == "chegali":
            chegali_window()
        elif name == "blood":
            blood_window.show()
            app.hide()
        elif name == "meghias":
            meghias_window.show()
            app.hide()
        elif name == "takhalkhol":
            takhalkhol_window.show()
            app.hide()
        elif name == "test":
            test_window.show()
            app.hide()
        else:
            Warning_window.show()
            app.hide()
    # -------------------------------
    # Picturs of buttons
    # -------------------------------
    chegali_botton = PushButton(
        buttons, command=open_window, image="icons/chegali.png", grid=[0, 0], args=["chegali"])

    blood_button = PushButton(
        buttons, command=open_window, image="icons/blood.png", grid=[1, 0], args=["blood"])

    meghias_button = PushButton(
        buttons, command=open_window, image="icons/meghias.png", grid=[0, 1], args=["meghias"])

    takhalkhol_button = PushButton(
        buttons, command=open_window, image="icons/takhalkhol.png", grid=[1, 1], args=["takhalkhol"])

    test_button = PushButton(buttons, command=open_window,
                             image="icons/test.png", grid=[0, 2], args=["test"])

    warning_button = PushButton(
        buttons, command=open_window, image='icons/warning.png', grid=[1, 2], args=["warning"])

    def chegali_window():
        buttons.hide()
        title.hide()
        about_chegali = Box(app , border=True , width="fill" , height=150)
        chegali_text = Text(about_chegali , text="چگالی یا دانستیه یک ماده که به آن جرم\n حجمی یا جرم ویژه می گویند \n، یا به عبارتی دیگر جرم یک سانتی متر \nمکعب از یک جسم را می گویند  \nو آن را با نماد p نشان می دهند و از رابطه ی p=m/vبه \nدست می آید  که p چگالی ، mحجم و v حجم جسم است")
        chegali_cal_box = Box(app , width="fill" , height=250 , border=True) #cal = calculate
        footer_box = Box(app , width="fill" ,height=100 , border=True)

def about():
    about_window = Window(app, title="درباره", width=400, height=540)

# ------------------------------------
# App
# ------------------------------------
app = App('app_lab' , width=500 , height=500)
title = Text(app, text="آزمایشگاه علوم تجربی دهم", size=25, font="B Titr")

about_menubar = MenuBar(app, toplevel=["منو"], options=[[["درباره", about]]])

# menu_title()
board()
app.display()
