from machine import Pin
import time

led = Pin('LED', Pin.OUT)
dir = Pin(15, Pin.OUT)
step = Pin(14, Pin.OUT)
sleep = Pin(13, Pin.OUT)

led.low()
sleep.low()
dir.low()
step.low()

while True:
    sleep.high()
    for x in range(3200):
        step.value(1)
        time.sleep_ms(1)
        step.value(0)
        time.sleep_ms(1)
        if x % 100 == 0:
            led.toggle()
    sleep.low()
    led.high();
    time.sleep(30)