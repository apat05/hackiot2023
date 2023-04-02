import RPi.GPIO as GPIO
import time


import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


# Setting up GPIO mode and pin for LED
GPIO.setmode(GPIO.BOARD)

ultrasonic_channel = 0

# Read the output of the Grove light sensor with intervals of 100ms and print the raw value along with the text “bright” or “dark”
threshold = 500  
start_time = time.time()
while (time.time() - start_time) < 5:
    ultrasonic_value = mcp.read_adc(ultrasonic_channel)
    if ultrasonic_value > threshold:
        print("No: ", ultrasonic_value)
    else:
        print("Dish-in: ", ultrasonic_value)
    time.sleep(0.1)


# Cleanup
GPIO.cleanup()


