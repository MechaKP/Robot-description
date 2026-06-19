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
LAP_DEGREES = 10050
lap = 0
while lap < 3:

    front = front_sensor.distance()
    left = left_sensor.distance()
    right = right_sensor.distance()

    drive_motor.run(500)

    # zid ispred -> lijevo
    if front < 700:
        steering_motor.track_target(35)
        wait(100)
        steering_motor.track_target(0)
        drive_motor.run(800)

    # ako lijevi vidi zid -> desno
    elif left < 300:
        steering_motor.track_target(30)
        wait(40)
    elif right < 300:
        steering_motor.run_target(500, -30)
        wait(80)

    # ako lijevi ne vidi zid -> lijevo
    else:
        steering_motor.track_target(0)
        drive_motor.run(500)

    # krugovi
    if abs(drive_motor.angle()) >= LAP_DEGREES:
        lap += 1
        print("Krug:", lap)
        drive_motor.reset_angle(0)

    wait(20)

drive_motor.stop()
steering_motor.run_target(500, 0)

print("Gotovo!")
