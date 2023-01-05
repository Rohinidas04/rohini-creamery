# This demos using modes (aka screens).
from cmu_112_graphics import *
import random
import os
import time
from Icecreamscoop import *
from order import *
from button import *
##########################################
# Splash Screen Mode
##########################################
#this is the first screen that the user sees when they begin the game. it displays
#the name of the game and includes a key press event where the user is directed
#to the next screen if they press the left key
#this function loads the gif image on the home page
def loadAnimatedGif(path):
    # load first sprite outside of try/except to raise file-related exceptions
    spritePhotoImages = [ PhotoImage(file=path, format='gif -index 0') ]
    i = 1 
    while True:
        try:
            spritePhotoImages.append(PhotoImage(file=path,
                                                format=f'gif -index {i}'))
            i += 1
        except Exception as e:
            return spritePhotoImages




def splashScreenMode_redrawAll(app, canvas):
    #sets the font as arial 26 bold
    font = 'Arial 26 bold'
    #sets background color to light pink
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    # #title of game
    canvas.create_text(app.entryTextPosition, app.height/4, text= \
            'WELCOME TO ROHINI\'S CREAMERY!  WELCOME TO ROHINI\'S CREAMERY!  WELCOME TO ROHINI\'S CREAMERY!',
                       fill='firebrick3', font='Helvetica 26 bold ')
  

    #calls button function and draws button
    app.startButton.drawButton(canvas)

    
    canvas.create_text(300, app.height*3/4+75, text = 'Play', fill = 'white', font = 'Helvetic 20 bold')
    photoImage = app.spritePhotoImages[app.spriteCounter]
    
    #creates gif image (url below)
    canvas.create_image(300, 275, image=photoImage)


#checks for boundaries of done button
def doneSplashScreen(app, x, y, boxNum):
    return (250 <= x <= 350 and app.height*3/4+50 <= y <= app.height*3/4+100)

#animates gif 
def splashScreenMode_timerFired(app):
    app.spriteCounter = (1+app.spriteCounter)  % len(app.spritePhotoImages)

    if app.entryTextPosition<700:
        app.entryTextPosition+=3
    else:
        app.entryTextPosition = 0
   
#if left key is pressed, it shifts to next screen (directions page)
def splashScreenMode_mousePressed(app, event):
    if doneSplashScreen(app, event.x, event.y, 0):
        app.mode = 'startMode'

##########################################
# Game Mode
##########################################

#this is the directions image. it includes the directions on the goal of the game
def startMode_redrawAll(app, canvas):
    #sets font
    font = 'Arial 20 bold'
    #background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    #directions on how to play the game
    canvas.create_text(app.width/2, 20, text='INSTRUCTIONS',
                       fill='firebrick3', font='Helvetica 26 bold ')
    canvas.create_text(app.width/2, 70, text='You will be given icecream orders from customers',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 110, text = 'Use the slider and buttons to make the batter', font=font, fill='firebrick3')
    canvas.create_text(app.width/2, 150, text = 'Drag the icecream into the cup/cone', font=font, fill='black')
    canvas.create_text(app.width/2, 190, text = 'Drag the toppings into the cup/cone', font=font, fill='firebrick3')
    canvas.create_text(app.width/2, 230, text = 'At the end, you will be judged', font=font, fill='black')
    canvas.create_text(app.width/2, 270, text = 'Your goal is to serve all the customers before time runs out', font=font, fill='firebrick3')

    #tells user to press h to see directions and any other key to get started
    canvas.create_text(app.width/2, 310, text='Press h to see directions!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 350, text='Press any other key to get started',
                       font=font, fill='firebrick3')

    
    canvas.create_oval(550, 5, 590, 45, fill = 'firebrick3', outline = 'firebrick3')
    canvas.create_text(570, 25, text = '?', font = 'Helvetica 26 bold', fill = 'white')




#takes user back to direction page if h is pressed, else continues game
def startMode_keyPressed(app, event):
    #goes to helpmode if h is pressed
    if (event.key == 'h'):
        app.mode = 'helpMode'
    #goes to ordermode (next screen) if any other key is pressed
    else:
        app.mode = 'sittingMode'

#checks for boundaries of help button
def helpButtonClickedInBox(app, x, y, boxNum):
    return (550 <= x <= 590 and 5<= y <= 45)

def countdownTimer(app, x, y, boxNum):
    return (5 <= x <= 25 and 5<= y <= 25)

def startMode_mousePressed(app, event):
    # sets mode to erasing/not erasing based on box clicked
    if helpButtonClickedInBox(app, event.x, event.y, 0):
        app.help = True
        if app.help == True:
            app.mode = 'helpMode'



    
##########################################
# Help Mode
##########################################

#includes directions on how to play the game (help page)
def helpMode_redrawAll(app, canvas):
    #sets font 
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 150, text='This is the help screen!', 
                       font=font, fill='black')
    font = 'Arial 20 bold'
    #helps user by telling user directions on how to play game
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, 20, text='Directions',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 50, text='You will be given orders from customers',
                       font=font, fill='black')
    canvas.create_text(app.width/2, 80, text = 'You will make the icecream batter', font=font, fill='black')
    canvas.create_text(app.width/2, 110, text = 'You will scoop the icecream into cup/cone', font=font, fill='black')
    canvas.create_text(app.width/2, 140, text = 'You will add toppings', font=font, fill='black')
    canvas.create_text(app.width/2, 170, text = 'At the end, you will be judged and paid', font=font, fill='black')

    #tells user to press any other key to return to game
    canvas.create_text(app.width/2, 350, text='Press any key to return to the game!',
                       font=font, fill='black')

   
    
#takes user back to start screen if they press any key
def helpMode_keyPressed(app, event):
    app.mode = 'startMode'






