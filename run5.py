from easy import myRobot
from time import sleep

def run5def(b: myRobot):
  b.elore(4, 60)
  for i in range(5):
    b.m1.reset()
    b.m2.reset()
    b.hatra(0.1)
    b.elore(0.6)
  b.hatra(0.2, 30, absWay=0)
  b.fullStop()
  b.balra(45, prec=2, log=False)
  b.fullStop()
  b.resetMotors()
  b.elore(0.2, 10)
  b.balra(95, prec=2, log=False)
  # b.jobbra(90, 5, prec=1, log=False)
  b.fullStop()
  b.elore(0.5, 25, absWay=90, end=True)
  b.modulok(0, 0, 1, 100)
  b.elore(2.2, 40, absWay=90, end=True)
  b.modulok(1, -100, 0, 0)
  b.hatra(0.5, 20)
  b.balra(135, speed=5, prec=3)
  b.elore(1.8, 30, absWay=135, end=True)
  # while True:
  b.modulok(0, 0, 0.5, -100)
  sleep(1)
  while True:
    b.modulok(0, 0, 0.5, 100)
    b.mt.on(20, -20)
    b.modulok(0, 0, 0.5, -100)
  b.playSound("./anthem.sh")
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run5def(b)