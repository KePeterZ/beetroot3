from easy import myRobot
from time import sleep

def run4def(b: myRobot):
  b.resetMotors()
  b.gyroReset()
  # b.playSound("./mario.sh&")
  b.elore(2.8, 35)
  b.balra(70, speed=8, prec=2, log=False)
  b.elore(1.5, 20, end=True)
  b.hatra(0.05, 10, end=True)
  # b.hatra(0.1, 10, end=True)
  b.egyszerre(-100, 2)
  b.egyszerre(100, 1)
  b.hatra(0.2, 10, end=True)
  # b.egyszerre(-60, 8)
  # b.egyszerre(100, 4)
  b.jobbra(45, speed=4, prec=1)
  b.justGo(10, 1)
  # b.elore(1, 10, 3, absWay=15)
  b.fullStop(True)
  # while True: print(b.gs.value())
  # b.elore(0.5, 3, absWay=33)
  # sleep(2)
  # b.hatra(0.1, 5, end=True)
  # b.elore(0.3, 20, absWay=20)
  b.egyszerre(-50, 2)
  # b.egyszerre(50, 4)
  b.hatra(1.5, 40)
  b.justTurn(20, 0.4)
  b.hatra(3, 40)
  b.fullStop()
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run4def(b)