def sittingMode_redrawAll(app, canvas):
    titleFont = 'Helvetica 26 bold'
    font = 'Helvetica 20'
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    #url: https://www.vecteezy.com/vector-art/8383986-abstract-seamless-pattern-of-orange-white-ceramic-floor-tiles-design-geometric-mosaic-texture-for-the-decoration-of-the-kitchen-room-vector-illustration
    canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.sittingSquare2))

    #shows customers moving across screen
    length = len(app.kitchenImageList)
    for i in range(length):
        canvas.create_image((i+1)*app.movingPersonWidth/(length + 1), 100, image=ImageTk.PhotoImage(app.kitchenImageList[i]))
        
        #creates individual timers for each customer
        if app.orders[i].getTotalSecond()>0:
            if app.orders[i].getTotalSecond() % 60 < 10:
                canvas.create_text((i+1)*app.movingPersonWidth/(length + 1), 150, text = f'{app.orders[i].getTotalSecond()//60}:0{app.orders[i].getTotalSecond()%60}', font = 'Helvetica 26 bold', fill = 'black')
            elif app.orders[i].getTotalSecond()%60 == 0:
                canvas.create_text((i+1)*app.movingPersonWidth/(length + 1), 150, text = f'{app.orders[i].getTotalSecond()//60}:{app.orders[i].getTotalSecond()%60}0', font = 'Helvetica 26 bold', fill = 'black')
            elif app.orders[i].getTotalSecond()%10 == 0 and app.orders[i].getTotalSecond()%60 != 0:
                canvas.create_text((i+1)*app.movingPersonWidth/(length + 1),150, text = f'{app.orders[i].getTotalSecond()//60}:{app.orders[i].getTotalSecond()%60}', font = 'Helvetica 26 bold', fill = 'black')
            else:
                canvas.create_text((i+1)*app.movingPersonWidth/(length + 1), 150, text = f'{app.orders[i].getTotalSecond()//60}:{app.orders[i].getTotalSecond()%60}', font = 'Helvetica 26 bold', fill = 'black')

       

    #tables
    #https://www.creativefabrica.com/product/brown-table-illustration-vector/
    canvas.create_image(app.width/3, (app.width*1)/2, image=ImageTk.PhotoImage(app.sittingTable2))
    canvas.create_image(app.width*2/3, (app.width*1)/2, image=ImageTk.PhotoImage(app.sittingTable2))
    canvas.create_image(app.width/2, (app.width*2)/3, image=ImageTk.PhotoImage(app.sittingTable2))
 

    #order here sign
    #https://stock.adobe.com/search?k=%22order+here+sign%22
    canvas.create_image(app.width*7.5/8, 55, image=ImageTk.PhotoImage(app.orderHere2))

    
    
    
    canvas.create_rectangle(7, app.height*0.82, (app.width/6 -app.width*0.03), app.height*0.92, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = 7
    a1 = (app.width/6 -app.width*0.03)
    b0 = app.height*0.82
    b1 = app.height*0.92
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Back', font = 'Helvetica 20 bold', fill = 'black')

    #creates timer at top of screen
    if app.totalSeconds>0:
        if app.totalSeconds % 60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')



#changes value of timer
def sittingMode_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'
    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'

    #changes position of customers
    if(app.movingPersonWidth < app.width):
        app.movingPersonWidth+=8


#boundaries for setting current order customer
def clickedOnImage(app,x,y,boxNum):
        return(app.imageX-20<=x<=app.imageX+20 and app.imageY-40<=y<=app.imageY+40)
       

def backSittingClickedInBox(app, x, y, boxNum):
    return (0 <= x <= (app.width/6 -app.width*0.03) and
            app.height*0.82 <= y <= app.height*0.92)


def sittingMode_mousePressed(app, event):
    
    if backSittingClickedInBox(app, event.x, event.y, 0):
        app.mode = 'startMode'
    
    imageWidth = app.width/(len(app.kitchenImageList)+1)
    for i in range(len(app.kitchenImageList)):
        app.imageX = imageWidth
        app.imageY = 100
        imageWidth=imageWidth+app.width/(len(app.kitchenImageList)+1)
        if app.foundImage!=True:
            if clickedOnImage(app, event.x, event.y, 0):
                app.foundImage = True
                #sets value of app.currentOrder
                app.currentOrder = app.orders[i]
                app.foundImageIndex = i
                app.currentOrder.setMilkHeight(app.height*5/6)
                app.mode = 'orderMode'
               


    
#orderMode
#includes randomly generated order for customer
def orderMode_redrawAll(app, canvas):
    titleFont = 'Helvetica 26 bold'
    font = 'Helvetica 20'
    #shows order on side of screen
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Here is an order from a customer',
                       font=titleFont, fill='black')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')
    canvas.create_image((app.width*2)/3, app.height*3.2/7, image=ImageTk.PhotoImage(app.orderBackground2))
    
    canvas.create_text((app.width/3)*2, app.height*0.30, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font=font, fill='black')
    canvas.create_text((app.width/3)*2, app.height*0.35, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=font, fill='black')
    canvas.create_text((app.width/3)*2, app.height*0.41, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=font, fill='black')
    canvas.create_text((app.width/3)*2, app.height*0.47, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=font, fill='black')
    canvas.create_text((app.width/3)*2, app.height*0.53, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=font, fill='black')
    #only includes toppings in higher levels (2-3)
    if app.level>1:
        canvas.create_text((app.width/3)*2, app.height*0.58, text = f'Toppings:',
                        font=font, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text((app.width/3)*2, app.height*0.64+ toppingsIncrement*15, text = f'{app.currentOrder.getToppings()[i]}',
                        font=font, fill='black')
            toppingsIncrement+=1
        canvas.create_text((app.width/3)*2, app.height*0.73, text = f'{app.currentOrder.getWhippedCream()}',
                        font=font, fill='black')
    
    
    #displays current customer image
    canvas.create_image(app.width/5, app.height/2, image=ImageTk.PhotoImage(app.finalImageList[app.foundImageIndex]))
 
    
    #takes you to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')

    #creates rectangle to represent Next button
    canvas.create_oval((app.width/3)*2 + app.width*0.03, app.height*0.8, (app.width/3)*2 + app.width/6, app.height*0.9, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    x0 = (app.width/3)*2 + app.width*0.03
    x1 = (app.width/3)*2 + app.width/6
    y0 = app.height*0.8
    y1 = app.height*0.9
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'Next', font = 'Helvetica 20 bold', fill = 'black')

    #back button
    canvas.create_oval((app.width/3)*1 + app.width/7+ app.width*0.03, app.height*0.8, (app.width/3)*1 + app.width/7+ app.width/6, app.height*0.9, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = (app.width/3)*1 + app.width/7+ app.width*0.03
    a1 = (app.width/3)*1 + app.width/7 + app.width/6
    b0 = app.height*0.8
    b1 = app.height*0.9
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Back', font = 'Helvetica 20 bold', fill = 'black')

    if app.totalSeconds>0:
        if app.totalSeconds % 60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')



def orderMode_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'

#returns true if user clicks on area of rectangle representing Next button
def nextOrderClickedInBox(app, x, y, boxNum):
    return ((app.width/3)*2 + app.width*0.03 <= x <= (app.width/3)*2 + app.width/6 and
            app.height*0.8 <= y <= app.height*0.9)

#boundaries for going back to previous screen
def backOrderClickedInBox(app, x, y, boxNum):
    return ((app.width/3)*1 + app.width/7 + app.width*0.03 <= x <= (app.width/3)*1 + app.width/7 + app.width/6 and
            app.height*0.8 <= y <= app.height*0.9)

#boundaries for going back directly to sitting page
def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)

    
#takes user to batterModePress screen if nextOrderClickedInBox is true
def orderMode_mousePressed(app, event):
    # sets mode to erasing/not erasing based on box clicked
    if nextOrderClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModePress'

    if backOrderClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'

    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'


#screen includes slider that moves side to side and stops when button is pressed
#when user presses button in middle green regions, outputs a smiley face
#when user presses button in side red regions, outputs sad face
#represents making of milk
def batterModePress_redrawAll(app, canvas):
    font = 'Arial 26 bold'

    #sets background
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us make the batter!',
                       font=font, fill='black')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    #goes back to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')
    #order at top right
    orderFont = 'Arial 11 bold'
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')
    if app.level>1:
        canvas.create_text(529, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(529, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1
        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')
    #displays time on side of screen
    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')

    #ui that represents milk machine
    canvas.create_rectangle(app.width/2-120, app.height/3-50, app.width/2+180 +(app.width/4 - app.width/6)-120, (app.height/3)+3.5*(app.height/10)-50, fill = 'light gray')
    d0 = app.width/2-120
    e0 = app.height/3-50
    d1 = app.width/2+180 +(app.width/4 - app.width/6)-120
    e1 = (app.height/3)+3.5*(app.height/10)-50
    canvas.create_text((d0+d1)/2, e0 + ((e1-e0)/3), text = 'CHOOSE', font = font, fill = 'black')               
    #chocolate flavor
    #rectangle representing chocolate button
    #pressing button changes color of milk to represent flavor
    canvas.create_oval(app.width/2-30,app.height/3 + 2.5*(app.height/10)-100, app.width/2-30 + (app.width/4 - app.width/6), (app.height/3)+3.5*(app.height/10)-100, fill = 'green', outline = 'green')
    x0 = app.width/2-30
    y0 = app.height/3 + 2.5*(app.height/10)-100
    x1 = app.width/2-30 + (app.width/4 - app.width/6)
    y1 = (app.height/3)+3.5*(app.height/10)-100
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'Click', font = 'Helvetica 15', fill = 'white')

    #vanilla flavor
    #rectangle representing vanilla button

    #gradient rectangle with green, yellow, and red
    canvas.create_image(app.width/2-30+((app.width/4 - app.width/6)/2), app.height/3 + 3*(app.height/10)-36,image=ImageTk.PhotoImage(app.gradient2))
    
    #rectangle that represents slider that moves from side to side of gradient
    # canvas.create_rectangle(app.width/2-120, (app.height/3)+3.5*(app.height/10)-50-22, app.width/2-120+10, (app.height/3)+3.5*(app.height/10)-50, fill = 'green' )
    canvas.create_rectangle(app.currentOrder.getSliderXOne(), (app.height/3)+3.5*(app.height/10)-50-22, app.currentOrder.getSliderXTwo(), (app.height/3)+3.5*(app.height/10)-50, fill = 'green' )
    f0 = app.width/2-120
    g0 = (app.height/3)+3.5*(app.height/10)-50-22
    f1 =  app.width/2-120+10
    g1 =(app.height/3)+3.5*(app.height/10)-50

    #rectangle that represents back button
    canvas.create_oval(app.width/5, app.height/2-0.5*app.height/10+200, app.width/5+(app.width/3-app.width/7), app.height/2+0.5*app.height/10+200, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = app.width/5
    b0 = app.height/2-0.5*app.height/10+200
    a1 = app.width/5+(app.width/3-app.width/7)
    b1 = app.height/2+0.5*app.height/10+200
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Back', font = 'Helvetica 20 bold', fill = 'black', activefill = '#54a8e8')

    #rectangle that represents next button
    canvas.create_oval(app.width/5+2*(app.width/3-app.width/7), app.height/2-0.5*app.height/10+200, app.width/5+3*(app.width/3-app.width/7), app.height/2+0.5*app.height/10+200, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    x0 = app.width/5+2*(app.width/3-app.width/7)
    y0 = app.height/2-0.5*app.height/10+200
    x1 = app.width/5+3*(app.width/3-app.width/7)
    y1 = app.height/2+0.5*app.height/10+200
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'Next', font = 'Helvetica 20 bold', fill = 'black', activefill = '#54a8e8')

    #image of cooking cup that milk is poured into
    canvas.create_image(app.width/2, app.height/2-0.5*app.height/10+140,image=ImageTk.PhotoImage(app.cookingCup2))

    #represents milk that will be filled up in cup
    canvas.create_rectangle(app.width/2-30+9,app.currentOrder.getBatterPressHeight(), app.width/2-30 + (app.width/4 - app.width/6)+1, app.height/2-0.5*app.height/10+187, fill = 'white')

    #calls function from order class to determine whether to output happy or sad face
    if app.currentOrder.getIsSliderMoving() == False:
        if app.currentOrder.getFace() == 'happy':
            canvas.create_image(app.width*5/6, app.height/2,image=ImageTk.PhotoImage(app.happyFace2))
        else:
            canvas.create_image(app.width*5/6, app.height/2,image=ImageTk.PhotoImage(app.sadFace2))


#timer fired for counting down time
def pressDoneClickedInBox(app, x, y, boxNum):
    return (app.width/5+2*(app.width/3-app.width/7) <= x <= app.width/5+3*(app.width/3-app.width/7) and
            app.height/2-0.5*app.height/10+200 <= y <= app.height/2+0.5*app.height/10+200)

#boundaries for going to previous screen
def pressBackClickedInBox(app, x, y, boxNum):
    return (app.width/5 <= x <= app.width/5+(app.width/3-app.width/7) and
           app.height/2-0.5*app.height/10+200 <= y <= app.height/2+0.5*app.height/10+200)


#boundaries for clicking on "click" button that stops and starts slider
def isClickedButton(app,x,y, boxNum):
    return(app.width/2-30<=x<=app.width/2-30 + (app.width/4 - app.width/6) and app.height/3 + 2.5*(app.height/10)-100<=y<=(app.height/3)+3.5*(app.height/10)-100)


def batterModePress_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'


    #based on location of slider on gradient, the slider moves faster or slower and changes direction
    #when the slider is closer to the middle green areas, its velocity increases
    #when the slider is further away from middle green areas, its velocity decreases
    #when the slider reaches either ends of the gradient, it begins moving in the other direction
    if app.currentOrder.getIsSliderMoving() == True:
        app.currentOrder.setBatterPressHeight(412)
        if app.currentOrder.getSliderXTwo() == app.width/2+180 +(app.width/4 - app.width/6)-120:
            app.currentOrder.setIsSliderNegative(True)
        if app.currentOrder.getSliderXOne() == app.width/2-120:
            app.currentOrder.setIsSliderNegative(False)
        if app.currentOrder.getIsSliderNegative() == False:
            if app.currentOrder.getSliderXTwo() <= (app.width/2-120 + app.width/2+180 +(app.width/4 - app.width/6)-120)/2:
                app.currentOrder.setSliderVelocityIncrement(0.1)
                app.currentOrder.setSliderXOneIncrement(app.currentOrder.getSliderVelocity())
                app.currentOrder.setSliderXTwoIncrement(app.currentOrder.getSliderVelocity())
            if app.currentOrder.getSliderXTwo() > (app.width/2-120 + app.width/2+180 +(app.width/4 - app.width/6)-120)/2:
                app.currentOrder.setSliderVelocityDecrement(0.1)
                app.currentOrder.setSliderXOneIncrement(app.currentOrder.getSliderVelocity())
                app.currentOrder.setSliderXTwoIncrement(app.currentOrder.getSliderVelocity())
            
        if app.currentOrder.getIsSliderNegative() == True:
            if app.currentOrder.getSliderXOne() >= (app.width/2-120 + app.width/2+180 +(app.width/4 - app.width/6)-120)/2:
                app.currentOrder.setSliderVelocityIncrement(0.1)
                app.currentOrder.setSliderXOneDecrement(app.currentOrder.getSliderVelocity())
                app.currentOrder.setSliderXTwoDecrement(app.currentOrder.getSliderVelocity())
            if app.currentOrder.getSliderXOne() < (app.width/2-120 + app.width/2+180 +(app.width/4 - app.width/6)-120)/2:
                app.currentOrder.setSliderVelocityDecrement(0.1)
                app.currentOrder.setSliderXOneDecrement(app.currentOrder.getSliderVelocity())
                app.currentOrder.setSliderXTwoDecrement(app.currentOrder.getSliderVelocity())

    if app.currentOrder.getIsSliderMoving() == False:
        app.currentOrder.setFace('')
        if app.currentOrder.getBatterPressHeight() >= app.height/2-0.5*app.height/10+173:
            app.currentOrder.decrementBatterPressHeight(0.5)
        if app.currentOrder.getSliderXOne()>=app.width/2-30:
            if app.currentOrder.getSliderXOne() <= app.width/2-30 + (app.width/4 - app.width/6):
                app.currentOrder.setFace('happy')
            
        else:
            app.currentOrder.setFace('sad')



#boundaries for going back to sitting screen
def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)

def batterModePress_mousePressed(app, event):
    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'

    #changes truth value whenever button is pressed
    if isClickedButton(app, event.x, event.y, 0):
        if app.currentOrder.getIsSliderMoving() == True:
            app.currentOrder.setIsSliderMoving(False)
        elif app.currentOrder.getIsSliderMoving() == False:
            app.currentOrder.setIsSliderMoving(True)
    if pressDoneClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModeMilk'
    
    if pressBackClickedInBox(app, event.x, event.y, 0):
        app.mode = 'orderMode'

#batter mode
#in this section, user adds cups of milk to cup
#milk doesnt go above the height of the cup
#user can remove or add milk with buttons
def batterModeMilk_redrawAll(app, canvas):
    #sets font
    
    font = 'Arial 26 bold'

    #sets background
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us make the batter!',
                       font=font, fill='black')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')
    
    #goes back to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')
    #order at top right
    orderFont = 'Arial 11 bold'
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')
    if app.level>1:
        canvas.create_text(529, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(529, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1
        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')


    canvas.create_image((app.width/2+(app.width*5)/6)/2, (app.height/4+(app.height*4.9)/7)/2, image=ImageTk.PhotoImage(app.milkJug2))
    canvas.create_rectangle(app.width/2+(app.width/15.5), app.height/4+app.height/14, (app.width*5)/6-(app.width/15.5), (app.height*5)/6, outline = 'light pink')
    canvas.create_text(app.width/4, app.height/3-20, text='Press for milk',
                       font=font, fill='black')

#creates rectangle representing button for adding milk
    canvas.create_oval(app.width/7, app.height/2 - 1.5*(app.height/10), app.width/3, (app.height/2)-0.5*(app.height/10), fill = 'light blue', activefill= '#54a8e8', outline = 'light blue')
    x0 = app.width/7
    y0 = app.height/2 - 1.5*(app.height/10)
    x1 = app.width/3
    y1 = (app.height/2)-0.5*(app.height/10)
    canvas.create_text(4*(x0 + x1)/7,(y0+y1)/2, text = 'Milk', font = 'Helvetica 20 bold', fill = 'black')
    #adding milk image
    canvas.create_image(3.5*(x0 + x1)/8, (y0+y1)/2, image=ImageTk.PhotoImage(app.milkImage2))


    #rectangle for remove button
    canvas.create_oval(app.width/7, app.height/2, app.width/3, (app.height/2)+(app.height/10), fill = 'light blue', activefill= '#54a8e8', outline = 'light blue')
    x0 = app.width/7
    y0 = app.height/2
    x1 = app.width/3
    y1 = (app.height/2)+(app.height/10)
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'Remove', font = 'Helvetica 20 bold', fill = 'black')
  
    
    #white rectangle that represents milk; rectangle gets larger as button is pressed
    #milkclicked parameter changes height of rectangle to represent additional cups of milk
    # canvas.create_rectangle(app.width/2+(app.width/15.5), (app.height*5)/6 - (app.currentOrdersses())*((((app.height*5)/6) - (app.height/4+app.height/14))/3), (app.width*5)/6-(app.width/15.5), (app.height*5)/6, fill = app.currentOrder.getColor())
    canvas.create_rectangle(app.width/2+(app.width/15.5), app.currentOrder.getMilkHeight(), (app.width*5)/6-(app.width/15.5), (app.height*5)/6, fill = app.currentOrder.getColor())

    #done button rectangle
    canvas.create_oval(app.width/7, (app.height/2)+1.5*(app.height/10), app.width/3, (app.height/2)+2.5*(app.height/10), fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = app.width/7
    b0 = (app.height/2)+1.5*(app.height/10)
    a1 = app.width/3
    b1 = (app.height/2)+2.5*(app.height/10)
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Next', font = 'Helvetica 20 bold', fill = 'black')

    #back button
    canvas.create_oval(app.width/7, (app.height/2)+3*(app.height/10), app.width/3, (app.height/2)+4*(app.height/10), fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    c0 = app.width/7
    d0 = (app.height/2)+3*(app.height/10)
    c1 = app.width/3
    d1 = (app.height/2)+4*(app.height/10)
    canvas.create_text((c0 + c1)/2,(d0+d1)/2, text = 'Back', font = 'Helvetica 20 bold', fill = 'black')



    #timer that counts down from 3 minutes and outputs time
    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')

#timer fired for counting down time

def batterModeMilk_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'

    #creates effect of milk being poured into cup
    if app.currentOrder.getMilkHeight() >= (app.height*5)/6 - (app.currentOrder.getActualMilkPresses())*((((app.height*5)/6) - (app.height/4+app.height/14))/3):
        app.currentOrder.setMilkHeight(app.currentOrder.getMilkHeight()-3)
    if app.currentOrder.getMilkHeight() <= (app.height*5)/6 - (app.currentOrder.getActualMilkPresses())*((((app.height*5)/6) - (app.height/4+app.height/14))/3):
        app.currentOrder.setMilkHeight(app.currentOrder.getMilkHeight()+3)


  

def moreMilkClickedInBox(app, x, y, boxNum):
    return (app.width/7 <= x <= app.width/3 and
            (app.height/2)-1.5*(app.height/10) <= y <= (app.height/2)-0.5*(app.height/10))

def removeMilkClickedInBox(app,x,y,boxNum):
    return (app.width/7 <= x <= app.width/3 and
            app.height/2 <= y <= (app.height/2)+(app.height/10))

def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)

#checks for pressing area of done button for milk
def milkDoneClickedInBox(app, x, y, boxNum):
    return (app.width/7 <= x <= app.width/3 and
            (app.height/2)+1.5*(app.height/10) <= y <= (app.height/2)+2.5*(app.height/10))

def milkBackClickedInBox(app, x, y, boxNum):
    return (app.width/7 <= x <= app.width/3 and
            (app.height/2)+3*(app.height/10) <= y <= (app.height/2)+4*(app.height/10))


#mouse pressed for batter mode page 
def batterModeMilk_mousePressed(app, event):
    #changes app.milkClicked when button is pressed to increase amount of milk
    if moreMilkClickedInBox(app, event.x, event.y, 0):
     #creates effect of milk being poured into cup
        if app.currentOrder.getActualMilkPresses() < 3:
            app.currentOrder.incrementMilkClicked()
            app.mode = 'batterModeMilk'

    if removeMilkClickedInBox(app,event.x, event.y, 0):
        if app.currentOrder.getActualMilkPresses() > 0:
            app.currentOrder.decrementMilkClicked()
            app.mode = 'batterModeMilk'


    #goes to next screen when done button is pressed
    if milkDoneClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModeFlavor'

    if milkBackClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModePress'
    
    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'


#battermodeflavor page
#user chooses flavor of icecream
#after user chooses flavor, a smaller cup moves to actual cup and changes its color
def batterModeFlavor_redrawAll(app, canvas):
    #sets font
    font = 'Arial 26 bold'
    #sets background color
    
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us make the batter!',
                       font=font, fill='black')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    #takes you to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')

    orderFont = 'Arial 11 bold'
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')
    if app.level>1:
        canvas.create_text(520, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(520, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1
    
        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')

    canvas.create_image((app.width/2+(app.width*5)/6)/2, (app.height/4+(app.height*4.9)/7)/2, image=ImageTk.PhotoImage(app.milkJug2))
    canvas.create_rectangle(app.width/2+(app.width/15.5), app.height/4+app.height/14, (app.width*5)/6-(app.width/15.5), (app.height*5)/6, outline = 'light pink')
    canvas.create_text(app.width/4, app.height/3, text='Press the correct flavor',
                       font=font, fill='black')

    #gray rectangle
    canvas.create_rectangle(10, app.height/3+20, 190 +(app.width/4 - app.width/6), (app.height/3)+3.5*(app.height/10)+20, fill = 'light gray')
    d0 = 10
    e0 = app.height/3+20
    d1 = 190 +(app.width/4 - app.width/6)
    e1 = (app.height/3)+3.5*(app.height/10)+20
    canvas.create_text((d0+d1)/2, e0 + ((e1-e0)/3), text = 'CHOOSE', font = font, fill = 'black')               
    #chocolate flavor
    #rectangle representing chocolate button
    #pressing button changes color of milk to represent flavor
    canvas.create_rectangle(25,app.height/3 + 2.5*(app.height/10), 25 + (app.width/4 - app.width/6), (app.height/3)+3.5*(app.height/10), fill = '#401c03', outline = '#401c03')
    x0 = 25
    y0 = app.height/3 + 2.5*(app.height/10)
    x1 = 25 + (app.width/4 - app.width/6)
    y1 = (app.height/3)+3.5*(app.height/10)
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'C', font = 'Helvetica 20 bold', fill = 'white')

    #vanilla flavor
    #rectangle representing vanilla button

    canvas.create_rectangle(app.width/6, app.height/3 + 2.5*(app.height/10), app.width/4, (app.height/3)+3.5*(app.height/10), fill = '#f2ede9', outline = '#f2ede9')
    x0 = app.width/6
    y0 = app.height/3 + 2.5*(app.height/10)
    x1 = app.width/4
    y1 = (app.height/3)+3.5*(app.height/10)
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'V', font = 'Helvetica 20 bold', fill = 'black')

    #strawberry flavor
    #rectangle representing strawberry button
    canvas.create_rectangle(175, app.height/3 + 2.5*(app.height/10), 175 +(app.width/4 - app.width/6), (app.height/3)+3.5*(app.height/10), fill = '#f5bae5', outline = '#f5bae5')
    x0 = 175
    y0 = app.height/3 + 2.5*(app.height/10)
    x1 = 175 + (app.width/4 - app.width/6)
    y1 = (app.height/3)+3.5*(app.height/10)
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'S', font = 'Helvetica 20 bold', fill = 'white')
    
    #smaller milk cup that moves horizontal to actual cup
    canvas.create_rectangle(app.width/6+app.currentOrder.getMoveHorizontal(), (app.height/3)+3.5*(app.height/10)+35, app.width/4+app.currentOrder.getMoveHorizontal(), (app.height/3)+5.5*(app.height/10)-10, outline = 'black')
    canvas.create_rectangle(app.width/6+app.currentOrder.getMoveHorizontal(), (app.height/3)+3.5*(app.height/10)+60, app.width/4+app.currentOrder.getMoveHorizontal(), (app.height/3)+5.5*(app.height/10)-10, fill = app.currentOrder.getTemporaryFlavorColor())


    #actual milk rectangle
    canvas.create_rectangle(app.width/2+(app.width/15.5), (app.height*5)/6 - (app.currentOrder.getActualMilkPresses())*((((app.height*5)/6) - (app.height/4+app.height/14))/3), (app.width*5)/6-(app.width/15.5), (app.height*5)/6, fill = app.currentOrder.getActualColor())

    #rectnagle representing done button
    canvas.create_oval((app.width*5)/6 - (app.width/3- app.width/7), (app.height/3)+5.5*(app.height/10), (app.width*5)/6, (app.height/3)+6.5*(app.height/10), fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = (app.width*5)/6 - (app.width/3- app.width/7)
    b0 = (app.height/3)+5.5*(app.height/10)
    a1 = (app.width*5)/6
    b1 = (app.height/3)+6.5*(app.height/10)
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Next', font = 'Helvetica 20 bold', fill = 'black')

    #back button
    canvas.create_oval((app.width*5)/6 - 2*(app.width/3- app.width/7) - app.width/13, (app.height/3)+5.5*(app.height/10), (app.width*5)/6 - (app.width/3- app.width/7) - app.width/13, (app.height/3)+6.5*(app.height/10), fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = (app.width*5)/6 - 2*(app.width/3- app.width/7) - app.width/13
    b0 = (app.height/3)+5.5*(app.height/10)
    a1 = (app.width*5)/6 - 1*(app.width/3- app.width/7) - app.width/13
    b1 = (app.height/3)+6.5*(app.height/10)
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Back', font = 'Helvetica 20 bold', fill = 'black')

    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')


def batterModeFlavor_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'

    #after button is pressed, smaller cup moves to larger cup
    #once it reaches larger cup, it changes its color
    if app.currentOrder.getTemporaryFlavorColor() != 'white':
        if app.currentOrder.getMoveHorizontal() < 175:
            app.currentOrder.setMoveHorizontal(5)
        else:
            app.currentOrder.setActualColor(app.color)





def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)


#checks for pressing area of chocolate
def chocolateClickedInBox(app, x, y, boxNum):
    return (25 <= x <= 25 + (app.width/4 - app.width/6) and
            app.height/3 + 2.5*(app.height/10) <= y <= (app.height/3)+3.5*(app.height/10))

#checks for pressing area of vanilla
def vanillaClickedInBox(app, x, y, boxNum):
    return (app.width/6 <= x <= app.width/4 and
            app.height/3 + 2.5*(app.height/10) <= y <= (app.height/3)+3.5*(app.height/10))


    
#checks for pressing area of chocolate
def strawberryClickedInBox(app, x, y, boxNum):
    return (175 <= x <= 175 + (app.width/4 - app.width/6) and
            app.height/3 + 2.5*(app.height/10) <= y <= (app.height/3)+3.5*(app.height/10))

#checks for pressing area of done button 
def flavorDoneClickedInBox(app, x, y, boxNum):
    return ((app.width*5)/6 - (app.width/3- app.width/7) <= x <= (app.width*5)/6 and
            (app.height/3)+5.5*(app.height/10) <= y <= (app.height/3)+6.5*(app.height/10))

def flavorBackClickedInBox(app, x, y, boxNum):
    return ((app.width*5)/6 - 2*(app.width/3- app.width/7) - app.width/13 <= x <= (app.width*5)/6 - 1*(app.width/3- app.width/7) - app.width/13 and
            (app.height/3)+5.5*(app.height/10) <= y <= (app.height/3)+6.5*(app.height/10))


def batterModeFlavor_mousePressed(app, event):
    #changes app.color to shade of brown, white, or pink to represent different
    #flavors if chocolateClickedInBox, vanillaClickedInBox, strawberryClickedInBox
    #is true
  
    if chocolateClickedInBox(app, event.x, event.y, 0):
        app.actualFlavor = 'Chocolate'
        app.color = '#401c03'
        app.currentOrder.setTemporaryFlavorColor(app.color)
        app.currentOrder.setActualFlavor(app.actualFlavor)
        # app.currentOrder.setActualColor(app.color)
    if vanillaClickedInBox(app, event.x, event.y, 0):
        app.actualFlavor = 'Vanilla'
        app.color = '#f2ede9'
        app.currentOrder.setTemporaryFlavorColor(app.color)
        app.currentOrder.setActualFlavor(app.actualFlavor)
        # app.currentOrder.setActualColor(app.color)
    if strawberryClickedInBox(app, event.x, event.y, 0):
        app.actualFlavor = 'Strawberry'
        app.color = '#f5bae5'
        app.currentOrder.setTemporaryFlavorColor(app.color)
        app.currentOrder.setActualFlavor(app.actualFlavor)
        # app.currentOrder.setActualColor(app.color)

    
    #goes to next screen if done button is pressed
    if flavorDoneClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModeSugar'

    if flavorBackClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModeMilk'

    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'


# adds sugar to batter
#uses app.dots to create small dots that represent sugar particles
#user can add or remove sugar by pressing button
def batterModeSugar_redrawAll(app, canvas):
    #sets font

    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us make the batter!',
                       font=font, fill='black')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')

    orderFont = 'Arial 11 bold'
    #displays order at side of screen
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')
    if app.level>1:
        canvas.create_text(520, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(520, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1

        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')

    canvas.create_image((app.width/2+(app.width*5)/6)/2, (app.height/4+(app.height*4.9)/7)/2, image=ImageTk.PhotoImage(app.milkJug2))
    canvas.create_rectangle(app.width/2+(app.width/15.5), app.height/4+app.height/14, (app.width*5)/6-(app.width/15.5), (app.height*5)/6, outline = 'light pink')
    
    canvas.create_text(app.width/4, app.height/3-20, text='Press for sugar',
                       font=font, fill='black')
    #creates rectangle representing button for adding sugar
    canvas.create_oval(app.width/7, app.height/2 - 1.5*(app.height/10), app.width/3, (app.height/2)-0.5*(app.height/10), fill = 'light blue', activefill= '#54a8e8', outline = 'light blue')
    x0 = app.width/7
    y0 = app.height/2 - 1.5*(app.height/10)
    x1 = app.width/3
    y1 = (app.height/2)-0.5*(app.height/10)
    canvas.create_text(4*(x0 + x1)/7,(y0+y1)/2, text = 'Sugar', font = 'Helvetica 20 bold', fill = 'black')
    #adding milk image

    canvas.create_image(3*(x0 + x1)/8, (y0+y1)/2, image=ImageTk.PhotoImage(app.sugarImage2))


    #button for remove sugar
    canvas.create_oval(app.width/7, app.height/2, app.width/3, (app.height/2)+(app.height/10), fill = 'light blue', activefill= '#54a8e8', outline = 'light blue')
    x0 = app.width/7
    y0 = app.height/2
    x1 = app.width/3
    y1 = (app.height/2)+(app.height/10)
    #sugar button
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'Remove', font = 'Helvetica 20 bold', fill = 'black')
   
    
    #milk white rectangle
    canvas.create_rectangle(app.width/2+(app.width/15.5), (app.height*5)/6 - (app.currentOrder.getActualMilkPresses())*((((app.height*5)/6) - (app.height/4+app.height/14))/3), (app.width*5)/6-(app.width/15.5), (app.height*5)/6, fill = app.currentOrder.getActualColor())

    #done button to move to next screen
    canvas.create_oval(app.width/7, (app.height/2)+1.5*(app.height/10), app.width/3, (app.height/2)+2.5*(app.height/10), fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = app.width/7
    b0 = (app.height/2)+1.5*(app.height/10)
    a1 = app.width/3
    b1 = (app.height/2)+2.5*(app.height/10)
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Next', font = 'Helvetica 20 bold', fill = 'black')


    #back button
    canvas.create_oval(app.width/7, (app.height/2)+3*(app.height/10), app.width/3, (app.height/2)+4*(app.height/10), fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    c0 = app.width/7
    d0 = (app.height/2)+3*(app.height/10)
    c1 = app.width/3
    d1 = (app.height/2)+4*(app.height/10)
    canvas.create_text((c0 + c1)/2,(d0+d1)/2, text = 'Back', font = 'Helvetica 20 bold', fill = 'black')


    #sets cx and cy values to create circles that represent sugar particles.
    #pressing sugar button increases area of rectangle with sugar to represent additional sugar

    
    if app.currentOrder.getActualSugarPresses() > 0:
        for i in range(400):
            cxFirst = int(app.width/2+(app.width/15.5)) + app.sugarRadius 
            cxSecond = int((app.width*5)/6-(app.width/15.5)) - app.sugarRadius
        #randomly selects cx from range
            cx = random.randint(cxFirst, cxSecond)
        

            upperBound = int((app.height*5)/6 - (app.currentOrder.getActualMilkPresses())*((((app.height*5)/6) - (app.height/4+app.height/14))/3))
            cyFirst = upperBound - app.currentOrder.getActualSugarPresses()*5
  
            cySecond = upperBound
        #randomly selects cy from range
            cy = random.randint(cyFirst, cySecond)
            
            #creates small oval shapes that represent sugar particles
            canvas.create_oval(cx-app.sugarRadius, cy-app.sugarRadius, cx+app.sugarRadius, cy+app.sugarRadius, fill='white', outline='white')

    #displays time at top of screen
    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')




def batterModeSugar_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'


#checks if user presses in area of sugar button
def moreSugarClickedInBox(app, x, y, boxNum):
    return (app.width/7 <= x <= app.width/3 and
            app.height/2 - 1.5*(app.height/10) <= y <= (app.height/2)-0.5*(app.height/10))

def removeSugarClickedInBox(app,x,y,boxNum):
    return (app.width/7 <= x <= app.width/3 and
            app.height/2 <= y <= (app.height/2)+(app.height/10))

def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)

#checks for pressing area of done button 
def sugarDoneClickedInBox(app, x, y, boxNum):
    return (app.width/7 <= x <= app.width/3 and
            (app.height/2)+1.5*(app.height/10) <= y <= (app.height/2)+2.5*(app.height/10))

def sugarBackClickedInBox(app, x, y, boxNum):
    return (app.width/7 <= x <= app.width/3 and
            (app.height/2)+3*(app.height/10) <= y <= (app.height/2)+4*(app.height/10))



def batterModeSugar_mousePressed(app, event):
    #more sugar and done button
    if moreSugarClickedInBox(app, event.x, event.y, 0):
        #adds more sugar to cup by calling function in order class
        if app.currentOrder.getActualSugarPresses() < 3:
            app.currentOrder.incrementSugarClicked()
            app.mode = 'batterModeSugar'
    if removeSugarClickedInBox(app, event.x, event.y, 0):
        #reduces sugar in cup by callling function in order class
        if app.currentOrder.getActualSugarPresses()>0:
            app.currentOrder.decrementSugarClicked()
            app.mode = 'batterModeSugar'
    #takes user to next screen
    if sugarDoneClickedInBox(app, event.x, event.y, 0):
        app.mode = 'cupOrConeMode'

    #takes user to previous screen
    if sugarBackClickedInBox(app, event.x, event.y, 0):
        app.mode = 'batterModeFlavor'
    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'


#in this screen, user picks cone or cup depending on order
def cupOrConeMode_redrawAll(app, canvas):
    #sets font
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us scoop icecream!',
                       font=font, fill='black')
    
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    #takes you to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')

    orderFont = 'Arial 11 bold'
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')

    if app.level>1:
        canvas.create_text(520, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(520, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1

        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')

    #cup button
    canvas.create_oval(app.width/5, app.height/2-0.5*app.height/10, app.width/5+(app.width/3-app.width/7), app.height/2+0.5*app.height/10, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    a0 = app.width/5
    b0 = app.height/2-0.5*app.height/10
    a1 = app.width/5+(app.width/3-app.width/7)
    b1 = app.height/2+0.5*app.height/10
    canvas.create_text((a0 + a1)/2,(b0+b1)/2, text = 'Cup', font = 'Helvetica 20 bold', fill = 'black', activefill = '#54a8e8')

    #cone button
    canvas.create_oval(app.width/5+2*(app.width/3-app.width/7), app.height/2-0.5*app.height/10, app.width/5+3*(app.width/3-app.width/7), app.height/2+0.5*app.height/10, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    x0 = app.width/5+2*(app.width/3-app.width/7)
    y0 = app.height/2-0.5*app.height/10
    x1 = app.width/5+3*(app.width/3-app.width/7)
    y1 = app.height/2+0.5*app.height/10
    canvas.create_text((x0 + x1)/2,(y0+y1)/2, text = 'Cone', font = 'Helvetica 20 bold', fill = 'black', activefill = '#54a8e8')

    #displays timer at side of screen
    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')




def cupOrConeMode_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'


def cupClickedInBox(app, x, y, boxNum):
    return (app.width/5 <= x <= app.width/5+(app.width/3-app.width/7) and
            app.height/2-0.5*app.height/10 <= y <= app.height/2+0.5*app.height/10)

def coneClickedInBox(app, x, y, boxNum):
    return (app.width/5+2*(app.width/3-app.width/7) <= x <= app.width/5+3*(app.width/3-app.width/7) and
            app.height/2-0.5*app.height/10 <= y <= app.height/2+0.5*app.height/10)

def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)

def cupOrConeMode_mousePressed(app, event):
    #more sugar and done button
    #takes user to cone or cup screens 
    if cupClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setActualCupOrCone('Cup')
        app.mode = 'coneScoopMode'
     
    if coneClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setActualCupOrCone('Cone')
        app.mode = 'coneScoopMode'

    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'

#here, the user drag and drop icecream scoops to the cone 
def coneScoopMode_redrawAll(app, canvas):

    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us scoop icecream in a cone!',
                       font=font, fill='black')
    
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    #takes you to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')

    #draws order at side of screen
    orderFont = 'Arial 11 bold'
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')

    if app.level>1:
        canvas.create_text(520, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(520, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1

        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')

    #displays cup or cone depending on button that user chose before
    if app.currentOrder.getActualCupOrCone() == 'Cone':
        canvas.create_image((app.width*3)/4, app.height/2+app.height/13, image=ImageTk.PhotoImage(app.icecreamCone2))
    elif app.currentOrder.getActualCupOrCone() == 'Cup':
        canvas.create_image((app.width*3)/4, app.height/2+app.height/5, image=ImageTk.PhotoImage(app.icecreamCup2))
   
    canvas.create_image((app.width)/4, (app.height*3)/4, image=ImageTk.PhotoImage(app.icecreamBowl2))

    #creates three icecream scoops 
    icecreamScoop(app, app.currentOrder.getFirstScoopX(), app.currentOrder.getFirstScoopY(), app.currentOrder.getActualFlavor(), canvas)
    icecreamScoop(app, app.currentOrder.getSecondScoopX(), app.currentOrder.getSecondScoopY(), app.currentOrder.getActualFlavor(), canvas)
    icecreamScoop(app, app.currentOrder.getThirdScoopX(), app.currentOrder.getThirdScoopY(), app.currentOrder.getActualFlavor(), canvas)


    canvas.create_oval(500, 450, 575, 490, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    canvas.create_text((500+575)/2, 470, text = 'Next', font = 'Helvetica 20 bold')

    canvas.create_oval(25, 450, 100, 490, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    canvas.create_text((25+100)/2, 470, text = 'Back', font = 'Helvetica 20 bold')

    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')




def coneScoopMode_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'

def goHomeClickedInBox(app, x, y, boxNum):
    return(5<=x<=60 and 60<=y<=90)
  

#sets image based on what flavor is
def icecreamScoop(app, x,y, flavor, canvas):
    if flavor == 'Chocolate':
        canvas.create_image(x,y, image=ImageTk.PhotoImage(app.chocolateScoop2))
    elif flavor == 'Vanilla':
        canvas.create_image(x,y, image=ImageTk.PhotoImage(app.vanillaScoop2))
    else:
        canvas.create_image(x,y, image=ImageTk.PhotoImage(app.strawberryScoop2))

#checks if user is clicking on area of any of scoops
def firstScoopClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getFirstScoopX()-70 <= x <= app.currentOrder.getFirstScoopX()+70 and
            app.currentOrder.getFirstScoopY()-70 <= y <= app.currentOrder.getFirstScoopY()+70)

def secondScoopClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getSecondScoopX()-70 <= x <= app.currentOrder.getSecondScoopX()+70 and
            app.currentOrder.getSecondScoopY()-70 <= y <= app.currentOrder.getSecondScoopY()+70)

def thirdScoopClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getThirdScoopX()-70 <= x <= app.currentOrder.getThirdScoopX()+70 and
            app.currentOrder.getThirdScoopY()-70 <= y <= app.currentOrder.getThirdScoopY()+70)

def coneScoopDoneClickedInBox(app, x, y, boxNum):
    return(500 <= x <= 575 and 450 <= y <= 490)

def coneScoopBackClickedInBox(app, x, y, boxNum):
    return(25 <= x <= 100 and 450 <= y <= 490)


            
def coneScoopMode_mousePressed(app, event):
    #sets firstScoopMove to true and makes other scoops false
    if firstScoopClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setFirstScoopMove(True)
    else:
        app.currentOrder.setFirstScoopMove(False)
    
    if secondScoopClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setSecondScoopMove(True)
    else:
        app.currentOrder.setSecondScoopMove(False)

    if thirdScoopClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setThirdScoopMove(True)
    else:
        app.currentOrder.setThirdScoopMove(False)

    if coneScoopDoneClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setFirstScoopFinalLocX(app.currentOrder.getFirstScoopX())
        app.currentOrder.setFirstScoopFinalLocY(app.currentOrder.getFirstScoopY())
        app.currentOrder.setSecondScoopFinalLocX(app.currentOrder.getSecondScoopX())
        app.currentOrder.setSecondScoopFinalLocY(app.currentOrder.getSecondScoopY())
        app.currentOrder.setThirdScoopFinalLocX(app.currentOrder.getThirdScoopX())
        app.currentOrder.setThirdScoopFinalLocY(app.currentOrder.getThirdScoopY())


        #increases number of scoops if location of final scoop is near cone/cup
        if app.currentOrder.getFirstScoopFinalLocX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getFirstScoopFinalLocX() <= (app.width*2)/3 + 2.5*app.width/10:
            if app.currentOrder.getFirstScoopFinalLocY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getFirstScoopFinalLocY() <= app.height/2+app.height/7.5:
                app.currentOrder.incrementScoopsClicked()

        if app.currentOrder.getSecondScoopFinalLocX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getSecondScoopFinalLocX() <= (app.width*2)/3 + 2.5*app.width/10:
            if app.currentOrder.getSecondScoopFinalLocY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getSecondScoopFinalLocY() <= app.height/2+app.height/7.5:
                app.currentOrder.incrementScoopsClicked()

        if app.currentOrder.getThirdScoopFinalLocX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getThirdScoopFinalLocX() <= (app.width*2)/3 + 2.5*app.width/10:
            if app.currentOrder.getThirdScoopFinalLocY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getThirdScoopFinalLocY() <= app.height/2+app.height/7.5:
                app.currentOrder.incrementScoopsClicked()
            
        if app.level>1:
            app.mode = 'coneToppingsMode'
        else:
            app.mode = 'judgeMode'

    if coneScoopBackClickedInBox(app, event.x, event.y, 0):
        app.mode = 'cupOrConeMode'
    if goHomeClickedInBox(app, event.x, event.y, 0):
        app.foundImage = False
        app.mode = 'sittingMode'


#if first scoop is being moved, other scoops are not being moved
def coneScoopMode_mouseDragged(app, event):
    # if tester(app, event.x, event.y, 0):
    if app.currentOrder.getFirstScoopMove() == True:
        if app.currentOrder.getSecondScoopMove() == False:
            if app.currentOrder.getThirdScoopMove() == False:
                app.currentOrder.setFirstScoopX(event.x)
                app.currentOrder.setFirstScoopY(event.y)
                app.currentOrder.setSecondScoopX(app.currentOrder.getSecondScoopX())
                app.currentOrder.setSecondScoopY(app.currentOrder.getSecondScoopY())
                app.currentOrder.setThirdScoopX(app.currentOrder.getThirdScoopX())
                app.currentOrder.setThirdScoopY(app.currentOrder.getThirdScoopY())


    if app.currentOrder.getSecondScoopMove() == True:
        if app.currentOrder.getFirstScoopMove() == False:
            if app.currentOrder.getThirdScoopMove() == False:
                app.currentOrder.setSecondScoopX(event.x)
                app.currentOrder.setSecondScoopY(event.y)
                app.currentOrder.setFirstScoopX(app.currentOrder.getFirstScoopX())
                app.currentOrder.setFirstScoopY(app.currentOrder.getFirstScoopY())
                app.currentOrder.setThirdScoopX(app.currentOrder.getThirdScoopX())
                app.currentOrder.setThirdScoopY(app.currentOrder.getThirdScoopY())


    if app.currentOrder.getThirdScoopMove() == True:
        if app.currentOrder.getFirstScoopMove() == False:
            if app.currentOrder.getSecondScoopMove() == False:
                app.currentOrder.setThirdScoopX(event.x)
                app.currentOrder.setThirdScoopY(event.y)
                app.currentOrder.setFirstScoopX(app.currentOrder.getFirstScoopX())
                app.currentOrder.setFirstScoopY(app.currentOrder.getFirstScoopY())
                app.currentOrder.setSecondScoopX(app.currentOrder.getSecondScoopX())
                app.currentOrder.setSecondScoopY(app.currentOrder.getSecondScoopY())



#here, the user drags cherries, marshmellows, or oreo toppings to cone/cup(only applicable in later levels)
#user can also drag whipped cream and spray it on cup/cone through dots
def coneToppingsMode_redrawAll(app, canvas):

    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Let us scoop icecream in a cone!',
                       font=font, fill='black')
    
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')

    #takes you to home screen
    canvas.create_oval(5, 60, 60, 90, fill = 'white', activefill = 'light gray', outline = 'white')
    canvas.create_text(32, 75, text = 'Home', activefill = 'light gray', fill = 'black')

    orderFont = 'Arial 11 bold'
    canvas.create_text(529, 40, text = f'Flavor: {app.currentOrder.getFlavor()}',
                       font= orderFont, fill='black')
    canvas.create_text(529, 55, text = f'Cups of Milk: {app.currentOrder.getCupsOfMilk()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 70, text = f'Spoons of sugar: {app.currentOrder.getSpoonsOfSugar()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 85, text = f'Cup or Cone: {app.currentOrder.getCupOrCone()}',
                       font=orderFont, fill='black')
    canvas.create_text(529, 100, text = f'Number of Scoops: {app.currentOrder.getNumOfScoops()}',
                       font=orderFont, fill='black')

    if app.level>1:
        canvas.create_text(520, 115, text = f'Toppings:',
                        font=orderFont, fill='black')
        toppingsIncrement = 0
        for i in range(len(app.currentOrder.getToppings())):
            canvas.create_text(520, 130 + toppingsIncrement*10, text = f'{app.currentOrder.getToppings()[i]}',
                        font=orderFont, fill='black')
            toppingsIncrement+=1

        canvas.create_text(529, 155, text = f'{app.currentOrder.getWhippedCream()}',
                        font=orderFont, fill='black')

    #sets font
    if app.currentOrder.getActualCupOrCone() == 'Cone':
        canvas.create_image((app.width*3)/4, app.height/2+app.height/13, image=ImageTk.PhotoImage(app.icecreamCone2))
    elif app.currentOrder.getActualCupOrCone() == 'Cup':
        canvas.create_image((app.width*3)/4, app.height/2+app.height/5, image=ImageTk.PhotoImage(app.icecreamCup2))
   
    
    # canvas.create_rectangle((app.width*3)/4 - app.width/6, 0,(app.width*3)/4 + app.width/6, app.height/2+app.height/6, outline = 'black')

    #cherry toppings bowl
    canvas.create_image((app.width)/4, (app.height*3)/4, image=ImageTk.PhotoImage(app.toppingsBowl2))   

    #oreo toppings bowl
    canvas.create_image((app.width)/4, (app.height*2)/4, image=ImageTk.PhotoImage(app.toppingsBowl4))   

    #marshmellow toppings bowl
    canvas.create_image((app.width)/4, (app.height)/4, image=ImageTk.PhotoImage(app.toppingsBowl6)) 
   


    #checks whether to put icecream scoop or not
    if app.currentOrder.getFirstScoopFinalLocX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getFirstScoopFinalLocX() <= (app.width*2)/3 + 2.5*app.width/10:
        if app.currentOrder.getFirstScoopFinalLocY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getFirstScoopFinalLocY() <= app.height/2+app.height/7.5:
            icecreamScoop(app, app.currentOrder.getFirstScoopFinalLocX(), app.currentOrder.getFirstScoopFinalLocY(), app.currentOrder.getActualFlavor(), canvas)
            
    if app.currentOrder.getSecondScoopFinalLocX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getSecondScoopFinalLocX() <= (app.width*2)/3 + 2.5*app.width/10:
        if app.currentOrder.getSecondScoopFinalLocY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getSecondScoopFinalLocY() <= app.height/2+app.height/7.5:
         
            icecreamScoop(app, app.currentOrder.getSecondScoopFinalLocX(), app.currentOrder.getSecondScoopFinalLocY(), app.currentOrder.getActualFlavor(), canvas)

    if app.currentOrder.getThirdScoopFinalLocX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getThirdScoopFinalLocX() <= (app.width*2)/3 + 2.5*app.width/10:
        if app.currentOrder.getThirdScoopFinalLocY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getThirdScoopFinalLocY() <= app.height/2+app.height/7.5:
         
            icecreamScoop(app, app.currentOrder.getThirdScoopFinalLocX(), app.currentOrder.getThirdScoopFinalLocY(), app.currentOrder.getActualFlavor(), canvas)




    #adds three cherry toppings
    cherryTopping(app, app.currentOrder.getFirstCherryX(), app.currentOrder.getFirstCherryY(), canvas)
    cherryTopping(app, app.currentOrder.getSecondCherryX(), app.currentOrder.getSecondCherryY(), canvas)
    cherryTopping(app, app.currentOrder.getThirdCherryX(), app.currentOrder.getThirdCherryY(), canvas)

    #adds three oreo toppings
    oreoTopping(app, app.currentOrder.getFirstOreoX(), app.currentOrder.getFirstOreoY(), canvas)
    oreoTopping(app, app.currentOrder.getSecondOreoX(), app.currentOrder.getSecondOreoY(), canvas)
    oreoTopping(app, app.currentOrder.getThirdOreoX(), app.currentOrder.getThirdOreoY(), canvas)
       
    #adds three marshmellow toppings
    marshmellowTopping(app, app.currentOrder.getFirstMarshmellowX(), app.currentOrder.getFirstMarshmellowY(), canvas)
    marshmellowTopping(app, app.currentOrder.getSecondMarshmellowX(), app.currentOrder.getSecondMarshmellowY(), canvas)
    marshmellowTopping(app, app.currentOrder.getThirdMarshmellowX(), app.currentOrder.getThirdMarshmellowY(), canvas)
    #done button
    canvas.create_oval(500, 450, 575, 490, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    canvas.create_text((500+575)/2, 470, text = 'Next', font = 'Helvetica 20 bold')

    #back button
    #done button
    canvas.create_oval(25, 450, 100, 490, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    canvas.create_text((25+100)/2, 470, text = 'Back', font = 'Helvetica 20 bold')




    if app.totalSeconds>0:
        if app.totalSeconds%60 < 10:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:0{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%60 == 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}0', font = 'Helvetica 26 bold', fill = 'black')
        elif app.totalSeconds%10 == 0 and app.totalSeconds%60 != 0:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
        else:
            canvas.create_text(30, 20, text = f'{app.totalSeconds//60}:{app.totalSeconds%60}', font = 'Helvetica 26 bold', fill = 'black')
    
    if(app.currentOrder.getWhippedCreamX()!=0):
        if(app.currentOrder.getWhippedCreamY()!=0):
            canvas.create_image(app.currentOrder.getWhippedCreamX(), app.currentOrder.getWhippedCreamY(), image=ImageTk.PhotoImage(app.whippedCream2))
            for dot in app.currentOrder.getDots():
                cx, cy, color, r = dot
                drawDot(app, canvas, cx, cy, color, r)

                

def coneToppingsMode_timerFired(app):
    timer = datetime.timedelta(seconds = app.totalSeconds)
    app.timer += 1

    if app.timer % 60 == 0:
        if app.totalSeconds > 0:
            app.totalSeconds -= 1
        else:
            app.mode = 'youLoseMode'

    for i in range(len(app.orders)):
        timer = datetime.timedelta(seconds = app.orders[i].getTotalSecond())
    
        app.orders[i].incrementTimer(1)
        if app.orders[i].getTimer() % 60 == 0:
            if app.orders[i].getTotalSecond() > 0:
                app.orders[i].setTotalSecond(app.orders[i].getTotalSecond() - 1)
 
            else:
                app.mode = 'youLoseMode'


#create cherry image
def cherryTopping(app, x,y, canvas):
    canvas.create_image(x,y, image=ImageTk.PhotoImage(app.cherry2))

#create oreo image
def oreoTopping(app, x,y, canvas):
    canvas.create_image(x,y, image=ImageTk.PhotoImage(app.oreo2))
    # canvas.create_rectangle(x-15,y-18,x+15,y+18, outline = 'black')

#create marshmellow image
def marshmellowTopping(app, x,y, canvas):
    canvas.create_image(x,y, image=ImageTk.PhotoImage(app.marshmellow2))
    # canvas.create_rectangle(x-15,y-21,x+15,y+16, outline = 'black') 

#checks if user clicks on area of cherries
def firstCherryClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getFirstCherryX()-15 <= x <= app.currentOrder.getFirstCherryX()+15 and
            app.currentOrder.getFirstCherryY()-39 <= y <= app.currentOrder.getFirstCherryY()+39)

def secondCherryClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getSecondCherryX()-15 <= x <= app.currentOrder.getSecondCherryX()+15 and
            app.currentOrder.getSecondCherryY()-39 <= y <= app.currentOrder.getSecondCherryY()+39)

def thirdCherryClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getThirdCherryX()-15 <= x <= app.currentOrder.getThirdCherryX()+15 and
            app.currentOrder.getThirdCherryY()-39 <= y <= app.currentOrder.getThirdCherryY()+39)


#oreo clicked in box
def firstOreoClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getFirstOreoX()-15 <= x <= app.currentOrder.getFirstOreoX()+15 and
            app.currentOrder.getFirstOreoY()-18 <= y <= app.currentOrder.getFirstOreoY()+18)

def secondOreoClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getSecondOreoX()-15 <= x <= app.currentOrder.getSecondOreoX()+15 and
            app.currentOrder.getSecondOreoY()-18 <= y <= app.currentOrder.getSecondOreoY()+18)

def thirdOreoClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getThirdOreoX()-15 <= x <= app.currentOrder.getThirdOreoX()+15 and
            app.currentOrder.getThirdOreoY()-18 <= y <= app.currentOrder.getThirdOreoY()+18)

