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

# Chegali method


def chegali(p: float, m: float, v: float):
    """
        متد محاسبه چگالی
    Args:
        p (float, optional): [چگالی]. Defaults to -1.
        m (float, optional): [جرم]. Defaults to -1.
        v (float, optional): [حجم]. Defaults to -1.

    Returns:
        [type]: [مقدار محاسبه شده را با توجه به ورودی بر می گرداند]
    """
    if p == -1:
        return m/v
    elif m == -1:
        return p*v
    else:
        return m/p

# khoon method


def khoon(antiA, antiB, antiD):
    """
     متد تایین گروه خونی
    Args:
        antiA (str, optional): [آنتی A]. Defaults to 0.
        antiB (str, optional): [آنتی B]. Defaults to 0.
        antiD (str, optional): [آنتی D]. Defaults to 0.
    Returns:
        [type]: [گروه خونی را با توجه به ورودی برمی گرداند]
    """
    if antiA == -1 and antiB == -1 and antiD == 1:
        print('O+')
    elif antiA == -1 and antiB == 1 and antiD == -1:
        print('B-')
    elif antiA == -1 and antiB == 1 and antiD == 1:
        print('B+')
    elif antiA == 1 and antiB == 1 and antiD == 1:
        print('AB+')
    elif antiA == 1 and antiB == 1 and antiD == -1:
        print('AB-')
    elif antiA == 1 and antiB == -1 and antiD == -1:
        print('A-')
    else:
        print('A+')

# takhmin_masafat method


def takhmin_masafat(meghias: float, f_map: float, f_ground: float):
    """
    متد محاسبه مقیاس

    Args:
        meghias (floatl,optional): [مقیاس] Defaults to -1 .
        f_map (float,optional): [فاصله دو نقطه روی نقشه] Defaults to -1 .
        f_ground (float,optional): [فاصله دو نقطه روی زمین] Defaults to -1 .
    Returns:
        [Type] : [مقیاس را با توجه به ورودی برمیگرداند]
    """
    if meghias == -1:
        return f_map/f_ground
    elif f_map == -1:
        return meghias * f_ground
    else:
        return f_map/meghias

# takhalkhol method


def cheshme(takhalkhol: float, v_sang: float, v_kol: float):
    """
    متد محاسبه تخلخل

    args:
        takhal (float,optional): [تخلخل] Defaults to -1.
        v_sang (float,optional): [حجم فضای خالی سنگ یا رسوب] Defaults to -1.
        v_kol (float,optional):  [حجم کل فضای سنگ یا رسوب] Defaults to -1.
    Returns : 
    [type] : [مقدار تخلخل را با توجه به ورودی برمی گرداند]

    """
    if takhalkhol == -1:
        return (v_sang/v_kol)*100
    elif v_sang == -1:
        return (takhalkhol*v_sang)/100
    else:
        return (v_sang/takhalkhol)*100

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

    # -------------------------------
    # Picturs of buttons
    # -------------------------------
    chegali_botton = PushButton(
        buttons, command=open_chegali, image="chegali.png", grid=[0, 0])

    blood_button = PushButton(
        buttons, command=open_blood, image="blood.png", grid=[1, 0])

    meghias_button = PushButton(
        buttons, command=open_maghias, image="meghias.png", grid=[0, 1])

    takhalkhol_button = PushButton(
        buttons, command=open_takhalkhol, image="takhalkhol.png", grid=[1, 1])

    test_button = PushButton(buttons, command=open_test,
                             image="test.png", grid=[0, 2])

    warning_button = PushButton(
        buttons, command=open_warning, image='warning.png', grid=[1, 2])


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
