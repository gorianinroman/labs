import spidev
import time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt


########################################
#   Open, use and close SPI ADC
########################################
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxV =3.3
comp = 4
troyka = 17
samples = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setwarnings(False)
spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1000
    print ("SPI for ADC have been initialized")

def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac,signal)
    return signal



    
    
    
    


def getAdc(samples, a, c, count):
    a = time.time()
    print()
    time_start = time.time()
    time_end = time.time()
    i = 0
    while (time_end - time_start < 15):
        time_end = time.time()
        c = time.time()
        for value in range(256):
            signal = num2dac(value)
            voltage = value/levels * maxV
            time.sleep(0.0001)
            compValue = GPIO.input(comp)
            if compValue == 0:
                print ("ADC value = {:^3} -> {}, input voltage = {:.2f}".format(value, signal, voltage))
                break
        samples.append(value)
        i = i + 1
    print(i)
    print(format(a - c))
    count = 10 / i
    print(count)

    


########################################
#   Setup, use and cleanup GPIO
########################################

def waitForOpen():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.IN)

    print('GPIO initialized. Wait for door opening...')
    a = 1

    while a > 0:
        a=int(input())

    GPIO.cleanup()
    print('The door is open. GPIO has been cleaned up. Start sampling...')


########################################
#   Save and read data
########################################

def save(samples, start, finish, Hz):
    filename = 'wave-data_40mm opening {}.txt'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))

    with open(filename, "w") as outfile:
        outfile.write('- Wave Lab\n')
        #outfile.write('- Частота дискретизации: {:.6f} s\n\n'.format(10/count))
        outfile.write('- Date: {}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        outfile.write('- Duration: {:.2f} s\n\n'.format(finish - start))
        
        np.savetxt(outfile, np.array(samples).T, fmt='%d')

def read(filename):
    with open(filename) as f:
        lines = f.readlines()

    duration = float(lines[2].split()[2])
    samples = np.asarray(lines[4:], dtype=int)
    
    return samples, duration, len(samples)