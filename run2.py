from easy import myRobot
from time import sleep

def run2def(b: myRobot):
  b.elore(1.8, 40, absWay=0)
  b.modulok(1.5, 100, 0, 0)
  b.elore(0.2, 40, absWay=-2)
  sleep(1)
  b.hatra(4, 50, absWay=-15)
  # b.balra(50, 50)
  # b.hatra(2, 50)
  # b.balra(100, 50)
  # b.justGo(10, 0.5)
  # b.balra(60, speed=40, prec=5)
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run2def(b)