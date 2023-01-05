import copy
import random
from cmu_112_graphics import *

#creates button based on center x, center y, fill, activefill, and outline
class Button:
    def __init__(self, cx, cy, fill, activefill, outline):
        self.x0 = cx-50
        self.y0 = cy-25
        self.x1 = cx+50
        self.y1 = cy+25
        self.fill = fill
        self.activefill = activefill
        self.outline = outline

    #draws rectangular butotn with curved edges using rectangle and oval
    def drawButton(self, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.fill, activefill=self.activefill, outline=self.outline)
        canvas.create_oval(self.x1-10, self.y0, self.x1+10, self.y1, fill = self.fill, activefill = self.activefill, outline = self.outline)
        canvas.create_oval(self.x0-10, self.y0, self.x0+10, self.y1, fill = self.fill, activefill = self.activefill, outline = self.outline)


#    