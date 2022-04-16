# -----------------------------------
# Imports
# -----------------------------------
from secrets import choice
from time import time
from guizero import App, PushButton, Box, Picture, TextBox, Text, Window, MenuBar, ButtonGroup, Slider

from library import chegali
from library import khoon
from library import takhmin_masafat
from library import cheshme

import os

from random import shuffle
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

LIST_AZMOON = ["برق" , "قابل انفجار" , "قابل اشتعال" , "خورنده" , "مواد زیستی" ,"اکسید اسید" , "پسماند" ,"سمی" , "زیان آور"]
AZMOON_BARGH=int(0)
AZMOON_ENFEJAR=int(1)
AZMOON_ESHTEAL=int(2)
AZMOON_KHORANDE=int(3)
AZMOON_ZISTI=int(4)
AZMOON_ACID=int(5)
AZMOON_PASMAND=int(6)
AZMOON_SAMMI=int(7)
AZMOON_ZEYAN=int(8)
# -----------------------------------
# Variables
# -----------------------------------

# -----------------------------------
# Functions
# -----------------------------------

# Main Section
def showBox(id: int):
    boxMain.hide()
    boxChegalei.hide()
    boxKhoon.hide()
    boxTakhal.hide()
    boxWarning.hide()
    boxMeghias.hide()
    boxGame.hide()

    btnBackMain.show()
    
    if id== MAIN_BOX:
        boxMain.show()
        btnBackMain.hide()
    elif id == CHEGHALEY_BOX:
        boxChegalei.show()
    elif id == GOROOH_KHOONEI_BOX:
        boxKhoon.show()
    elif id == MEGHYAS_BOX:
        boxMeghias.show()
    elif id == TAKHALKHOL_BOX:
        boxTakhal.show()
    elif id == ALAMAT_BOX:
        boxWarning.show()
    elif id == AZMOON_BOX:
        setupGame()
        boxGame.show()


# Chegali Section

def updateBtnGChegali():
    txtChegli.enable()
    txtJerm.enable()
    txtHajm.enable()
    if btnGChegali.value == "چگالی":
        txtChegli.disable()
    elif btnGChegali.value == "جرم":
        txtJerm.disable()
    elif btnGChegali.value == "حجم":
        txtHajm.disable()


def chegaliParametersChange():
    try:
        p = float(txtChegli.value)
    except ValueError:
        txtChegli.value = ""

    try:
        v = float(txtHajm.value)
    except ValueError:
        txtHajm.value = ""

    try:
        m = float(txtJerm.value)
    except ValueError:
        txtJerm.value = ""

    if txtChegli.enabled == False and m > -1 and v > -1:
        p = int(-1)
        txtChegli.value = chegali(p, m, v)
    elif txtHajm.enabled == False and m > -1 and p > -1:
        v = int(-1)
        txtHajm.value = chegali(p, m, v)
    elif txtJerm.enabled == False and p > -1 and v > -1:
        m = int(-1)
        txtJerm.value = chegali(p, m, v)

# Groop Khooni section
def khoonParametrChange():
    try:
        anti_a = int(sldAntia.value)
    except ValueError:
        anti_a = ""
    try:
        anti_b = int(sldAntib.value)
    except ValueError:
        anti_b = ""
    try:
        anti_d = int(sldAntid.value)
    except ValueError:
        anti_d = ""
    resultKhoon.value = khoon(anti_a, anti_b, anti_d)
    if sldAntia.value == 0:
        resultKhoon.value = ""
    elif sldAntib.value == 0:
        resultKhoon.value = ""
    elif sldAntid.value == 0:
        resultKhoon.value = ""


# Meghias section
def updateBtnMeghias():
    txtMeghias.enable()
    txtFmap.enable()
    txtFground.enable()
    if btnMeghias.value == "مقیاس":
        txtMeghias.disable()
    elif btnMeghias.value == "فاصله دو نقطه روی نقشه":
        txtFmap.disable()
    elif btnMeghias.value == "فاصله دو نقطه روی زمین":
        txtFground.disable()


def meghiasParametersChange():
    try:
        meghias = float(txtMeghias.value)
    except ValueError:
        txtMeghias.value = ""

    try:
        f_map = float(txtFmap.value)
    except ValueError:
        txtFmap.value = ""

    try:
        f_ground = float(txtFground.value)
    except ValueError:
        txtFground.value = ""

    if txtMeghias.enabled == False and f_map > -1 and f_ground > -1:
        meghias = int(-1)
        txtMeghias.value = takhmin_masafat(meghias, f_map, f_ground)
    elif txtFmap.enabled == False and meghias > -1 and f_ground > -1:
        f_map = int(-1)
        txtFmap.value = takhmin_masafat(meghias, f_map, f_ground)
    elif txtFground.enabled == False and f_map > -1 and f_ground > -1:
        f_ground = int(-1)
        txtFground.value = takhmin_masafat(meghias, f_map, f_ground)
