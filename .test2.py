from easy import myRobot

def test2def(b: myRobot):
  b.egyszerre(-100, 10)

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  test2def(b)