#checks if user presses on area of marshmellow
def firstMarshmellowClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getFirstMarshmellowX()-15 <= x <= app.currentOrder.getFirstMarshmellowX()+15 and
            app.currentOrder.getFirstMarshmellowY()-21 <= y <= app.currentOrder.getFirstMarshmellowY()+16)

def secondMarshmellowClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getSecondMarshmellowX()-15 <= x <= app.currentOrder.getSecondMarshmellowX()+15 and
            app.currentOrder.getSecondMarshmellowY()-21 <= y <= app.currentOrder.getSecondMarshmellowY()+16)

def thirdMarshmellowClickedInBox(app, x, y, boxNum):
    return (app.currentOrder.getThirdMarshmellowX()-15 <= x <= app.currentOrder.getThirdMarshmellowX()+15 and
            app.currentOrder.getThirdMarshmellowY()-21 <= y <= app.currentOrder.getThirdMarshmellowY()+16)

def whippedCreamClickedInBox(app,x,y,boxNum):
    return(app.currentOrder.getWhippedCreamX()- 20 <= x <= app.currentOrder.getWhippedCreamX() + 20 and app.currentOrder.getWhippedCreamY() - 65 <= y<= app.currentOrder.getWhippedCreamY() +60)






#checks if user presses area of done button
def coneToppingsDoneClickedInBox(app, x, y, boxNum):
    return(500 <= x <= 575 and 450 <= y <= 490)

