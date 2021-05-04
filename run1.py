from easy import myRobot

def run1def(b: myRobot):
  # b.elore()
  # b.hatra()
  # b.jobbra()
  # b.balra()
  b.modulok(1, -50, 0.5, -100)
  b.egyszerre(20, 5)
  b.egyszerre(-20, 5)
  b.fullStop(False)
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run1def(b)