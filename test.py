from cmu_112_graphics import *

def appStarted(app):
    app.circleCenters = [ ]

def mousePressed(app, event):
    newCircleCenter = (event.x, event.y)
    app.circleCenters.append(newCircleCenter)

def keyPressed(app, event):
    if (event.key == 'd'):
        if (len(app.circleCenters) > 0):
            app.circleCenters.pop(0)
        else:
            print('No more circles to delete!')

def redrawAll(app, canvas):
    # draw the circles
    for circleCenter in app.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill='cyan')
    # draw the text
    canvas.create_text(app.width/2, 20,
                       text='Example: Adding and Deleting Shapes', fill='black')
    canvas.create_text(app.width/2, 40,
                       text='Mouse clicks create circles', fill='black')
    canvas.create_text(app.width/2, 60,
                       text='Pressing "d" deletes circles', fill='black')

runApp(width=400, height=400)