#checks if user presses area of next button
def coneToppingsBackClickedInBox(app, x, y, boxNum):
    return(25 <= x <= 100 and 450 <= y <= 490)          

            
def coneToppingsMode_mousePressed(app, event):
    if firstCherryClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setFirstCherryMove(True)
        
    else:
        app.currentOrder.setFirstCherryMove(False)
    
    if secondCherryClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setSecondCherryMove(True)
    else:
        app.currentOrder.setSecondCherryMove(False)

    if thirdCherryClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setThirdCherryMove(True)
    else:
        app.currentOrder.setThirdCherryMove(False)



    if firstOreoClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setFirstOreoMove(True)
    else:
        app.currentOrder.setSecondOreoMove(False)
    
    if secondOreoClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setSecondOreoMove(True)
    else:
        app.currentOrder.setSecondOreoMove(False)

    if thirdOreoClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setThirdOreoMove(True)
    else:
        app.currentOrder.setThirdOreoMove(False)


    if firstMarshmellowClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setFirstMarshmellowMove(True)
    else:
        app.currentOrder.setFirstMarshmellowMove(False)
    
    if secondMarshmellowClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setSecondMarshmellowMove(True)
    else:
        app.currentOrder.setSecondMarshmellowMove(False)

    if thirdMarshmellowClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setThirdMarshmellowMove(True)
    else:
        app.currentOrder.setThirdMarshmellowMove(False)

    if whippedCreamClickedInBox(app, event.x, event.y, 0):
        app.currentOrder.setWhippedCreamMove(True)
    else:
        app.currentOrder.setWhippedCreamMove(False)
    
    if coneToppingsDoneClickedInBox(app, event.x, event.y, 0):

        if 'Cherries' in app.currentOrder.getCherriesToppings():
            app.currentOrder.setActualToppings('Cherries')


        if 'Oreos' in app.currentOrder.getOreosToppings():
            app.currentOrder.setActualToppings('Oreos')


        if 'Marshmellows' in app.currentOrder.getMarshmellowsToppings():
            app.currentOrder.setActualToppings('Marshmellows')

        app.mode = 'judgeMode'

    if coneToppingsBackClickedInBox(app, event.x, event.y, 0):
        app.mode = 'coneScoopMode'



