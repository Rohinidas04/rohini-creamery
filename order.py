import copy
import random
#function randomly generates item from list
def pickRandom(list):
    num = len(list)
    randVal = random.randrange(num)
    randItem = list[randVal]
    return randItem

class Order:
    def __init__(self):
        #randomly choose values from lists
        self.image = pickRandom(['/Users/rohinidas/Documents/15112/tpfinalproject/characterlist/characterone.png', \
            '/Users/rohinidas/Documents/15112/tpfinalproject/characterlist/charactertwo.png', \
                '/Users/rohinidas/Documents/15112/tpfinalproject/characterlist/characterthree.png',\
                    '/Users/rohinidas/Documents/15112/tpfinalproject/characterlist/characterfour.png',\
                        '/Users/rohinidas/Documents/15112/tpfinalproject/characterlist/characterfive.png'])
        self.cupsOfMilk = pickRandom([1,2,3])
        self.flavor = pickRandom(['Chocolate','Vanilla','Strawberry'])
        self.spoonsOfSugar = pickRandom([1,2,3])
        self.cupOrCone = pickRandom(['Cone', 'Cup'])
        self.numOfScoops = pickRandom([1,2,3])
        self.isWhippedCream = pickRandom(['Yes', 'No'])

        #sets milk height to 0 by default
        self.milkHeight = 0
        if(self.isWhippedCream == 'Yes'):
            self.whippedCream = 'Whipped Cream'   
        else:
            self.whippedCream = 'No Whipped Cream'     

        if(self.whippedCream == 'Whipped Cream'):
            self.whippedCreamX = 267
            self.whippedCreamY = 375
        else:
            self.whippedCreamX = 0
            self.whippedCreamY = 0

        #used for creating sugar particles
        self.dots = []
        self.r = 4
        self.dotColor = 'white'
        self.whippedCreamMove = False
        self.cx = 0
        self.cy = 0

        #appends toppings to list
        self.toppings = []
        self.numberOfToppings = pickRandom([1,2,3])
        for i in range(self.numberOfToppings):
            topping = pickRandom(['Cherries', 'Oreos', 'Marshmellows'])
            if topping not in self.toppings:
                self.toppings.append(topping)


        self.milkClicked = 0
        self.sugarClicked = 0
        self.actualFlavor = ''
        self.color = 'white'
        self.actualColor = 'white'
        
        self.score = 0
        self.actualCupOrCone = ''
        self.actualScoopsClicked = 0


        #location of scoops
        self.firstScoopX = 150
        self.firstScoopY = 375-87
        self.secondScoopX = 150
        self.secondScoopY = 375 - 2*87
        self.thirdScoopX = 150
        self.thirdScoopY = 375-3*87

        self.firstScoopFinalLocX = 0
        self.firstScoopFinalLocY = 0
        self.secondScoopFinalLocX = 0
        self.secondScoopFinalLocY = 0
        self.thirdScoopFinalLocX = 0
        self.thirdScoopFinalLocY = 0

        self.firstScoopMove = False
        self.secondScoopMove = False
        self.thirdScoopMove = False

        #location of cherries
        self.firstCherryX = 104
        self.firstCherryY = 316
        self.secondCherryX = 150
        self.secondCherryY = 316
        self.thirdCherryX = 196
        self.thirdCherryY = 316

        self.firstCherryMove = False
        self.secondCherryMove = False
        self.thirdCherryMove = False

        #location of oreos
        self.firstOreoX = 104
        self.firstOreoY = 208
        self.secondOreoX = 150
        self.secondOreoY = 208
        self.thirdOreoX = 196
        self.thirdOreoY = 208



        self.firstOreoMove = False
        self.secondOreoMove = False
        self.thirdOreoMove = False

        #location of marshmellows
        self.firstMarshmellowX = 104
        self.firstMarshmellowY = 89
        self.secondMarshmellowX = 150
        self.secondMarshmellowY = 89
        self.thirdMarshmellowX = 196
        self.thirdMarshmellowY = 89

   

        self.firstMarshmellowMove = False
        self.secondMarshmellowMove = False
        self.thirdMarshmellowMove = False

        self.cherriesToppings = []
        self.oreosToppings = []
        self.marshmellowsToppings = []
        self.actualToppings = []

        self.movingPersonWidth = 0

        self.temporaryFlavorColor = 'white'
        self.moveHorizontal = 0


        self.isSliderMoving = True
        self.isSliderNegative = False

        self.sliderXOne = 180
        self.sliderXTwo = 190
        self.sliderVelocity = 0 

        self.batterPressHeight = 412
        self.face = ''
        self.totalSecond = 180
        self.timer = 0

    #all getter functions retrieve values of attribute
    #all setter functions set values of attribute
    #increment and decrement functionos also set values of attribute
    
    def getToppings(self):
        return self.toppings

    def getCupsOfMilk(self):
        return self.cupsOfMilk

    def getSpoonsOfSugar(self):
        return self.spoonsOfSugar

    def getImage(self):
        return self.image

    def getFlavor(self):
        return self.flavor

    def getColor(self):
        return self.color

    def getCupOrCone(self):
        return self.cupOrCone

 
    #increment or decrement milk clicked
    def incrementMilkClicked(self):
        self.milkClicked+=1
        return None

    def decrementMilkClicked(self):
        self.milkClicked-=1
        return None


    #returns actual number of times milk was clicked
    def getActualMilkPresses(self):
        return self.milkClicked


    def incrementSugarClicked(self):
        self.sugarClicked+=1
        return None

    def decrementSugarClicked(self):
        self.sugarClicked-=1
        return None


    def getActualSugarPresses(self):
        return self.sugarClicked

    def setActualFlavor(self, actualFlavor):
        self.actualFlavor = actualFlavor
        return None

    def getActualFlavor(self):
        return self.actualFlavor


    def setActualColor(self, actualColor):
        self.actualColor = actualColor
        return None

    def getActualColor(self):
        return self.actualColor


    def incrementScore(self):
        self.score+=1

    def getScore(self):
        return self.score

    def setActualCupOrCone(self, actualCupOrCone):
        self.actualCupOrCone = actualCupOrCone
        return None

    def getActualCupOrCone(self):
        return self.actualCupOrCone

    def getNumOfScoops(self):
        return self.numOfScoops



    def getFirstScoopX(self):
        return self.firstScoopX

    def setFirstScoopX(self, firstX):
        self.firstScoopX = firstX
        return None
    
    def getFirstScoopY(self):
        return self.firstScoopY

    def setFirstScoopY(self, firstY):
        self.firstScoopY = firstY
        return None

    def getSecondScoopX(self):
        return self.secondScoopX

    def setSecondScoopX(self, secondX):
        self.secondScoopX = secondX
        return None
    
    def getSecondScoopY(self):
        return self.secondScoopY

    def setSecondScoopY(self, secondY):
        self.secondScoopY = secondY
        return None

    def getThirdScoopX(self):
        return self.thirdScoopX

    def setThirdScoopX(self, thirdX):
        self.thirdScoopX = thirdX
        return None
    
    def getThirdScoopY(self):
        return self.thirdScoopY

    def setThirdScoopY(self, thirdY):
        self.thirdScoopY = thirdY
        return None


    def getFirstScoopFinalLocX(self):
        return self.firstScoopFinalLocX

    def setFirstScoopFinalLocX(self, firstXFinal):
        self.firstScoopFinalLocX = firstXFinal
        return None
    
    def getFirstScoopFinalLocY(self):
        return self.firstScoopFinalLocY

    def setFirstScoopFinalLocY(self, firstYFinal):
        self.firstScoopFinalLocY = firstYFinal
        return None

    def getSecondScoopFinalLocX(self):
        return self.secondScoopFinalLocX

    def setSecondScoopFinalLocX(self, secondXFinal):
        self.secondScoopFinalLocX = secondXFinal
        return None
    
    def getSecondScoopFinalLocY(self):
        return self.secondScoopFinalLocY

    def setSecondScoopFinalLocY(self, secondYFinal):
        self.secondScoopFinalLocY = secondYFinal
        return None

    def getThirdScoopFinalLocX(self):
        return self.thirdScoopFinalLocX

    def setThirdScoopFinalLocX(self, thirdXFinal):
        self.thirdScoopFinalLocX = thirdXFinal
        return None
    
    def getThirdScoopFinalLocY(self):
        return self.thirdScoopFinalLocY

    def setThirdScoopFinalLocY(self, thirdYFinal):
        self.thirdScoopFinalLocY = thirdYFinal
        return None


    def getFirstScoopMove(self):
        return self.firstScoopMove

    def setFirstScoopMove(self, firstMove):
        self.firstScoopMove = firstMove

    def getSecondScoopMove(self):
        return self.secondScoopMove

    def setSecondScoopMove(self, secondMove):
        self.secondScoopMove = secondMove

    def getThirdScoopMove(self):
        return self.thirdScoopMove

    def setThirdScoopMove(self, thirdMove):
        self.thirdScoopMove = thirdMove


    def incrementScoopsClicked(self):
        self.actualScoopsClicked+=1
        return None


    def getActualScoopsPresses(self):
        return self.actualScoopsClicked




    def getFirstCherryX(self):
        return self.firstCherryX

    def setFirstCherryX(self, firstCherryX):
        self.firstCherryX = firstCherryX
        return None

    def getFirstCherryY(self):
        return self.firstCherryY

    def setFirstCherryY(self, firstCherryY):
        self.firstCherryY = firstCherryY
        return None

    def getSecondCherryX(self):
        return self.secondCherryX

    def setSecondCherryX(self, secondCherryX):
        self.secondCherryX = secondCherryX
        return None

    def getSecondCherryY(self):
        return self.secondCherryY

    def setSecondCherryY(self, secondCherryY):
        self.secondCherryY = secondCherryY
        return None

    def getThirdCherryX(self):
        return self.thirdCherryX

    def setThirdCherryX(self, thirdCherryX):
        self.thirdCherryX = thirdCherryX
        return None

    def getThirdCherryY(self):
        return self.thirdCherryY

    def setThirdCherryY(self, thirdCherryY):
        self.thirdCherryY = thirdCherryY
        return None



    def getFirstOreoX(self):
        return self.firstOreoX

    def setFirstOreoX(self, firstOreoX):
        self.firstOreoX = firstOreoX
        return None

    def getFirstOreoY(self):
        return self.firstOreoY

    def setFirstOreoY(self, firstOreoY):
        self.firstOreoY = firstOreoY
        return None

    def getSecondOreoX(self):
        return self.secondOreoX

    def setSecondOreoX(self, secondOreoX):
        self.secondOreoX = secondOreoX
        return None

    def getSecondOreoY(self):
        return self.secondOreoY

    def setSecondOreoY(self, secondOreoY):
        self.secondOreoY = secondOreoY
        return None

    def getThirdOreoX(self):
        return self.thirdOreoX

    def setThirdOreoX(self, thirdOreoX):
        self.thirdOreoX = thirdOreoX
        return None

    def getThirdOreoY(self):
        return self.thirdOreoY

    def setThirdOreoY(self, thirdOreoY):
        self.thirdOreoY = thirdOreoY
        return None


    def getFirstMarshmellowX(self):
        return self.firstMarshmellowX

    def setFirstMarshmellowX(self, firstMarshmellowX):
        self.firstMarshmellowX = firstMarshmellowX
        return None

    def getFirstMarshmellowY(self):
        return self.firstMarshmellowY

    def setFirstMarshmellowY(self, firstMarshmellowY):
        self.firstMarshmellowY = firstMarshmellowY
        return None

    def getSecondMarshmellowX(self):
        return self.secondMarshmellowX

    def setSecondMarshmellowX(self, secondMarshmellowX):
        self.secondMarshmellowX = secondMarshmellowX
        return None

    def getSecondMarshmellowY(self):
        return self.secondMarshmellowY

    def setSecondMarshmellowY(self, secondMarshmellowY):
        self.secondMarshmellowY = secondMarshmellowY
        return None

    def getThirdMarshmellowX(self):
        return self.thirdMarshmellowX

    def setThirdMarshmellowX(self, thirdMarshmellowX):
        self.thirdMarshmellowX = thirdMarshmellowX
        return None

    def getThirdMarshmellowY(self):
        return self.thirdMarshmellowY

    def setThirdMarshmellowY(self, thirdMarshmellowY):
        self.thirdMarshmellowY = thirdMarshmellowY
        return None

    def getFirstCherryMove(self):
        return self.firstCherryMove

    def setFirstCherryMove(self, firstCherryMove):
        self.firstCherryMove = firstCherryMove
        return None

    def getSecondCherryMove(self):
        return self.secondCherryMove

    def setSecondCherryMove(self, secondCherryMove):
        self.secondCherryMove = secondCherryMove
        return None

    def getThirdCherryMove(self):
        return self.thirdCherryMove

    def setThirdCherryMove(self, thirdCherryMove):
        self.thirdCherryMove = thirdCherryMove
        return None



    def getFirstOreoMove(self):
        return self.firstOreoMove

    def setFirstOreoMove(self, firstOreoMove):
        self.firstOreoMove = firstOreoMove
        return None

    def getSecondOreoMove(self):
        return self.secondOreoMove

    def setSecondOreoMove(self, secondOreoMove):
        self.secondOreoMove = secondOreoMove
        return None

    def getThirdOreoMove(self):
        return self.thirdOreoMove

    def setThirdOreoMove(self, thirdOreoMove):
        self.thirdOreoMove = thirdOreoMove
        return None


    def getFirstMarshmellowMove(self):
        return self.firstMarshmellowMove

    def setFirstMarshmellowMove(self, firstMarshmellowMove):
        self.firstMarshmellowMove = firstMarshmellowMove
        return None

    def getSecondMarshmellowMove(self):
        return self.secondMarshmellowMove

    def setSecondMarshmellowMove(self, secondMarshmellowMove):
        self.secondMarshmellowMove = secondMarshmellowMove
        return None

    def getThirdMarshmellowMove(self):
        return self.thirdMarshmellowMove

    def setThirdMarshmellowMove(self, thirdMarshmellowMove):
        self.thirdMarshmellowMove = thirdMarshmellowMove
        return None


    def getCherriesToppings(self):
        return self.cherriesToppings

    def setCherriesToppings(self, cherryTopping):
        self.cherriesToppings.append(cherryTopping)
        return None

    def getOreosToppings(self):
        return self.oreosToppings

    def setOreosToppings(self, oreoTopping):
        self.oreosToppings.append(oreoTopping)
        return None

    def getMarshmellowsToppings(self):
        return self.marshmellowsToppings

    def setMarshmellowsToppings(self, marshmellowTopping):
        self.marshmellowsToppings.append(marshmellowTopping)
        return None

    def getActualToppings(self):
        return self.actualToppings

    def setActualToppings(self, actualTopping):
        self.actualToppings.append(actualTopping)
        return None



 
            
        


    def getWhippedCream(self):
        return self.whippedCream
    
    def getWhippedCreamX(self):
        return self.whippedCreamX
    
    def setWhippedCreamX(self, whippedCreamX):
        self.whippedCreamX = whippedCreamX
        return None

    def getWhippedCreamY(self):
        return self.whippedCreamY

    def setWhippedCreamY(self, whippedCreamY):
        self.whippedCreamY = whippedCreamY
        return None
    
    def getWhippedCreamR(self):
        return self.r
    
    def getWhippedCreamColor(self):
        return self.dotColor

    def getWhippedCreamMove(self):
        return self.whippedCreamMove
        
    def setWhippedCreamMove(self, whippedCreamMove):
        self.whippedCreamMove = whippedCreamMove
        return None

    def getDots(self):
        return self.dots

    def getcx(self):
        return self.cx

    def getcy(self):
        return self.cy

    def setcx(self, cxvalue):
        self.cx = cxvalue
        return None

    def setcy(self, cyvalue):
        self.cy = cyvalue
        return None

    def setDots(self, cx, cy, r, color):
        dot = cx, cy, r, color
        self.dots.append(dot)
        return None
    
    def getMovingPersonWidth(self):
        return self.movingPersonWidth

    def setMovingPersonWidth(self, value):
        self.movingPersonWidth+=value   
        return None

    def getMilkHeight(self):
        return self.milkHeight

    def setMilkHeight(self, milkValue):
        self.milkHeight = milkValue
        return None

    def getTemporaryFlavorColor(self):
        return self.temporaryFlavorColor

    def setTemporaryFlavorColor(self, color):
        self.temporaryFlavorColor = color
        return None

    def getMoveHorizontal(self):
        return self.moveHorizontal

    def setMoveHorizontal(self, x):
        self.moveHorizontal+=x
        return None






    def getIsSliderMoving(self):
        return self.isSliderMoving

    def setIsSliderMoving(self, changeSlider):
        self.isSliderMoving = changeSlider
        return None

    def getIsSliderNegative(self):
        return self.isSliderNegative

    def setIsSliderNegative(self, changeNegative):
        self.isSliderNegative = changeNegative
        return None




    def getSliderVelocity(self):
        return self.sliderVelocity

    def setSliderVelocityIncrement(self, value):
        self.sliderVelocity+=value
        return None

    def setSliderVelocityDecrement(self, value):
        self.sliderVelocity-=value
        return None
        

    def getSliderXOne(self):
        return self.sliderXOne

    def setSliderXOneIncrement(self, value):
        self.sliderXOne+=value
        return None

    def setSliderXOneDecrement(self, value):
        self.sliderXOne-=value
        return None

    def getSliderXTwo(self):
        return self.sliderXTwo

    def setSliderXTwoIncrement(self, value):
        self.sliderXTwo+=value
        return None

    def setSliderXTwoDecrement(self, value):
        self.sliderXTwo-=value
        return None

    def getBatterPressHeight(self):
        return self.batterPressHeight

    def setBatterPressHeight(self, value):
        self.batterPressHeight = value
        return None

    def decrementBatterPressHeight(self, value):
        self.batterPressHeight-=value
        return None

    def getFace(self):
        return self.face

    def setFace(self, emotion):
        self.face = emotion
        return None

    def getTotalSecond(self):
        return self.totalSecond

    def setTotalSecond(self, value):
        self.totalSecond = value

    def getTimer(self):
        return self.timer

    def incrementTimer(self, value):
        self.timer+=value

