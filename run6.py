from easy import myRobot

def run6def(b: myRobot):
  b.elore(2, 50, 1.5, absWay=6)
  b.elore(1, 30)
  b.fullStop()
  b.sleep(1) # Uncheck if necessary
  b.hatra(0.5, 20)
  b.elore(1, 20, end=True)
  b.modulok(1, 30, 0, 0)
  b.hatra(2, 50)
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run6def(b)