def coneToppingsMode_mouseDragged(app, event):
    # if tester(app, event.x, event.y, 0):
    #sets cherries to event.x and event.y if user is in bounds of cherry
    if app.currentOrder.getFirstCherryMove() == True:
        if app.currentOrder.getSecondCherryMove() == False:
            if app.currentOrder.getThirdCherryMove() == False:
                app.currentOrder.setFirstCherryX(event.x)
                app.currentOrder.setFirstCherryY(event.y)
                app.currentOrder.setSecondCherryX(app.currentOrder.getSecondCherryX())
                app.currentOrder.setSecondCherryY(app.currentOrder.getSecondCherryY())
                app.currentOrder.setThirdCherryX(app.currentOrder.getThirdCherryX())
                app.currentOrder.setThirdCherryY(app.currentOrder.getThirdCherryY())

                if(app.currentOrder.getFirstCherryX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getFirstCherryX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getFirstCherryY() <= app.height/2+app.height/6):
                            app.currentOrder.setCherriesToppings('Cherries')

    if app.currentOrder.getSecondCherryMove() == True:
        if app.currentOrder.getFirstCherryMove() == False:
            if app.currentOrder.getThirdCherryMove() == False:
                app.currentOrder.setSecondCherryX(event.x)
                app.currentOrder.setSecondCherryY(event.y)
                app.currentOrder.setFirstCherryX(app.currentOrder.getFirstCherryX())
                app.currentOrder.setFirstCherryY(app.currentOrder.getFirstCherryY())
                app.currentOrder.setThirdCherryX(app.currentOrder.getThirdCherryX())
                app.currentOrder.setThirdCherryY(app.currentOrder.getThirdCherryY())

                if(app.currentOrder.getSecondCherryX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getSecondCherryX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getSecondCherryY() <= app.height/2+app.height/6):
                            app.currentOrder.setCherriesToppings('Cherries')


    if app.currentOrder.getThirdCherryMove() == True:
        if app.currentOrder.getFirstCherryMove() == False:
            if app.currentOrder.getSecondCherryMove() == False:
                app.currentOrder.setThirdCherryX(event.x)
                app.currentOrder.setThirdCherryY(event.y)
                app.currentOrder.setFirstCherryX(app.currentOrder.getFirstCherryX())
                app.currentOrder.setFirstCherryY(app.currentOrder.getFirstCherryY())
                app.currentOrder.setSecondCherryX(app.currentOrder.getSecondCherryX())
                app.currentOrder.setSecondCherryY(app.currentOrder.getSecondCherryY())

                if(app.currentOrder.getThirdCherryX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getThirdCherryX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getThirdCherryY() <= app.height/2+app.height/6):
                            app.currentOrder.setCherriesToppings('Cherries')
             
    if app.currentOrder.getFirstOreoMove() == True:
        if app.currentOrder.getSecondOreoMove() == False:
            if app.currentOrder.getThirdOreoMove() == False:
                app.currentOrder.setFirstOreoX(event.x)
                app.currentOrder.setFirstOreoY(event.y)
                app.currentOrder.setSecondOreoX(app.currentOrder.getSecondOreoX())
                app.currentOrder.setSecondOreoY(app.currentOrder.getSecondOreoY())
                app.currentOrder.setThirdOreoX(app.currentOrder.getThirdOreoX())
                app.currentOrder.setThirdOreoY(app.currentOrder.getThirdOreoY())

                if(app.currentOrder.getFirstOreoX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getFirstOreoX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getFirstOreoY() <= app.height/2+app.height/6):
                            app.currentOrder.setOreosToppings('Oreos')


    if app.currentOrder.getSecondOreoMove() == True:
        if app.currentOrder.getFirstOreoMove() == False:
            if app.currentOrder.getThirdOreoMove() == False:
                app.currentOrder.setSecondOreoX(event.x)
                app.currentOrder.setSecondOreoY(event.y)
                app.currentOrder.setFirstOreoX(app.currentOrder.getFirstOreoX())
                app.currentOrder.setFirstOreoY(app.currentOrder.getFirstOreoY())
                app.currentOrder.setThirdOreoX(app.currentOrder.getThirdOreoX())
                app.currentOrder.setThirdOreoY(app.currentOrder.getThirdOreoY())

                if(app.currentOrder.getSecondOreoX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getSecondOreoX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getSecondOreoY() <= app.height/2+app.height/6):
                            app.currentOrder.setOreosToppings('Oreos')


    if app.currentOrder.getThirdOreoMove() == True:
        if app.currentOrder.getFirstOreoMove() == False:
            if app.currentOrder.getSecondOreoMove() == False:
                app.currentOrder.setThirdOreoX(event.x)
                app.currentOrder.setThirdOreoY(event.y)
                app.currentOrder.setFirstOreoX(app.currentOrder.getFirstOreoX())
                app.currentOrder.setFirstOreoY(app.currentOrder.getFirstOreoY())
                app.currentOrder.setSecondOreoX(app.currentOrder.getSecondOreoX())
                app.currentOrder.setSecondOreoY(app.currentOrder.getSecondOreoY())

                if(app.currentOrder.getThirdOreoX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getThirdOreoX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getThirdOreoY() <= app.height/2+app.height/6):
                            app.currentOrder.setOreosToppings('Oreos')

                
    #sets oreo location to event.x and event.y if user is in bounds of oreo
    
    if app.currentOrder.getFirstMarshmellowMove() == True:
        if app.currentOrder.getSecondMarshmellowMove() == False:
            if app.currentOrder.getThirdMarshmellowMove() == False:
                app.currentOrder.setFirstMarshmellowX(event.x)
                app.currentOrder.setFirstMarshmellowY(event.y)
                app.currentOrder.setSecondMarshmellowX(app.currentOrder.getSecondMarshmellowX())
                app.currentOrder.setSecondMarshmellowY(app.currentOrder.getSecondMarshmellowY())
                app.currentOrder.setThirdMarshmellowX(app.currentOrder.getThirdMarshmellowX())
                app.currentOrder.setThirdMarshmellowY(app.currentOrder.getThirdMarshmellowY())

                if(app.currentOrder.getFirstMarshmellowX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getFirstMarshmellowX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getFirstMarshmellowY() <= app.height/2+app.height/6):
                            app.currentOrder.setMarshmellowsToppings('Marshmellows')


    if app.currentOrder.getSecondMarshmellowMove() == True:
        if app.currentOrder.getFirstMarshmellowMove() == False:
            if app.currentOrder.getThirdMarshmellowMove() == False:
                app.currentOrder.setSecondMarshmellowX(event.x)
                app.currentOrder.setSecondMarshmellowY(event.y)
                app.currentOrder.setFirstMarshmellowX(app.currentOrder.getFirstMarshmellowX())
                app.currentOrder.setFirstMarshmellowY(app.currentOrder.getFirstMarshmellowY())
                app.currentOrder.setThirdMarshmellowX(app.currentOrder.getThirdMarshmellowX())
                app.currentOrder.setThirdMarshmellowY(app.currentOrder.getThirdMarshmellowY())

                if(app.currentOrder.getSecondMarshmellowX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getSecondMarshmellowX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getSecondMarshmellowY() <= app.height/2+app.height/6):
                            app.currentOrder.setMarshmellowsToppings('Marshmellows')





    


    if app.currentOrder.getThirdMarshmellowMove() == True:
        if app.currentOrder.getFirstMarshmellowMove() == False:
            if app.currentOrder.getSecondMarshmellowMove() == False:
                app.currentOrder.setThirdMarshmellowX(event.x)
                app.currentOrder.setThirdMarshmellowY(event.y)
                app.currentOrder.setFirstMarshmellowX(app.currentOrder.getFirstMarshmellowX())
                app.currentOrder.setFirstMarshmellowY(app.currentOrder.getFirstMarshmellowY())
                app.currentOrder.setSecondMarshmellowX(app.currentOrder.getSecondMarshmellowX())
                app.currentOrder.setSecondMarshmellowY(app.currentOrder.getSecondMarshmellowY())

                if(app.currentOrder.getThirdMarshmellowX() >= (app.width*3)/4 - app.width/6):
                    if(app.currentOrder.getThirdMarshmellowX() <= (app.width*3)/4 + app.width/6):
                        if(app.currentOrder.getThirdMarshmellowY() <= app.height/2+app.height/6):
                            app.currentOrder.setMarshmellowsToppings('Marshmellows')


    

    if app.currentOrder.getWhippedCreamMove() == True:
        app.currentOrder.setWhippedCreamX(event.x)
        app.currentOrder.setWhippedCreamY(event.y)
        #append whipped cream to list of ingredients
        if app.currentOrder.getWhippedCreamX() >= (app.width*2)/3 - app.width/10 and app.currentOrder.getWhippedCreamX() <= (app.width*2)/3 + 2.5*app.width/10:
            if app.currentOrder.getWhippedCreamY() >= app.height/2-3*app.height/7.5 and app.currentOrder.getWhippedCreamY() <= app.height/2+app.height/7.5:
                app.currentOrder.setcx(event.x)
                app.currentOrder.setcy(event.y)
                app.currentOrder.setDots(app.currentOrder.getcx(), app.currentOrder.getcy(), app.currentOrder.getWhippedCreamColor(), app.currentOrder.getWhippedCreamR())          



         


