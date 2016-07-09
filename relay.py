import RPi.GPIO as GPIO

# the -1 is there to make this 1-based
# because the relay id's on the board start at 1
relays=[-1, 7, 8, 25, 24, 23, 18, 15, 4]

def setupRelayOUT(relayNumber):
    GPIO.setup(relays[relayNumber], GPIO.OUT)
    GPIO.output(relays[relayNumber], True)

def setRelay(relayNumber, activate):
    GPIO.output(relays[relayNumber], activate)

GPIO.setmode(GPIO.BCM)
