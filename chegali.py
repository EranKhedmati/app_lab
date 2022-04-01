#-----------------------------------
#imports
#-----------------------------------
from guizero import App , Box , Text
import os
#-----------------------------------
#variables
#-----------------------------------

#-----------------------------------
#App
#-----------------------------------
chegali_app = App("chegali" , width=400 , height=540)
#-----------------------------------
#boxs
#-----------------------------------
about_box = Box(app , border=True , width="fill" , height=200) #بردر برای اینکه باکس رو فعلا تشخیض بدیم

chegali_text = Text(about_box, text="چگالی یا دانستیه یک ماده که به آن جرم حجمی یا جرم ویژه می گویند ، یا به عبارتی دیگر جرم یک سانتی متر مکعب از یک جسم را می گویند و آن را با نماد p نشان می دهند و از رابطه ی p=m/v به دست می آید  که p چگالی ، mحجم و v حجم جسم است")

calculation_box = Box(app , width="fill" , height=260 , border=True

    )
footer_box = Box(app ,width="fill" , height=80 , border=True) 
footer_text = Text(footer_box , text="محاسبه ی چگالی" ,size=18 , align="right" )

app.display()