def drawDot(app, canvas, cx, cy, color, r):
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r, fill=color,outline=color)






def judgeMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height*0.04, text='Here is your score!',
                       font=font, fill='black')
    canvas.create_text(30, 50, text = f'Score:{app.totalScore}')
    #judge flavor
    if(app.currentOrder.getFlavor() == app.currentOrder.getActualFlavor()):
        canvas.create_text(app.width/2, app.height/5, text = 'Correct Flavor: +1 point', font = font, fill = 'black')
    else: 
        canvas.create_text(app.width/2, app.height/5, text = 'Incorrect Flavor: 0 point', font = font, fill = 'black')

    
    #judge milk
    if(app.currentOrder.getCupsOfMilk() == app.currentOrder.getActualMilkPresses()):
        canvas.create_text(app.width/2, app.height/5+app.height/10, text = 'Correct cups of milk: +1 point', font = font, fill = 'black')

    else:
        canvas.create_text(app.width/2, app.height/5+app.height/10, text = 'Incorrect cups of milk: 0 point', font = font, fill = 'black')

    #judge sugar
    if(app.currentOrder.getSpoonsOfSugar() == app.currentOrder.getActualSugarPresses()):
        canvas.create_text(app.width/2, app.height/5+2*app.height/10, text = 'Correct spoons of sugar: +1 point', font = font, fill = 'black')

    else:
        canvas.create_text(app.width/2, app.height/5+2*app.height/10, text = 'Incorrect spoons of sugar: 0 point', font = font, fill = 'black')
    #judge cup or cone
    if(app.currentOrder.getCupOrCone() == app.currentOrder.getActualCupOrCone()):
        canvas.create_text(app.width/2, app.height/5+3*app.height/10, text = 'Correct cup or cone: +1 point', font = font, fill = 'black')

    else:
        canvas.create_text(app.width/2, app.height/5+3*app.height/10, text = 'Incorrect cup or cone: 0 point', font = font, fill = 'black')

   #judge number of scoops
    if(app.currentOrder.getNumOfScoops() == app.currentOrder.getActualScoopsPresses()):

        canvas.create_text(app.width/2, app.height/5+4*app.height/10, text = 'Correct number of scoops: +1 point', font = font, fill = 'black')

    else:
    
        canvas.create_text(app.width/2, app.height/5+4*app.height/10, text = 'Incorrect number of scoops: 0 point', font = font, fill = 'black')
    #only judges toppings in upper levels
    if app.level>1:
        toppingsWrongCount = 0
        for toppings in app.currentOrder.getToppings():
            if toppings not in app.currentOrder.getActualToppings():
                toppingsWrongCount+=1
        
        if toppingsWrongCount == 0:
            canvas.create_text(app.width/2, app.height/5+5*app.height/10, text = 'Correct number of toppings: +1 point', font = font, fill = 'black')
        else:
            canvas.create_text(app.width/2, app.height/5+5*app.height/10, text = 'Incorrect number of toppings: 0 point', font = font, fill = 'black')

    

    
    #next button
    canvas.create_oval(500, 450, 575, 490, fill = 'light blue', activefill = '#54a8e8', outline = 'light blue')
    canvas.create_text((500+575)/2, 470, text = 'Next', font = 'Helvetica 20 bold')





