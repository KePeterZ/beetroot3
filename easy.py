#!/usr/bin/env micropython
import ev3dev2
from ev3dev2.motor import MoveSteering, LargeMotor, MoveTank, Motor
# from ev3dev2.motor import *
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, InfraredSensor
from ev3dev2.sensor import *
from ev3dev2.led import *
from ev3dev2.button import Button
from ev3dev2.console import Console
import time, sys, os

def isPositive(num):
  if num > 0:
    return 1
  else:
    return -1

class myRobot():
    def __init__(self, motorPort1, motorPort2, modulePort, colorPort1, colorPort2, gyro1=None, gyro2=None, motorDiff=1, colMode="COL-COLOR", moduleSensor=None, printErrors=True, enableConsole=False, modulePort2=None):
        if motorPort1 and motorPort2: self.ms = MoveSteering(motorPort1, motorPort2) # If defined in parameters, define MoveSteering
        if motorPort1 and motorPort2: self.mt = MoveTank(motorPort1, motorPort2)# If defined in parameters, define MoveTank
        if motorPort1: self.m1 = LargeMotor(motorPort1) # If defined in parameters, define Left Motor
        if motorPort2: self.m2 = LargeMotor(motorPort2) # If defined in parameters, define Right Motor
        if modulePort: self.mmt = Motor(modulePort); # If defined in parameters, define module motor
        if modulePort2: self.mmt2 = Motor(modulePort2); # If defined in parameters, define module motor
        if enableConsole: self.resetMotors()
        if colorPort1 != None: # If defined in parameters, define Left Color sensor
            self.csLeft = ColorSensor(colorPort1)
            self.csLeft.mode = colMode # Set color mode to the one in the parameters
        if colorPort2 != None: # If defined in parameters, define Right Color sensor
            self.csRight = ColorSensor(colorPort2)
            self.csRight.mode = colMode # Set color mode to the one in the parameters
        if moduleSensor != None: # If defined in parameters, define module sensor
            self.moduleSensor = ColorSensor(moduleSensor)
            self.moduleSensor.mode = "COL-COLOR"
        try: self.gs = GyroSensor(gyro1); self.gs.mode = "GYRO-RATE"; self.gs.mode = "GYRO-ANG"
        except: print("Gyro 1 can't be defined!") # Define gyro if possible, otherwise show error
        try: self.gs2 = GyroSensor(gyro2); self.gs2.mode = "GYRO-RATE"; self.gs2.mode = "TILT-ANG"
        except: print("Gyro 2 can't be defined!")# Define gyro if possible, otherwise show error
        self.using2ndGyro = False # Set default gyro to the 1st one
        self.motorDiff = motorDiff # Set motor difference to the one defined
        self.leds = Leds() # Setup brick leds
        self.bt = Button() # Setup brick buttons
        if enableConsole: self.console = Console(font="Lat15-Terminus32x16") # Enable console access if needed
        try: 
            with open("/home/robot/sappers2/pid.txt", "w") as pid: pid.write(str(os.getpid()))
        except: pass # Write PID into file for other applications.
        if printErrors: print("Successfully Initialized. ")
        self.timerStart = time.time()

    def elore(self, rots=1, speed=50, adj=2, absWay=None, end=None):
        pastGyro = self.gs.value() if absWay == None else absWay
        currentRot = (self.m1.position+self.m1.position)/2
        steerDiff = -1 if speed < 0 else 1
        startTime = time.time()
        while abs((currentRot - (self.m1.position+self.m2.position)/2)/360) < rots:
            if True: print(int(abs((currentRot - self.m1.position)/360)*100)/100, self.gs.value())
            self.ms.on((self.gs.value()-pastGyro)*adj*steerDiff, speed*self.motorDiff)
            pass
        if end: self.ms.off(brake=True)

    def hatra(self, rots=1, speed=50, adj=2, absWay=None, end=None):
        pastGyro = self.gs.value() if absWay == None else absWay
        currentRot = (self.m1.position+self.m1.position)/2
        speed = speed*-1
        steerDiff = -1 if speed < 0 else 1
        startTime = time.time()
        while abs((currentRot - (self.m1.position+self.m2.position)/2)/360) < rots:
            if True: print(int(abs((currentRot - self.m1.position)/360)*100)/100, self.gs.value())
            self.ms.on((self.gs.value()-pastGyro)*adj*steerDiff, speed*self.motorDiff)
            pass
        if end: self.ms.off(brake=True)
    
    def balra(self, deg=90, speed=10, prec=1, log=True):
      self.ms.on(-90, speed*self.motorDiff)
      # while (self.gs.value() > deg+prec  or self.gs.value() < deg-prec):
      while (self.gs.value() != deg):
          if log: print(self.gs.value())
          pass
    
    def jobbra(self, deg=-90, speed=10, prec=1, log=True):
      self.ms.on(90, speed*self.motorDiff)
      # while (self.gs.value() > deg+prec  or self.gs.value() < deg-prec):
      while (self.gs.value() != deg):
          if log: print(self.gs.value())
          pass

    def modulok(self, lAmount, lSpeed, rAmount, rSpeed):
      if(rAmount > lAmount):
        self.mmt.on_for_seconds(lSpeed, lAmount, block=False)
        self.mmt2.on_for_seconds(rSpeed, rAmount)
      else:
        self.mmt2.on_for_seconds(rSpeed, rAmount, block=False)
        self.mmt.on_for_seconds(lSpeed, lAmount)

    def egyszerre(self, speed, amount):
      self.mmt2.on_for_seconds(speed, amount, block=False)
      self.mmt.on_for_seconds(speed*-1, amount)  

    def prepareForRun(self): # Reset gyro and motors
        self.ms.reset()
        self.gyroReset()

    def changeGyro(self, newGyroPort): # Change gyro to 2nd one
        try: self.gs = GyroSensor(newGyroPort); self.using2ndGyro = True
        except: print("Can't change Gyro!")

    def attachNew(self, isMotor=True, port="outA", largeMotor=False): # Attach new motor
        if isMotor:
            self.m3 = Motor(port)
        else:
            self.m3 = LargeMotor(port)

    def followLine(self, timeOfGoing, speed, multiplier=5, debug=False): # Simple line follower
        currentTime = time.time()
        while time.time() - currentTime < timeOfGoing:
            colorLeft = int(self.csLeft.value()/1)
            colorRight = int(self.csRight.value()/1)
            print(colorLeft, colorRight)
            if colorLeft != 6 and colorRight != 6:
                tempSteering = 0
            elif colorLeft != 6:
                tempSteering = -multiplier
            elif colorRight != 6:
                tempSteering = multiplier
            else:
                tempSteering = 0
            self.ms.on(tempSteering, speed*self.motorDiff)
    
    def goByWay(self, waySteering, timeToGo, speed=80, debug=False): # MoveSteering but for time
        currentTime = time.time()
        while time.time() - currentTime < timeToGo:
            self.ms.on(waySteering, speed*self.motorDiff)

    def goUntilLine(self, speed, lineColor, multiplier=1, debug=False): # Goes forward with gyro, but stops when detecting line
        pastGyro = self.gs.value()
        while (self.csLeft.value() not in lineColor) and (self.csRight.value() not in lineColor):
            self.ms.on((self.gs.value()-pastGyro)*multiplier, speed*self.motorDiff)
            if debug: print(self.gs.value(), self.csLeft.value(), self.csRight.value())
        print(self.gs.value(), self.csLeft.value(), self.csRight.value())

    def goWithGyro(self, timeToGo, speed=70, multiplier=2, debug=False): 
        # Forward with gyro for time
        pastGyro = self.gs.value()
        currentTime = time.time()
        while time.time() - currentTime < timeToGo:
            self.ms.on(self.max100((self.gs.value()-pastGyro)*multiplier), speed*self.motorDiff)
            if debug: print(self.gs.value())

    def moveModule(self, length, speed=30, stopMoving=True, useLarge=False, waitAfter=False): # Module motor access
        if useLarge: 
            try:
                self.m3.on(speed)
                time.sleep(length)
                if stopMoving: self.m3.reset()
            except: 
                print("not working bruh you should fix it like rn")
        else:
            while True:
                try:
                    self.mmt.on(speed*-1)
                    time.sleep(length)
                    if stopMoving: self.mmt.reset()
                    if waitAfter: time.sleep(waitAfter)
                    break
                except Exception as e:
                    print(e)
                    break

    def moveModuleByRot(self, rotations, speed, block=True): # Deprecated module moving
        self.mmt.on_for_rotations(-speed, rotations, block=block)

    def moveModuleByRot2(self, rotations, speed, block=True): # Deprecated module moving
        self.mmt.on_for_rotations(-speed, rotations, block=block)

    def moveBothModules(self, rotations, speed, block=True, speed2=False): # Deprecated module moving
        self.mmt.on_for_rotations(-speed, rotations, block=False)
        self.mmt2.on_for_rotations((speed2 if speed2 else -speed), rotations, block=block)


    def resetMotors(self): # Motor reset
        self.ms.reset()
        self.mmt.on(100)
        time.sleep(1)
        self.mmt.reset()

    def gyroReset(self): # Gyro reset
        self.gs.mode = "GYRO-RATE"; self.gs.mode = "GYRO-ANG"
        try: self.gs2.mode = "GYRO-RATE"; self.gs2.mode = "TILT-ANG"
        except: print("Gyro2 not found!")

    def resetGyro(self, gyroObject, desiredMode="TILT-ANG"):
        gyroObject.mode = "GYRO-RATE"
        gyroObject.mode = desiredMode
    
    def fullStop(self, brakeOrNo=True): # Stops the robot, breaks if defined.
        self.ms.stop(brake=brakeOrNo)
        self.mmt.reset()
        try: self.mmt2.reset()
        except: pass
    
    def turnWithGyro(self, degreesToTurn=90, speedToTurnAt=20): # Turns with gyro, and saves past value
        gyroPast = self.gs.value()
        self.ms.on(90, speedToTurnAt)
        while gyroPast - self.gs.value() <= degreesToTurn:
            print(gyroPast - self.gs.value())
        self.ms.stop(brake=True)
        print(self.gs.value())
    
    def justGo(self, speed, timeOfGoing): # Goes forward without gyro, for time
        self.ms.on(0, speed*self.motorDiff)
        time.sleep(timeOfGoing)
    
    def justTurn(self, speed, timeOfGoing): # Turns withot gyro, useful for quick turns.
        self.ms.on(90, speed*self.motorDiff)
        time.sleep(timeOfGoing)
    
    def absoluteTurn(self, speed, absoluteLoc, rotWay=-1, giveOrTake=1, debug=False, ver2=False): # Turns using absolute value from gyro
        self.ms.on(90*rotWay, speed*self.motorDiff)
        # while self.gs.value() > absoluteLoc+giveOrTake  or self.gs.value() < absoluteLoc+giveOrTake :
        #     if debug: print(self.gs.value())
        #     pass
        while self.gs.value() > absoluteLoc+giveOrTake  or self.gs.value() < absoluteLoc-giveOrTake :
            if debug: print(self.gs.value())
            pass

    def isPositive(self, number):
        if number > 0:
            return 1
        elif number < 0:
            return -1
        else:
            return 0



    def absolute(self, speed, location, giveOrTake=2, debug=False):
        """
        Absolute turning
        """
        while self.gs.value() > location+giveOrTake  or self.gs.value() < location-giveOrTake:
            self.ms.on(90*self.isPositive(self.gs.value()-location), speed*self.motorDiff)
            if debug: print(self.gs.value())
            pass
    
    def turnForMore(self, speed, minDeg, rotWay=-1, debug=False, ver2=False): # Turns with gyro, but stops quicker than absolute turn (useful for big turns)
        if debug: print(self.gs.value())
        self.ms.on(90*rotWay, speed*self.motorDiff)
        if ver2:
            currentDeg = int(self.gs.value())
            while minDeg-1<=currentDeg<=minDeg+1:
                if debug: print(self.gs.value())
        else:
            if rotWay < 0:
                while int(self.gs.value()) < int(minDeg):
                    if debug: print(self.gs.value())
                    pass
            else:
                while int(self.gs.value()) > int(minDeg):
                    if debug: print(self.gs.value())
                    pass
    
    def goWithShift(self, timeToGo, speed=70, multiplier=2, shift=1): # Goes with gyro using shift
        pastGyro = self.gs.value()
        currentTime = time.time()
        while time.time() - currentTime < timeToGo:
            if self.gs.value() == 0:
                gsValue = shift
            else:
                gsValue = self.gs.value()
            self.ms.on((gsValue-pastGyro)*multiplier, speed*self.motorDiff)

    def goWithGyroRot(self, rotations, speed, multiplier, debug=False, startValue=None, stopAtEnd=False): # Goes using gyro using one motor's rotation value
        pastGyro = self.gs.value() if startValue == None else startValue
        currentRot = self.m1.position
        steerDiff = -1 if speed < 0 else 1
        while abs((currentRot - self.m1.position)/360) < rotations:
            if debug: print(int(abs((currentRot - self.m1.position)/360)*100)/100, self.gs.value())
            self.ms.on((self.gs.value()-pastGyro)*multiplier*steerDiff, speed*self.motorDiff)
        if stopAtEnd: self.ms.stop(brake=True)
    
    def waitForColor(self, color=[1,2,3,4,5,6], amountOfTime=0.5, debug=False, waitingTime=0.5): # Waits until color detected
        colorArray = []
        while True:
            if self.moduleSensor.value() in color:
                colorArray.append(self.moduleSensor.value())
                time.sleep(amountOfTime/10)
                if debug: print(colorArray, end="\r")
                self.leds.set_color("LEFT", "GREEN")
                self.leds.set_color("RIGHT", "GREEN")
            elif self.bt.down == True:
                print("awaiting input")
                return False
            else:
                colorArray = []
                if debug: print("waiting", self.moduleSensor.value(), end="\r")
                self.leds.set_color("LEFT", "RED")
                self.leds.set_color("RIGHT", "RED")
            if len(colorArray) == 9:
                break
        self.leds.set_color("LEFT", "ORANGE")
        self.leds.set_color("RIGHT", "AMBER")
        time.sleep(waitingTime)
        if debug: print(max(set(colorArray), key=colorArray.count), end="\n")
        return max(set(colorArray), key=colorArray.count)
    
    def turnWithGyro2(self, degreesToTurn=90, speedToTurnAt=20, debug=False): # Deprecated turn with gyro
        gyroPast = self.gs.value()
        while gyroPast - self.gs.value() <= degreesToTurn:
            self.ms.on(90, ((degreesToTurn - speedToTurnAt) + abs((degreesToTurn - speedToTurnAt))) / 2)
            if debug: print(gyroPast - self.gs.value())
    
    def startRun(self, toExec, resetGyro=True, colorArray=[3]): # Starts run using magic wand
        self.waitForColor([3], 1, True)
        self.gyroReset()
        exec(toExec)

    def gyroSlowLinearly(self, rotations, startSpeed, multiplier, minSpeed=5, debug=False, startValue=None, stopAtEnd=False): # Goes with gyro and slows down as it nears to destination
        pastGyro = self.gs.value() if startValue == None else startValue
        currentRot = self.m1.position
        steerDiff = -1 if startSpeed < 0 else 1
        while abs((currentRot - self.m1.position)/360) < rotations:
            currSpeed = 1-((int(abs((currentRot - self.m1.position)/360)*100)/100) / rotations)
            if debug: print(currSpeed, round((startSpeed*currSpeed+minSpeed)*self.motorDiff))
            self.ms.on((self.gs.value()-pastGyro)*multiplier*steerDiff, round((startSpeed*currSpeed+minSpeed)*self.motorDiff))
        if stopAtEnd: self.ms.stop(brake=True)
    
    def goWithGyroRot2(self, rotations, speed, multiplier, debug=False, startValue=None, stopAtEnd=False, timeout=100000): # Goes forward using both motor's rotation value
        pastGyro = self.gs.value() if startValue == None else startValue
        currentRot = (self.m1.position+self.m1.position)/2
        steerDiff = -1 if speed < 0 else 1
        startTime = time.time()
        while abs((currentRot - (self.m1.position+self.m1.position)/2)/360) < rotations or time.time()-startTime>=timeout:
            if debug: print(int(abs((currentRot - self.m1.position)/360)*100)/100, self.gs.value())
            self.ms.on((self.gs.value()-pastGyro)*multiplier*steerDiff, speed*self.motorDiff)
        if stopAtEnd: self.ms.stop(brake=True)

    def returnButtons(self, pack2=False): # Returns pressed buttons for menu
        if pack2:
            packable = list(sys.stdin.readline().replace("\x1b[", "").rstrip())
            return [ ''.join(x) for x in zip(packable[0::2], packable[1::2]) ]
        else:
            return sys.stdin.readline().replace("\x1b[", "").rstrip()

    def goWithGyroForLevel(self, startRots, speed, multiplier, debug=False, startValue=None, levelNeeded=5, overrideDegrees=0): # Goes forward with gyro until water-level is detected
        pastGyro = self.gs.value() if startValue == None else startValue
        currentRot = (self.m1.position+self.m1.position)/2
        steerDiff = -1 if speed < 0 else 1
        self.goWithGyroRot2(startRots, speed, multiplier, False, startValue, False)
        print(abs(self.gs2.value()))
        while abs(self.gs2.value()) > levelNeeded:
            if debug: print((abs(self.gs2.value()),  self.gs.value(), ((self.gs.value()-pastGyro)*multiplier*steerDiff)+overrideDegrees))
            self.ms.on(self.max100(((self.gs.value()-pastGyro)*multiplier*steerDiff)+overrideDegrees), speed*self.motorDiff)
    
    def playSound(self, mscCommand): # Plays a sound
        try: os.system(mscCommand)
        except: pass

    def max100(self, value): # Sets value to a max of 100
        if value > 100:
            return 100
        elif value < -100:
            return -100
        else:
            return value
        
    def sleep(self, seconds): # sleep.
        time.sleep(seconds)

    def stopAtLine(self, speed, color, correctionSpeed=5): # Goes forward and stops when detecting lines
        pastGyro = self.gs.value()
        while True:
            if self.csLeft.value() == color and self.csRight.value() == color:
                break
            elif self.csRight.value() != color and self.csLeft.value() == color:
                self.mt.on(0, correctionSpeed*self.motorDiff)
            elif self.csLeft.value() != color and self.csRight.value() == color:
                self.mt.on(correctionSpeed*self.motorDiff, 0)
            elif self.csLeft.value() != color and self.csRight.value() != color:
                self.ms.on((self.gs.value()-pastGyro), speed*self.motorDiff)
            print({"right": self.csRight.value(), "left": self.csLeft.value(), "gyro": self.gs.value()})
        print("final", {"right": self.csRight.value(), "left": self.csLeft.value(), "gyro": self.gs.value()})

    def stayInPlace(self, multiplier): # Using gyro and motor values, keeps the robot in place
        motor1 = self.m1.position
        motor2 = self.m2.position
        while True:
            corrig1 = -(self.m1.position - motor1)*multiplier
            corrig2 = -(self.m2.position - motor2)*multiplier
            if round(corrig1, 2) == 0 and round(corrig2, 2) == 0:
                self.mt.stop(brake=False)
            else:
                self.mt.on(corrig1, corrig2)
            print(corrig1, corrig2)
            
            # print(corrig1, corrig2)

    def moveModuleRepeating(self, raiseTime, downTime, speed1, speed2, iterations): # Module motor access
        for i in range(iterations):
            self.moveModule(raiseTime, speed1, False)
            self.moveModule(downTime, speed2, True)
    
    def section(self, sectionName, resetTimer=False):
        """
        Provides timing functionality, and makes it easier to see sections of runs in logs.
        
        `resetTimer` parameter optional, it will reset the main runTimer.
        """
        if resetTimer: self.timerStart = time.time(); print(sectionName)
        else: print("%s, current run time: %i" % (sectionName, self.timerStart-time.time()))
            
    def goWithGyroRot2Maxed(self, rotations, speed, multiplier, debug=False, startValue=None, stopAtEnd=False, timeout=100000): # Goes forward using both motor's rotation value
        pastGyro = self.gs.value() if startValue == None else startValue
        currentRot = (self.m1.position+self.m1.position)/2
        steerDiff = -1 if speed < 0 else 1
        startTime = time.time()
        while abs((currentRot - (self.m1.position+self.m1.position)/2)/360) < rotations or time.time()-startTime>=timeout:
            if debug: print(int(abs((currentRot - self.m1.position)/360)*100)/100, self.gs.value())
            self.ms.on(self.max100((self.gs.value()-pastGyro)*multiplier*steerDiff), speed*self.motorDiff)
        if stopAtEnd: self.ms.stop(brake=True)



if __name__ == "__main__":
    k = myRobot("outC", "outB", "outD", None, None, -1, moduleSensor="in1")
    print("Successful initialization.")