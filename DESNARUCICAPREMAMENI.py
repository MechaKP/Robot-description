from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

hub = PrimeHub()

front_sensor = UltrasonicSensor(Port.F)
left_sensor = UltrasonicSensor(Port.A)
right_sensor = UltrasonicSensor(Port.B)

drive_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
steering_motor = Motor(Port.D)

drive_motor.run(200)

# Kalibracija volana
steering_motor.run_target(800, 0)

LAP_DEGREES = 9480
lap = 0

while lap < 3:

    front = front_sensor.distance()
    left = left_sensor.distance()
    right = right_sensor.distance()

    drive_motor.run(600)

    # zid ispred -> lijevo
    if front < 710:
        steering_motor.track_target(35)
        wait(35)
        steering_motor.track_target(0)
        drive_motor.run(600)

    # ako lijevi vidi zid -> desno
    elif right < 200:
        steering_motor.track_target(-10)
        wait(7)
        steering_motor.track_target(0)
        drive_motor.run(600)
    elif left < 400:
        steering_motor.track_target(24)

    # ako lijevi ne vidi zid -> lijevo
    else:
        steering_motor.track_target(0)
        drive_motor.run(600)

    # krugovi
    if abs(drive_motor.angle()) >= LAP_DEGREES:
        lap += 1
        print("Krug:", lap)
        drive_motor.reset_angle(0)

    wait(20)

drive_motor.stop()
steering_motor.run_target(200, 0)

print("Gotovo!")