# Takhalkhol section

def updateBtnTakhal():
    txtTakhal.enable()
    txtVsang.enable()
    txtVkol.enable()
    if btnTakhal.value == "تخلخل":
        txtTakhal.disable()
    elif btnTakhal.value == "حجم فضای خالی سنگ یا رسوب":
        txtVsang.disable()
    elif btnTakhal.value == "حجم کل فضای کل سنگ یا رسوب":
        txtVkol.disable()

def takhalParametersChange():
    try:
        takhalkhol = float(txtTakhal.value)
    except ValueError:
        txtTakhal.value = ""

    try:
        v_sang = float(txtVsang.value)
    except ValueError:
        txtVsang.value = ""

    try:
        v_kol = float(txtVkol.value)
    except ValueError:
        txtVkol.value = ""

    if txtTakhal.enabled == False and v_sang > -1 and v_kol > -1:
        takhalkhol = int(-1)
        txtTakhal.value = cheshme(takhalkhol, v_sang, v_kol)
    elif txtVsang.enabled == False and takhalkhol > -1 and v_kol > -1:
        v_sang = int(-1)
        txtVsang.value = cheshme(takhalkhol, v_sang, v_kol)
    elif txtVkol.enabled == False and v_sang > -1 and takhalkhol > -1:
        v_kol = int(-1)
        txtVkol.value = cheshme(takhalkhol, v_sang, v_kol)
# Warning section
def swapPicture(i:int):
    idx=icons.index(picture.image)

    if i>0:
        idx=idx+1
        if idx>len(icons)-1:
            idx=0
    else:
        idx=idx-1
    
    picture.image=icons[idx]
        
#Game Section
def setupGame():
    txtSoal.value = choice(LIST_AZMOON)
    timer.value=30
    btnReset.hide()
    txtNatije.hide()
    txtEmteyaz.value=0
    buttonBox.show()
    txtSoal.show()

def checkGame(idx: int):
    if idx==LIST_AZMOON.index(txtSoal.value):
        txtEmteyaz.value=int(txtEmteyaz.value)+1
    else:
        txtEmteyaz.value=int(txtEmteyaz.value)-1

    txtSoal.value = choice(LIST_AZMOON)

def reduce_time():
    timer.value = int(timer.value) - 1
    # is it game over?
    if int(timer.value) < 0:
        timer.value=0
        txtNatije.value = "زمان آزمون به پایان رسید امتیاز شما = " + txtEmteyaz.value
        txtNatije.show()
        btnReset.show()
        # hide the game
        buttonBox.hide()
        txtSoal.hide()

#Menu bar

def about():
    infoText="سرگروه: عرفان خدمتی" + "\n" + "عضو گروه: صالح بازماندگان" + "\n" + "کد اثر: 534785"
    app.info("سازنده", infoText)


# ------------------------------------
# App
# ------------------------------------
app = App(title="icons/app.jpg", width=500, height=500)
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
boxChegalei = Box(app, visible=False, width='fill')
btnGChegali = ButtonGroup(boxChegalei, options=["چگالی", "حجم", "جرم"], selected="چگالی",
                          command=updateBtnGChegali)
Text(boxChegalei, "لطفا دو مقدار را وارد کنید")
Text(boxChegalei, "چگالی بر حسب رو")
txtChegli = TextBox(boxChegalei, width='fill',
                    command=chegaliParametersChange, enabled=False)
Text(boxChegalei, "حجم بر حسب مترمکعب")
txtHajm = TextBox(boxChegalei, width='fill', command=chegaliParametersChange)
Text(boxChegalei, "جرم بر حسب کیلوگرم")
txtJerm = TextBox(boxChegalei, width='fill', command=chegaliParametersChange)


# Box Khoon

boxKhoon = Box(app, visible=False, width="fill")
Text(boxKhoon, "لطفا در صورت رسوب خون عدد ۱ و در غیر این صورت عدد -۱ \n را وارد کنید")
Text(boxKhoon, "آنتی A")
sldAntia = Slider(boxKhoon, start=-1, end=1, command=khoonParametrChange)
Text(boxKhoon, "آنتی B")
sldAntib = Slider(boxKhoon, start=-1, end=1, command=khoonParametrChange)
Text(boxKhoon, "آنتی D")
sldAntid = Slider(boxKhoon, start=-1, end=1, command=khoonParametrChange)
resultKhoon = Text(boxKhoon, size=20)


# Box meghias
boxMeghias = Box(app, visible=False, width='fill')
btnMeghias = ButtonGroup(boxMeghias,
                         options=["مقیاس", "فاصله دو نقطه روی نقشه", "فاصله دو نقطه روی زمین"], command=updateBtnMeghias, selected="مقیاس")
