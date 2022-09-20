from asyncio.windows_events import NULL
import RPi.GPIO as GPIO


class Sensor():
    def __init__(self):
        self.type = NULL
        self.pull_mode = NULL
        self.value = NULL
        self.pin = NULL

    def __init__(self, type, pull_mode, pin):
        self.type = type
        self.pull_mode = pull_mode
        self.pin = pin
        self.value = NULL
        GPIO.setup(self.pin, GPIO.IN)
    
    def set_pin(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)
    
    def set_pull_mode(self, pull_mode):
        self.pull_mode = pull_mode
    
    def get_value(self):
        if((self.pin == NULL) or (self.pull_mode == NULL)):
            print("Sensor not initialized")
            return -1
        else:
            self.value = GPIO.input(self.pin)
        return self.value