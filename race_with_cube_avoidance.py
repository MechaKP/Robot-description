from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
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

# --- Postavke izbjegavanja kocke ------------------------------------------
# Trajanje (ms) svake faze manevra izbjegavanja.
# OVO TREBAŠ IZMJERITI na svom robotu / stazi (ovisi o AVOID_SPEED).
AVOID_OUT_TIME = 700        # faza 1: skretanje OD kocke
AVOID_STRAIGHT_TIME = 900   # faza 2: vožnja ravno pored kocke
AVOID_BACK_TIME = 700       # faza 3: skretanje natrag na pravac

AVOID_STEER_ANGLE = 35      # kut volana tijekom izbjegavanja
AVOID_SPEED = 200           # sporija, sigurnija brzina tijekom izbjegavanja

SIDE_TOO_CLOSE = 200        # mm - ako je strana prema kojoj skrećemo preblizu zida

# Stanje izbjegavanja
avoid_direction = None      # None = ne izbjegavamo, 1 = lijevo (crveno), -1 = desno (zeleno)
avoid_phase = 0              # 1 = skretanje van, 2 = ravno, 3 = skretanje natrag
avoid_timer = StopWatch()

lap = 0

while lap < 3:

    left = left_sensor.distance()
    right = right_sensor.distance()
    cube = color_sensor.color()

    # --- Pokreni izbjegavanje kocke ako je vidimo i trenutno ne izbjegavamo ---
    if avoid_direction is None and cube in (Color.RED, Color.GREEN):
        avoid_direction = 1 if cube == Color.RED else -1
        avoid_phase = 1
        avoid_timer.reset()
        print("Kocka detektirana, izbjegavam:", "lijevo" if avoid_direction == 1 else "desno")

    # --- Izvođenje manevra izbjegavanja kocke ---
    if avoid_direction is not None:

        elapsed = avoid_timer.time()

        # Sigurnosna provjera: ako je strana prema kojoj skrećemo preblizu zida,
        # smanji kut skretanja umjesto potpunog skretanja
        side_dist = left if avoid_direction == 1 else right
        steer_angle = AVOID_STEER_ANGLE * avoid_direction
        if side_dist < SIDE_TOO_CLOSE:
            steer_angle = (AVOID_STEER_ANGLE / 3) * avoid_direction

        drive_motor.run(AVOID_SPEED)

        if avoid_phase == 1:
            steering_motor.track_target(steer_angle)
            if elapsed >= AVOID_OUT_TIME:
                avoid_phase = 2
                avoid_timer.reset()

        elif avoid_phase == 2:
            steering_motor.track_target(0)
            if elapsed >= AVOID_STRAIGHT_TIME:
                avoid_phase = 3
                avoid_timer.reset()

        elif avoid_phase == 3:
            steering_motor.track_target(-steer_angle)
            if elapsed >= AVOID_BACK_TIME:
                avoid_direction = None
                avoid_phase = 0
                steering_motor.track_target(0)

    # --- Normalna vožnja / praćenje zida (samo kad ne izbjegavamo kocku) ---
    else:
        drive_motor.run(300)

        # Praćenje zida lijevo/desno
        if left < 300:
            steering_motor.run_target(200, -20)
            wait(100)

        elif right < 250:
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