#depending on accuracy of user, they get points
#until they reach designated score, they keep playing
#if all customers have received their orders, more customers are randomly generated
#if user runs out of time, they lose game
#in higher levels, toppings are added and time is decreased
def judgeDoneClickedInBox(app, x, y, boxNum):
    return(500 <= x <= 575 and 450 <= y <= 490)

def judgeMode_mousePressed(app, event):
    if(app.currentOrder.getFlavor() == app.currentOrder.getActualFlavor()):
        app.totalScore+=1
        app.currentOrder.incrementScore()
    if(app.currentOrder.getCupsOfMilk() == app.currentOrder.getActualMilkPresses()):
        app.totalScore+=1
        app.currentOrder.incrementScore()
    if(app.currentOrder.getSpoonsOfSugar() == app.currentOrder.getActualSugarPresses()):
        app.totalScore+=1
        app.currentOrder.incrementScore()
    if(app.currentOrder.getCupOrCone() == app.currentOrder.getActualCupOrCone()):
        app.totalScore+=1
        app.currentOrder.incrementScore()
    if(app.currentOrder.getNumOfScoops() == app.currentOrder.getActualScoopsPresses()):
        app.totalScore+=1
        app.currentOrder.incrementScore()

    if app.level>1:
        toppingsWrongCountButton = 0

        for toppings in app.currentOrder.getToppings():
            if toppings not in app.currentOrder.getActualToppings():
                toppingsWrongCountButton+=1
        
        if toppingsWrongCountButton == 0:
            app.totalScore+=1
            app.currentOrder.incrementScore()

    #in first level, removes completed order from list and resets global variables
    #
    if app.level == 1:
        app.orders.remove(app.currentOrder)
        app.kitchenImageList = []
        app.finalImageList = []
        for order in app.orders:
            app.image3 = app.loadImage(order.getImage())
            app.image5 = app.scaleImage(app.image3, 1/10)
            app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
            app.image4 = app.scaleImage(app.image3, 1/3)
            app.kitchenImageList.append(app.image6)
            app.finalImageList.append(app.image4)
            app.foundImageIndex = 0
            app.imageX = 0
            app.imageY = 0
            app.foundImage = False
            app.movingPersonWidth = 0
        #goes back to first screen if there are more customers
        #completed customers are no longer displayer on sitting mode screen
        if len(app.orders)> 0:
            app.mode = 'sittingMode'
        else:
            #if user reaches designated score, they are taken to new page
            if app.totalScore > 24:
                app.mode = 'youWonMode'
            else:
                #randomly adds more orders
                o = Order()
                o2 = Order()
                app.orders.append(o)
                app.orders.append(o2)

                
                app.kitchenImageList = []
                app.finalImageList = []
                for order in app.orders:
                    app.image3 = app.loadImage(order.getImage())
                    app.image5 = app.scaleImage(app.image3, 1/10)
                    app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
                    app.image4 = app.scaleImage(app.image3, 1/3)
                    app.kitchenImageList.append(app.image6)
                    app.finalImageList.append(app.image4)
                    app.foundImageIndex = 0
                    app.imageX = 0
                    app.imageY = 0
                    app.foundImage = False
                    app.movingPersonWidth = 0
                app.mode = 'sittingMode'

    elif app.level == 2:
        app.orders.remove(app.currentOrder)
        app.kitchenImageList = []
        app.finalImageList = []
        for order in app.orders:
            app.image3 = app.loadImage(order.getImage())
            app.image5 = app.scaleImage(app.image3, 1/10)
            app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
            app.image4 = app.scaleImage(app.image3, 1/3)
            app.kitchenImageList.append(app.image6)
            app.finalImageList.append(app.image4)
            app.foundImageIndex = 0
            app.imageX = 0
            app.imageY = 0
            app.foundImage = False
            app.movingPersonWidth = 0
        if len(app.orders)> 0:
            app.mode = 'sittingMode'
        else:
            if app.totalScore > 35:
                app.mode = 'youWonMode'
            else:
                o = Order()
                o2 = Order()
                app.orders.append(o)
                app.orders.append(o2)

                
                app.kitchenImageList = []
                app.finalImageList = []
                for order in app.orders:
                    app.image3 = app.loadImage(order.getImage())
                    app.image5 = app.scaleImage(app.image3, 1/10)
                    app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
                    app.image4 = app.scaleImage(app.image3, 1/3)
                    app.kitchenImageList.append(app.image6)
                    app.finalImageList.append(app.image4)
                    app.foundImageIndex = 0
                    app.imageX = 0
                    app.imageY = 0
                    app.foundImage = False
                    app.movingPersonWidth = 0
                app.mode = 'sittingMode'

    elif app.level == 3:
        app.orders.remove(app.currentOrder)
        app.kitchenImageList = []
        app.finalImageList = []
        for order in app.orders:
            app.image3 = app.loadImage(order.getImage())
            app.image5 = app.scaleImage(app.image3, 1/10)
            app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
            app.image4 = app.scaleImage(app.image3, 1/3)
            app.kitchenImageList.append(app.image6)
            app.finalImageList.append(app.image4)
            app.foundImageIndex = 0
            app.imageX = 0
            app.imageY = 0
            app.foundImage = False
            app.movingPersonWidth = 0
        if len(app.orders)> 0:
            app.mode = 'sittingMode'
        else:
            if app.totalScore > 47:
                app.mode = 'youWonMode'
            else:
                o = Order()
                o2 = Order()
                o3 = Order()
                app.orders.append(o)
                app.orders.append(o2)
                app.orders.append(o3)
                o.setTotalSecond(120)
                o2.setTotalSecond(120)
                o3.setTotalSecond(120)

                
                app.kitchenImageList = []
                app.finalImageList = []
                for order in app.orders:
                    app.image3 = app.loadImage(order.getImage())
                    app.image5 = app.scaleImage(app.image3, 1/10)
                    app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
                    app.image4 = app.scaleImage(app.image3, 1/3)
                    app.kitchenImageList.append(app.image6)
                    app.finalImageList.append(app.image4)
                    app.foundImageIndex = 0
                    app.imageX = 0
                    app.imageY = 0
                    app.foundImage = False
                    app.movingPersonWidth = 0
                app.mode = 'sittingMode'






