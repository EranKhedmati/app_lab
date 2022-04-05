# -----------------------------------
# Imports
# -----------------------------------
from pydoc import text
from turtle import width
from guizero import App, PushButton, Box, Picture,TextBox, Text, Window, MenuBar,ButtonGroup

from library import chegali
from library import khoon
# -----------------------------------
# CONSTANS
# -----------------------------------
MAIN_BOX = int(0)
GOROOH_KHOONEI_BOX = int(1)
CHEGHALEY_BOX = int(2)
TAKHALKHOL_BOX = int(3)
MEGHYAS_BOX = int(4)
ALAMAT_BOX = int(5)
AZMOON_BOX = int(6)

# -----------------------------------
# Variables
# -----------------------------------
def showBox(id:int):
    boxMain.hide()
    if id==CHEGHALEY_BOX:
        boxChegalei.show()
    elif id==GOROOH_KHOONEI_BOX:
        boxKhoon.show()

# -----------------------------------
# Functions
# -----------------------------------
# Chegali Section
def updateBtnGChegali():
    txtChegli.enable()
    txtJerm.enable()
    txtHajm.enable()
    if btnGChegali.value=="چگالی":
        txtChegli.disable()
    elif btnGChegali.value=="جرم":
        txtJerm.disable()
    elif btnGChegali.value=="حجم":
        txtHajm.disable()

def chegaliParametersChange():
    try:
        p = float(txtChegli.value)
    except ValueError:
        txtChegli.value=""

    try:
        v = float(txtHajm.value)
    except ValueError:
        txtHajm.value=""

    try:
        m = float(txtJerm.value)
    except ValueError:
        txtJerm.value=""

    if txtChegli.enabled==False and m>-1 and v>-1:
        p=int(-1)
        txtChegli.value=chegali(p,m,v)
    elif txtHajm.enabled==False and m>-1 and p>-1:
        v=int(-1)
        txtHajm.value=chegali(p,m,v)
    elif txtJerm.enabled==False and p>-1 and v>-1:
        m=int(-1)
        txtJerm.value=chegali(p,m,v)
def khoonParametrChange():
    try:
        anti_a = int(txtAntia,value)
    except ValueError:
        txtAntia.value=""
    try:
        anti_b = int(txtAntib)
    except ValueError:
        txtAntib.value=""
    try:
        anti_d = int(txtAntid)
    except ValueError:
        txtAntid.value=""
    resultKhoon.value = khoon(anti_a, anti_b, anti_d)
# ---------------------------------------------


def about():
    about_window = Window(app, title="درباره", width=400, height=540)


# ------------------------------------
# App
# ------------------------------------
app = App('app_lab', width=500, height=500)
title = Text(app, text="آزمایشگاه علوم تجربی دهم", size=25, font="B Titr")

# Main Box
boxMain = Box(app, layout="grid")
for x in range(2):
    for y in range(3):
        button = PushButton(boxMain, grid=[x, y], padx=60, pady=60)

chegali_botton = PushButton(
    boxMain, command=showBox, image="icons/chegali.png", grid=[0, 0], args=[CHEGHALEY_BOX])

blood_button = PushButton(
    boxMain, command=showBox, image="icons/blood.png", grid=[1, 0], args=[GOROOH_KHOONEI_BOX])

meghias_button = PushButton(
    boxMain, command=showBox, image="icons/meghias.png", grid=[0, 1], args=[MEGHYAS_BOX])

takhalkhol_button = PushButton(
    boxMain, command=showBox, image="icons/takhalkhol.png", grid=[1, 1], args=[TAKHALKHOL_BOX])

test_button = PushButton(boxMain, command=showBox,
                         image="icons/test.png", grid=[0, 2], args=[AZMOON_BOX])

warning_button = PushButton(
    boxMain, command=showBox, image='icons/warning.png', grid=[1, 2], args=[ALAMAT_BOX])


# Box Chegalei
boxChegalei = Box(app,visible=False,width='fill')
btnGChegali = ButtonGroup(app, options=["چگالی", "حجم", "جرم"], selected="چگالی",
    command=updateBtnGChegali)
Text(boxChegalei,"لطفا دو مقدار را وارد کنید")
Text(boxChegalei,"چگالی")
txtChegli=TextBox(boxChegalei,width='fill',command=chegaliParametersChange,enabled=False)
Text(boxChegalei,"حجم")
txtHajm=TextBox(boxChegalei,width='fill',command=chegaliParametersChange)
Text(boxChegalei,"جرم")
txtJerm=TextBox(boxChegalei,width='fill',command=chegaliParametersChange)

# Box Khoon
boxKhoon = Box(app , visible=False , width='fill')
Text(boxKhoon , "لطفا مشخص کنید اگر خون با ماده رسوب کرده است عدد ۱ و در غیر اینصورت عدد -۱ را وارد کنید")
Text(boxKhoon , "آنتی A")
txtAntia=TextBox(boxKhoon , width='fill' , command=khoonParametrChange)
Text(boxKhoon , 'آنتی B')
txtAntib = TextBox(boxKhoon , width='fill' , command=khoonParametrChange)
Text(boxKhoon , 'آنتی D')
txtAntid = TextBox(boxKhoon , width='fill' , command=khoonParametrChange)
resultKhoon = Text(boxKhoon)

# Menu bar
about_menubar = MenuBar(app, toplevel=["منو"], options=[[["درباره", about]]])

# menu_title()
app.display()
