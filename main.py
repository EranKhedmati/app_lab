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
    # creat windows
    # -------------------------------
    chegali_window = Window(app, title="chegali", width=400, height=530)
    chegali_window.hide()

    #-------------------------------------
    #chegali_window
    #-------------------------------------
    # def chegali_detail():
    about_chegali = Box(chegali_window , border=True , width="fill" , height=200)
    chegali_text = Text(about_chegali, text="چگالی یا دانستیه یک ماده که به آن جرم\n حجمی یا جرم ویژه می گویند \n، یا به عبارتی دیگر جرم یک سانتی متر \nمکعب از یک جسم را می گویند  \nو آن را با نماد p نشان می دهند و از رابطه ی p=m/vبه \nدست می آید  که p چگالی ، mحجم و v حجم جسم است")
    chegali_cal = Box(chegali_window , width="fill" , height=260 , border=True)
    footer_box = Box(chegali_window ,width="fill" , height=70 , border=True) 

    blood_window = Window(app, title="blood", width=400, height=530)
    blood_window.hide()

    meghias_window = Window(app, title="meghias", width=400, height=530)
    meghias_window.hide()

    takhalkhol_window = Window(app, title="takhalkhol", width=400, height=530)
    takhalkhol_window.hide()

    test_window = Window(app, title="test", width=400, height=530)
    test_window.hide()

    Warning_window = Window(app, title="warning", width=400, height=530)
    Warning_window.hide()

    # -------------------------------
    # Open buttons
    # --------------------------------
    def open_window(name: str):
        if name == "chegali":
            chegali_window.show()
            app.hide()
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


def about():
    about_window = Window(app, title="درباره", width=400, height=540)

# ------------------------------------
# App
# ------------------------------------
app = App('app_lab')

title = Text(app, text="آزمایشگاه علوم تجربی دهم", size=25, font="B Titr")

about_menubar = MenuBar(app, toplevel=["منو"], options=[[["درباره", about]]])

# menu_title()
board()
app.display()
