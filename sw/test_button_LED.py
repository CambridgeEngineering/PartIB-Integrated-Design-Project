from machine import Pin
from utime import sleep

#Set the LED pin and configuration
led_pin = 28
led = Pin(led_pin, Pin.OUT)

#Continiously update the LED value and print said value
while True:
  led.value(button.value())
  sleep(0.1)
  print(button.value())
