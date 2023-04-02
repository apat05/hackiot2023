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
led_pin = 11
GPIO.setup(led_pin, GPIO.OUT)

light_channel = 0
sound_channel = 1


# Blink the LED 5 times with on/off intervals of 500ms
for i in range(5):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.5)

# Read the output of the Grove light sensor with intervals of 100ms and print the raw value along with the text “bright” or “dark”
threshold = 500  
start_time = time.time()
while (time.time() - start_time) < 5:
    light_value = mcp.read_adc(light_channel)
    if light_value > threshold:
        print("Bright: ", light_value)
    else:
        print("Dark: ", light_value)
    time.sleep(0.1)

# Blink the LED 4 times with on/off intervals of 200ms
for i in range(4):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.2)

# Read the output of the Grove sound sensor with intervals of 100ms and print the raw value. If the sound sensor is tapped, turn on the LED for 100ms
threshold = 200  
start_time = time.time()
while (time.time() - start_time) < 5:
    sound_value = mcp.read_adc(1)
    print("Sound: ", sound_value)
    if sound_value > threshold:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.1)

# Cleanup
GPIO.cleanup()


