import waveFunctions as b
import time
import RPi.GPIO as GPIO

b.initSpiAdc()
b.waitForOpen()
 



dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxV =3.3
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setwarnings(False)
c = time.time()
count = 1
samples = []

a = time.time()
b.getAdc(samples, a, c, count)
c = time.time()



b.save(samples, a, c, count)
b.deinitSpiAdc()