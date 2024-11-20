import RPi.GPIO as GPIO

class SensorManager:
    def __init__(self, sensor_pins):
        self.sensor_pins = sensor_pins
        GPIO.setmode(GPIO.BCM)
        for pin in sensor_pins:
            GPIO.setup(pin, GPIO.IN)

    def check_sensors(self):
        statuses = {}
        for name, pin in self.sensor_pins.items():
            statuses[name] = GPIO.input(pin)
        return statuses

