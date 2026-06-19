from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

hub = PrimeHub()

drive_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
steering_motor = Motor(Port.D)

# Kalibracija volana
steering_motor.run_target(800, 0)

# --- Postavke -----------------------------------------------------------
DRIVE_SPEED = 2000       # brzina vožnje ravno
TURN_SPEED = 300        # brzina vožnje tijekom skretanja
TURN_STEER_ANGLE = 25   # maksimalni kut volana tijekom skretanja
                          # OVO TREBAŠ IZMJERITI (ovisi o tvom robotu)


def FD(degrees):
    """
    Vozi naprijed dok motor ne odvozi zadani broj stupnjeva.
    Primjer: FD(1000) -> vozi naprijed 1000 stupnjeva motora.
    """
    steering_motor.track_target(0)
    drive_motor.reset_angle(0)
    drive_motor.run(DRIVE_SPEED)

    while abs(drive_motor.angle()) < degrees:
        wait(10)


def TR(angle):
    """
    Skreni za zadani kut u stupnjevima (mjeri žiroskop, ne timing).
    Pozitivan kut (npr. TR(90))  -> skreće DESNO.
    Negativan kut (npr. TR(-90)) -> skreće LIJEVO.

    Ako se na tvom robotu skreće obrnuto, samo zamijeni predznak
    u liniji "steer = ..." ispod.
    """
    direction = 1 if angle > 0 else -1
    target = abs(angle)

    steer = -TURN_STEER_ANGLE * direction  # plus = desno, minus = lijevo

    hub.imu.reset_heading(0)
    steering_motor.track_target(steer)
    drive_motor.run(TURN_SPEED)

    while abs(hub.imu.heading()) < target:
        wait(10)

    # Poravnaj kotače nazad na ravno
    steering_motor.track_target(0)


# --- Primjer korištenja ---------------------------------------------------
FD(700)
TR(-90)
FD(1100)
TR(-90)
FD(1150)
TR(-100)
FD(1150)
TR(-90)
FD(1150)
TR(-90)
FD(1150)
TR(-90)
FD(1150) # POCETAK 
TR(-90)
FD(1150)
TR(-90)
FD(1150) 
TR(-90)
FD(1150)
TR(-90)
FD(1150) 
TR(-90)
FD(1150)
TR(-90)
FD(1150) 




drive_motor.stop()
steering_motor.run_target(500, 0)

print("Gotovo!")
