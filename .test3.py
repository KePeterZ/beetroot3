from easy import myRobot

def test3def(b: myRobot):
  b.modulok(1, 100, 0, 0)

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  test3def(b)