Text(boxMeghias, "مقیاس")
txtMeghias = TextBox(boxMeghias, width='fill',
                     command=meghiasParametersChange, enabled=False)
Text(boxMeghias, "فاصله روی نشه")
txtFmap = TextBox(boxMeghias, width='fill', command=meghiasParametersChange)
Text(boxMeghias, "فاصله روی زمین")
txtFground = TextBox(boxMeghias, width='fill', command=meghiasParametersChange)


# Box takhalkhol
boxTakhal = Box(app, visible=False, width='fill')
btnTakhal = ButtonGroup(boxTakhal, options=[
                        "تخلخل", "حجم فضای خالی سنگ یا رسوب", "حجم کل فضای کل سنگ یا رسوب"], selected="تخلخل", command=updateBtnTakhal)
Text(boxTakhal, "لطفا دو مقدار را وارد کنید")
Text(boxTakhal, 'تخلخل')
txtTakhal = TextBox(boxTakhal, width='fill',
                    command=takhalParametersChange, enabled=False)
Text(boxTakhal, 'حجم فضای خلی سنگ یا رسوب ')
txtVsang = TextBox(boxTakhal, width='fill', command=takhalParametersChange)
Text(boxTakhal, 'حجم کل فضای سنگ یا رسوب')
txtVkol = TextBox(boxTakhal, width='fill', command=takhalParametersChange)


#Box Warning
boxWarning = Box(app , visible=False , width="fill")

iconDir = "res/wraningicons"
icons = [os.path.join(iconDir,f)for f in os.listdir(iconDir)]

picture = Picture(boxWarning)
picture.image=icons[0]

btnRight = PushButton(boxWarning ,command=swapPicture,args=[-1], text='قبل→' , align="right" ,height=10)
btnLeft = PushButton(boxWarning , command=swapPicture,args=[+1],text="←بعد" , align="left" ,height=10)

btnBackMain = PushButton(app ,command=showBox,args=[MAIN_BOX],
width='fill' ,text="برگشت به صفحه اصلی →" , align="bottom",visible=False)

#Box Game
boxGame = Box(app , visible=False , width="400",border="2")


top_box = Box(boxGame, align="top", width="fill")
Text(top_box, align="left", text="امتیاز ")
txtEmteyaz = Text(top_box, text="4", align="left")
timer = Text(top_box, text="30", align="right")
Text(top_box, text="زمان", align="right")

txtSoal = Text(boxGame,size=14,color="#0099ff")

gameDir = "res/gamepicture"
gameimg = [os.path.join(gameDir,f) for f in os.listdir(gameDir)]

buttonBox = Box(boxGame , layout="grid")
buttonGame = []


btnBargh = PushButton(buttonBox , image="res/gamepicture/bargh.png" ,command=checkGame, args=[AZMOON_BARGH] , grid=[0,0]) #برق
btnEnfejar = PushButton(buttonBox , image="res/gamepicture/ghabel enfegar.png" ,command=checkGame, args=[AZMOON_ENFEJAR],grid=[1,0])#قابل انفجار
btnEshteal = PushButton(buttonBox , image="res/gamepicture/ghabel eshteghal.png" ,command=checkGame, args=[AZMOON_ESHTEAL] , grid=[2,0])#قابل اشتعال
btnKhorande = PushButton(buttonBox , image="res/gamepicture/khorande.png" ,command=checkGame, args=[AZMOON_KHORANDE] , grid=[0,1])#خورنده
btnZisti = PushButton(buttonBox , image="res/gamepicture/mavad zisti.png" ,command=checkGame, args=[AZMOON_ZISTI] , grid=[1,1])#مواد زیستی
btnOccid = PushButton(buttonBox , image="res/gamepicture/occid asid.png" ,command=checkGame, args=[AZMOON_ACID], grid=[2,1])#اکسید اسید
btnPasmand = PushButton(buttonBox , image="res/gamepicture/pasmand.png" ,command=checkGame, args=[AZMOON_PASMAND] ,grid=[0,2])#پسماند
btnSammi = PushButton(buttonBox , image="res/gamepicture/sammi.png" ,command=checkGame, args=[AZMOON_SAMMI] , grid=[1,2])
btnZian = PushButton(buttonBox , image="res/gamepicture/zian avar.png" ,command=checkGame, args=[AZMOON_ZEYAN] , grid=[2,2])#زیان آور

txtNatije = Text(boxGame,size=14,color="red",visible=False)
btnReset=PushButton(boxGame,command=setupGame,text="از اول⟳",visible=False)

# Menu bar
about_menubar = MenuBar(app, toplevel=["منو"], options=[[["سازنده", about]]])
app.repeat(1000, reduce_time)
app.display()