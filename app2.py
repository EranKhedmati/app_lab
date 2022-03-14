#----------------------------------------
#Import
#----------------------------------------

from guizero import App , PushButton , Box , Picture , Text , Window
import os

#---------------------------------------
#function
#---------------------------------------


def board():  # ساخت کلید برای متود ها
        buttons = Box(app , layout='grid')
        for x in range(2): #ساخت دکمه برای متود ها
                for y in range(3):
                  button = PushButton(buttons , grid=[x,y] , padx=60 , pady=60)

        #----------------------------------------
        #creat windows
        #-----------------------------------------

        chegali_window = Window(app , title='chegali' , width=400 , height=530)
        chegali_window.hide()

        blood_window = Window(app , title='blood' , width=400 , height=540)
        blood_window.hide()
        
        meghias_window = Window(app , title='meghias' , width=400 , height=540)
        meghias_window.hide()

        takhalkhol_window = Window(app , title='takhalkhol' , width=400 , height=540)
        takhalkhol_window.hide()

        test_window = Window(app , title='test' , width=400 , height=540)
        test_window.hide()

        Warning_window = Window(app , title='warning' , width=400 , height=540)
        Warning_window.hide()

        #-----------------------------------------
        #open window
        #-----------------------------------------
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
                
        #-----------------------------------------
        #Pictures of button
        #-----------------------------------------
        chegali = PushButton(
                buttons ,
                command=open_chegali ,
                image='chegali.png' ,
                grid = [0,0]
                )

        blood = PushButton(
                buttons ,
                command=open_blood,
                image='blood.png' ,
                grid = [1,0]
                )

        meghias = PushButton(buttons ,
                command=open_maghias ,
                image='meghias.png' ,
                grid=[0,1]
                )

        takhalkhol = PushButton(
                buttons ,
                command=open_takhalkhol ,
                image='takhalkhol.png' ,
                grid = [1,1]
                )

        test = PushButton(
                buttons ,
                command=open_test ,
                image='test.png' ,
                grid=[0,2]
                )

        warning = PushButton(
                buttons ,
                command=open_warning ,
                image='warning.png' ,
                grid=[1,2]
                )
        


def menu_title(): #منو و تایتل'
        menubar = Box(app , width='fill' , height=70)
        menu = PushButton(menubar ,text='منو' , align='right' , )
        title = Text(menubar , text='آزمایشگاه علوم تجربی دهم' , size=25 , font= 'B Titr')



#----------------------------------------
#App
#----------------------------------------

app = App('app_lab' , width=400 , height=530)



menu_title()
board()
app.display()