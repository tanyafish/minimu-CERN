# first four bars of punks

import speech
import microbit

while True:

    if microbit.accelerometer.is_gesture("up"):
        speech.say("WORK IT", speed=120, pitch=100, throat=100, mouth=200)
        while microbit.accelerometer.is_gesture("up"):
            pass

    elif microbit.accelerometer.is_gesture("down"):
        speech.say("MEKIT", speed=150, pitch=50, throat=150, mouth=200)
        while microbit.accelerometer.is_gesture("down"):
            pass

    elif microbit.accelerometer.is_gesture("left"):
        speech.say("DO IT", speed=120, pitch=80, throat=100, mouth=200)
        while microbit.accelerometer.is_gesture("left"):
            pass

    elif microbit.accelerometer.is_gesture("right"):
        speech.say("MYKSUS", speed=100, pitch=20, throat=80, mouth=200)
        while microbit.accelerometer.is_gesture("right"):
            pass
