# -----------------------------------
# Imports
# -----------------------------------
from guizero import App, PushButton, Box, Picture, Text, Window
import os
# -----------------------------------
# Variables
# -----------------------------------

# -----------------------------------
# Functions
# -----------------------------------

# -----------------------------------
# methods
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
    # Open buttond
    # -------------------------------
    def open_chegali():
        chegali_window.show()

    def open_blood():
        blood_window.show()

    def open_maghias():
        meghias_window.show()

    def open_takhalkhol():
        takhalkhol_window.show()

    def open_test():
        test_window.show()

    def open_warning():
        Warning_window.show()

    def open_window(name:str):
        if name == "chegali":
            chegali_window.show()

    # -------------------------------
    # Picturs of buttons
    # -------------------------------
    chegali_botton = PushButton(
        buttons, command=open_window, image="icons\\chegali.png", grid=[0, 0],args=["chegali"])

    blood_button = PushButton(
        buttons, command=open_blood, image="icons\\blood.png", grid=[1, 0])

    meghias_button = PushButton(
        buttons, command=open_maghias, image="icons\\meghias.png", grid=[0, 1])

    takhalkhol_button = PushButton(
        buttons, command=open_takhalkhol, image="icons\\takhalkhol.png", grid=[1, 1])

    test_button = PushButton(buttons, command=open_test,
                             image="icons\\test.png", grid=[0, 2])

    warning_button = PushButton(
        buttons, command=open_warning, image='icons\\warning.png', grid=[1, 2])


def menu_title():
    menubar = Box(app, width="fill", height=70)
    menu = PushButton(menubar, text="منو", align="right")
    title = Text(menubar, text="آزمایشگاه علوم تجربی دهم",
                 size=25, font="B Titr")


# ------------------------------------
# App
# ------------------------------------
app = App('app_lab')

menu_title()
board()
app.display()
