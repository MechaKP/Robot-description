from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
front_sensor = UltrasonicSensor(Port.F)
left_sensor = UltrasonicSensor(Port.A)
right_sensor = UltrasonicSensor(Port.B)
color_sensor = ColorSensor(Port.C)

drive_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
steering_motor = Motor(Port.D)
drive_motor.run(1200)
# Kalibracija volana
steering_motor.run_target(800, 0)

# Koliko stupnjeva motora predstavlja jedan krug
# OVO TREBAŠ IZMJERITI
LAP_DEGREES = 10000

lap = 0

while lap < 3:

    front = front_sensor.distance()
    left = left_sensor.distance()
    right = right_sensor.distance()
    cube = color_sensor.color()

    # Vožnja naprijed
    drive_motor.run(300)

    # Kocka ispred -> skreni lijevo (crvena) ili desno (zelena)
    if cube == Color.RED:
        steering_motor.track_target(20)

    elif cube == Color.GREEN:
        steering_motor.track_target(-20)

    # Zid ispred -> skreni lijevo
    elif front < 650:
        steering_motor.track_target(35)
    
    # Praćenje zida lijevo/desno
    elif left < 200:
        steering_motor.run_target(200, 20)
        wait(100)

    elif right < 200:
        steering_motor.run_target(200, -25)
        wait(100)

    else:
        steering_motor.track_target(0)
        drive_motor.run(400)

    # Brojanje krugova
    if abs(drive_motor.angle()) >= LAP_DEGREES:
        lap += 1
        print("Krug:", lap)

        drive_motor.reset_angle(0)

    wait(20)

drive_motor.stop()
steering_motor.run_target(200, 0)

print("Gotovo!")
