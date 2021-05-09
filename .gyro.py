from ev3dev2.sensor.lego import GyroSensor
g1 = GyroSensor("in3")
while True:
    print(g1.value())