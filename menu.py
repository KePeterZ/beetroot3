#!/usr/bin/env micropython

# Start by importing the core library
from easy import myRobot
b = myRobot("outB", "outC", "outD", "in4", None, "in3", None, 1, moduleSensor="in4", modulePort2="outA")

# Import misc. libraries
import sys, time

files = ["run1", "run2", "run4", "run6", "run5"]

count = 0
while True:
  run = files[count]
  input("Press enter when ready..")
  try: exec(removeStatement)
  except: pass
  importStatement = "from " + files[count] + " import " + files[count]+"def"
  exec(importStatement)
  removeStatement = "del sys.modules['" + files[count] + "']"
  try:
    b.prepareForRun()
    b.gyroReset()
    exec(run+"def(b)")
  except KeyboardInterrupt:
    pass
  count += 1
  b.fullStop(False)