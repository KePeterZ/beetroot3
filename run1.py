from core import myRobot

def run1def(b: myRobot):
  b.goWithGyroRot2(3, -99, 3, True)
  b.fullStop()
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run1def(b)