from easy import myRobot

def test1def(b: myRobot):
  while True:
    print(b.gs.value())
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  test1def(b)