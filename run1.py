from easy import myRobot

def run1def(b: myRobot):
  # b.elore()
  # b.hatra()
  # b.jobbra()
  # b.balra()
  b.elore(4.9, 80, 3, end=False, absWay=2)
  b.elore(0.8, 10, 3, end=True, absWay=0)
  # b.justGo(20, 0.5)
  # b.elore(0.2, 20, 5, end=True)
  # b.hatra(1, 30, 5, end=True)
  # b.modulok(0.5, 30, 0, 0)
  # b.elore(4, 45, 3, end=True, absWay=0)
  b.modulok(4, 100, 0, 0)
  b.hatra(0.5, 15, 2, 0)
  b.balra(20, speed=8, prec=2)

  b.elore(1.0, 20, absWay=18, end=True)
  b.modulok(0, 0, 1, 100)
  b.hatra(0.2, 5, end=True)
  b.jobbra(6, 10)
  b.hatra(0.5, 15, end=True)
  b.balra(25, 20)
  b.fullStop()
  b.modulok(0, 0, 1, -100)

  b.hatra(0.8, 20)
  b.jobbra(0, 10, prec=3)
  b.hatra(6, 75, absWay=0)
  # b.jobbra(-30)
  # b.hatra(4, 80)
  # b.elore(1.5, 15, end=True)
  # b.modulok(0, 0, 1, 100)
  # b.hatra(0.4, 20, end=True)
  # b.m1.on_for_seconds(10, 1, block=False)
  # b.m2.on_for_seconds(-100, 1)
  # b.modulok(0, 0, 1, -100)
  b.fullStop()
  pass

if __name__ == '__main__':
  b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")
  run1def(b)