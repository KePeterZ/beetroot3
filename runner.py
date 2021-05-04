#!/usr/bin/env micropython

# Start by importing the core library
from easy import myRobot
b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")

# Import misc. libraries
import sys, time

run = sys.argv[-1].strip()
importStatement = "from " + run + " import " + run+"def"
removeStatement = "del sys.modules['" + run + "']"
exec(importStatement)

while True:
  input("Press enter when ready..")
  exec(removeStatement)
  exec(importStatement)
  b.prepareForRun()
  try:
    exec(run+"def(b)")
  except KeyboardInterrupt:
    b.fullStop()