#takes user to either new level mode if they want to keep playing or game over mode if they dont wish to continue playing
def youWonMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height/2-20, text='YOU WIN!',
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2+20, text=f'Total Score: {app.totalScore}',
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2 + app.height/10, text = 'Play again?', font = 'Arial 15 bold', fill = 'black')

    #yes
    canvas.create_rectangle(app.width/2-95, app.height*2/3, app.width/2-20, (app.height*2/3)+40, fill = 'light blue', activefill = '#54a8e8')
    x0 = app.width/2-95
    x1 = app.width/2-20
    y0 = app.height*2/3
    y1 = (app.height*2/3)+40
    canvas.create_text((x0+x1)/2, (y0+y1)/2, text = 'Yes', font = 'Helvetica 20 bold', fill = 'black')

    #no
    canvas.create_rectangle(app.width/2+20, app.height*2/3, app.width/2+95, (app.height*2/3)+40, fill = 'light blue', activefill = '#54a8e8')
    a0 = app.width/2+20
    a1 = app.width/2+95
    b0 = app.height*2/3
    b1 = (app.height*2/3)+40
    canvas.create_text((a0+a1)/2, (b0+b1)/2, text = 'No', font = 'Helvetica 20 bold', fill = 'black')


def yesButtonClickedInBox(app, x, y, boxNum):
    return (app.width/2-95 <= x <= app.width/2-20 and app.height*2/3 <= y <= (app.height*2/3)+40)

def noButtonClickedInBox(app, x, y, boxNum):
    return (app.width/2+20 <= x<= app.width/2+95 and app.height*2/3 <= y <= (app.height*2/3)+40)


def youWonMode_mousePressed(app, event):
    if yesButtonClickedInBox(app, event.x, event.y, 0):
        app.level+=1 
        app.mode = 'nextLevelMode'
    else:
        app.mode = 'gameOver'

def nextLevelMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')

    canvas.create_rectangle(app.width/2-40, app.height/2-40, app.width/2+40, app.height/2+40, fill = 'light blue', activefill = '#54a8e8')
    x0 = app.width/2-40
    x1 = app.width/2+40
    y0 = app.height/2-40
    y1 = app.height/2+40
    canvas.create_text((x0+x1)/2, (y0+y1)/2, text = 'Next Level', font = 'Helvetica 18 bold', fill = 'black')


def nextLevelClickedInBox(app, x, y, boxNum):
    return (app.width/2-40 <= x <= app.width/2+40 and app.height/2-40 <= y <= app.height/2+40)

#randomly generates orders in higher levels and resets global variable values
#changes alloted time for higher levels
def nextLevelMode_mousePressed(app, event):
    # sets mode to erasing/not erasing based on box clicked
    if nextLevelClickedInBox(app, event.x, event.y, 0):
        if app.level == 2:
            orderFour = Order()
            orderFive = Order()
            orderSix = Order()
            orderSeven = Order()
            app.orders = [orderFour, orderFive, orderSix, orderSeven]
            app.kitchenImageList = []
            app.finalImageList = []
            for order in app.orders:
                app.image3 = app.loadImage(order.getImage())
                app.image5 = app.scaleImage(app.image3, 1/10)
                app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
                app.image4 = app.scaleImage(app.image3, 1/3)
                app.kitchenImageList.append(app.image6)
                app.finalImageList.append(app.image4)
            app.foundImageIndex = 0
            app.imageX = 0
            app.imageY = 0
            app.foundImage = False
            app.totalSeconds = 180
            app.totalScore = 0
            app.mode = 'sittingMode'
            app.movingPersonWidth = 0
        elif app.level == 3:
            orderEight = Order()
            orderNine= Order()
            orderTen = Order()
            orderEleven = Order()
            orderTwelve = Order()
            app.orders = [orderEight, orderNine, orderTen, orderEleven, orderTwelve]
            app.kitchenImageList = []
            app.finalImageList = []
            for order in app.orders:
                app.image3 = app.loadImage(order.getImage())
                app.image5 = app.scaleImage(app.image3, 1/10)
                app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
                app.image4 = app.scaleImage(app.image3, 1/3)
                app.kitchenImageList.append(app.image6)
                app.finalImageList.append(app.image4)
            app.foundImageIndex = 0
            app.imageX = 0
            app.imageY = 0
            app.foundImage = False
            app.totalSeconds = 120
            app.totalScore = 0
            app.mode = 'sittingMode'
            app.movingPersonWidth = 0

        else:
            if app.level > 3:
                app.mode = 'gameFinished'

#final congratulations screen
#displays this screen after three levels are completed
def gameFinished_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.endTextPosition, app.height/2, text='Congrats! You finished the game',
                       fill='firebrick3', font='Helvetica 26 bold ')



def gameFinished_timerFired(app):
    
    if app.endTextPosition<700:
        app.endTextPosition+=3
    else:
        app.endTextPosition = 0

def gameOver_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height/2, text='Game over',
                       font=font, fill='black')
    canvas.create_text(app.width/2, app.height/2+30, text=f'Score:{app.totalScore}',
                       font=font, fill='black')

      

# #happens if dont get full score or if runs out of time
def youLoseMode_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #sets background color
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'light pink')
    canvas.create_text(app.width/2, app.height/2, text='YOU LOSE!',
                       font=font, fill='black')





##########################################
# Main App
##########################################

def appStarted(app):
    #sets values
    app.mode = 'splashScreenMode'
    app.spritePhotoImages = loadAnimatedGif('giphy.gif')
    
    app.spriteCounter = 0
    app.spriteValue = 0
    
    # app.values = [1,2,3]
    # app.orders = [Order(app.values) for app.values in zip(app.values)]
    orderOne = Order()
    orderTwo = Order()
    orderThree = Order()
 
    app.orders = [orderOne, orderTwo, orderThree]
    app.currentOrder = orderOne

    app.kitchenImageList = []
    app.finalImageList = []
    for order in app.orders:
        app.image3 = app.loadImage(order.getImage())
        app.image5 = app.scaleImage(app.image3, 1/10)
        app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)
        app.image4 = app.scaleImage(app.image3, 1/3)
        app.kitchenImageList.append(app.image6)
        app.finalImageList.append(app.image4)
    app.foundImageIndex = 0
    app.imageX = 0
    app.imageY = 0
    app.foundImage = False
        

    #icecream sundae
    # app.image1 = app.loadImage('sundae.jpg')
    # app.image2 = app.scaleImage(app.image1, 1/5)
    
    app.gradient1 = app.loadImage('gradient.png')
    app.gradient2 = app.scaleImage(app.gradient1, 1/12.5)
    #url:https://www.icegif.com/ice-cream-13/

    # #image of all objects


    # app.image5 = app.scaleImage(app.image3, 1/10)
    # app.image6 = app.image5.transpose(Image.FLIP_LEFT_RIGHT)

    # app.movingPersonWidth = 0
    #url: https://dribbble.com/tags/milk_carton
    app.milkImage1 = app.loadImage('milkimage.png')
    app.milkImage2 = app.scaleImage(app.milkImage1, 1/35)

    #https://www.vectorstock.com/royalty-free-vector/milk-bottle-icon-vector-19399426
    app.milkJug1 = app.loadImage('milkjug.png')
    app.milkJug2 = app.scaleImage(app.milkJug1, 3/4)
    app.milkHeight = (app.height*5)/6
    
    app.color = 'white'
    app.sugarRadius = 1 
    # app.sugarClicked = 0
    app.sugarHeight = 0
    #https://favpng.com/png_view/cube-clip-art-sugar-cubes-png/UDBPWsSC
    app.sugarImage1 = app.loadImage('sugar.png')
    app.sugarImage2 = app.scaleImage(app.sugarImage1, 1/19)


    app.icecreamCone1 = app.loadImage('icecreamcone.png')
    app.icecreamCone2 = app.scaleImage(app.icecreamCone1, 1.5)

    app.icecreamCup1 = app.loadImage('icecreamcup.png')
    app.icecreamCup2 = app.scaleImage(app.icecreamCup1, 0.57)

    app.icecreamBowl1 = app.loadImage('icecreambowl.png')
    app.icecreamBowl2 = app.scaleImage(app.icecreamBowl1, 1/7)
    

    app.chocolateScoop1 = app.loadImage('chocolatescoop.png')
    app.chocolateScoop2 = app.scaleImage(app.chocolateScoop1, 1/2)
    #https://wikiclipart.com/ice-cream-scoop-clipart_28834/

    app.vanillaScoop1 = app.loadImage('vanillascoop.png')
    app.vanillaScoop2 = app.scaleImage(app.vanillaScoop1, 1/2)
    #https://wikiclipart.com/ice-cream-scoop-clipart/

    app.strawberryScoop1 = app.loadImage('strawberryscoop.png')
    app.strawberryScoop2 = app.scaleImage(app.strawberryScoop1, 1/2)
    #https://wikiclipart.com/ice-cream-scoop-clipart_28828/

    app.sittingSquare1 = app.loadImage('sittingsquare.png')
    app.sittingSquare2 = app.scaleImage(app.sittingSquare1, 1/4.5)

    app.sittingTable1 = app.loadImage('sittingtable.png')
    app.sittingTable2 = app.scaleImage(app.sittingTable1, 1/2)

    #https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.compliancesigns.com%2Fpd%2Fplace-order-here-left-arrow-sign-nhe-9740-blkonwht-information&psig=AOvVaw0r2kzsDWNW2x6lpuf1cb1g&ust=1670534506267000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCMCXz5C46PsCFQAAAAAdAAAAABAE
    app.orderHere1 = app.loadImage('orderhere.png')
    app.orderHere2 = app.scaleImage(app.orderHere1, 1/5)
    # app.help = False

    # app.flavor = random_flavor
    # app.actualFlavor = ''
    
    # #number of times milk button was pressed
    app.cupsOfMilk = app.currentOrder.getCupsOfMilk()
    # app.actualMilkPresses = 0
    # app.milkClicked = 0

    #TIMER
    app.totalSeconds = 180
    app.minute = app.totalSeconds//60
    app.second = app.totalSeconds%60
    
    app.timer = 0

    app.totalScore = 0

    app.orderBackground1 = app.loadImage('orderbackground.png')
    app.orderBackground2 = app.scaleImage(app.orderBackground1, 0.35)
    # #URL: https://creazilla.com/nodes/16185-scroll-clipart

    #https://www.vetrovero.com/store/p155/Purple_%26_Grey_Scribble_Bowl.html
    app.toppingsBowl1 = app.loadImage('toppingsbowl.png')
    app.toppingsBowl2 = app.scaleImage(app.toppingsBowl1, 1/5)
    app.toppingsBowl3 = app.loadImage('toppingsbowl.png')
    app.toppingsBowl4 = app.scaleImage(app.toppingsBowl3, 1/5)
    app.toppingsBowl5 = app.loadImage('toppingsbowl.png')
    app.toppingsBowl6 = app.scaleImage(app.toppingsBowl5, 1/5)

    #https://www.istockphoto.com/vector/single-red-cherry-with-stem-gm481026143-36756980
    app.cherry1 = app.loadImage('cherry.png')
    app.cherry2 = app.scaleImage(app.cherry1, 1/12)

    #https://flyclipart.com/oreo-cliparts-oreo-logo-png-107731
    app.oreo1 = app.loadImage('oreo.png')
    app.oreo2 = app.scaleImage(app.oreo1, 1/5)

    #https://www.vecteezy.com/free-vector/marshmallow
    app.marshmellow1 = app.loadImage('marshmellow.png')
    app.marshmellow2 = app.scaleImage(app.marshmellow1, 1/14)
    
    #https://www.shutterstock.com/image-vector/whipped-cream-aerosol-can-vector-illustration-1310799479
    app.whippedCream1 = app.loadImage('whippedcream.png')
    app.whippedCream2 = app.scaleImage(app.whippedCream1, 1/2)

    app.movingPersonWidth = 0
    app.imageWidth = app.width/(len(app.kitchenImageList)+1)
    app.level = 1

    app.milkHeight = app.height*5/6

    app.entryTextPosition = 0
    app.startButton = Button(300, app.height*3/4+75, 'firebrick3','firebrick2', 'firebrick3')
    app.endTextPosition = 0

    #https://www.kindpng.com/imgv/bwTJwh_28-collection-of-empty-glass-clipart-black-and/
    app.cookingCup1 = app.loadImage('cookingcup.png')
    app.cookingCup2 = app.scaleImage(app.cookingCup1, 1/11)

    #https://www.istockphoto.com/illustrations/happy-face
    app.happyFace1 = app.loadImage('happyface.png')
    app.happyFace2 = app.scaleImage(app.happyFace1, 1/5)

    #https://www.seekpng.com/ipng/u2q8a9u2r5w7o0w7_sad-faces-clip-art-sad-face-on-black/
    app.sadFace1 = app.loadImage('sadface.png')
    app.sadFace2 = app.scaleImage(app.sadFace1, 1/3)

runApp(width=600, height=500)