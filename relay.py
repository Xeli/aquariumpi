import RPi.GPIO as GPIO

relays=[-1, 7, 8, 25, 24, 23, 18, 15, 4]

def setupRelayOUT(relayNumber):
    GPIO.setup(relays[relayNumber], GPIO.OUT)
    GPIO.output(relays[relayNumber], True)

def setRelay(relayNumber, activate):
    GPIO.output(relays[relayNumber], activate)

GPIO.setmode(GPIO.BCM)
