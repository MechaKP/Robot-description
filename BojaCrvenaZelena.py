from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Hub
hub = PrimeHub()

# Senzori
color_sensor = ColorSensor(Port.D)

# Motori
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.F)

# Robot
robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=64,
    axle_track=135
)

# Postavke
LAP_MM = 10050      # duljina jednog kruga
lap = 0

robot.reset()

while lap < 3:

    # Vožnja naprijed
    robot.drive(150, 0)

    # Očitavanje boje
    color = color_sensor.color()

    # Crvena = lijevo
    if color == Color.RED:
        robot.stop()
        robot.turn(-45)
        wait(500)
        robot.drive(150, 0)
        wait(2000)
        robot.turn(45)
    # Zelena = desno
    elif color == Color.GREEN:
        robot.stop()
        robot.turn(45)
        wait(500)
        robot.drive(150, 0)
        wait(2000)
        robot.turn(-45)
        robot.drive(150,0)
        wait(2900)
        robot.stop()
        robot.turn(90)
    elif color == Color.GRAY:
        robot.stop()
        wait(200)
        robot.turn(90)
        wait(200)
    elif color == Color.BLACK:
        robot.stop()
        wait(200)
        robot.turn(90)
        wait(200)
    elif color == Color.BROWN:
        robot.stop()
        wait(200)
        robot.turn(90)
        wait(200)

robot.stop()
print("Gotovo! Završena 3 kruga.")
