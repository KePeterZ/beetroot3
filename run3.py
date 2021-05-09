from easy import myRobot
from time import sleep

def run3def(b: myRobot):
  b.elore(1.3, 40)
  b.balra(45, prec=2)
  b.elore(1.15, 40)
  b.balra(130, prec=3, log=False)
  b.elore(2, 30, absWay=130)
  # b.modulok(1, 100, 0, 0)
  b.elore(1, 20, absWay=130, end=True)
  b.modulok(1, -100, 0, 0)
  b.hatra(1, 30)
  b.balra(180)
  b.elore(4)
  b.fullStop(True)
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run3def(b)