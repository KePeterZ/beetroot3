from easy import myRobot
from time import sleep

def run3def(b: myRobot):
  b.elore(0.9, 30)
  b.jobbra(-60, 15)
  b.fullStop(True)
  sleep(0.5)
  b.resetMotors()
  b.elore(1, 100)

  b.fullStop(True)
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run3def(b)