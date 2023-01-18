from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# LEDのピン設定
PIN_LASER = 21

def main():
    # LASERピン設定
    factory = PiGPIOFactory()
    led = LED(PIN_LASER, pin_factory=factory)

    # LASERをチカチカ
    for _ in range(5):
        print("LED ON")
        led.on()
        sleep(5.0)
        print("LED OFF")
        led.off()
        sleep(1.0)
    # while(True):
    #   print("LED ON")
    #   led.on()
    #   sleep(1.0)
    #   print("LED OFF")
    #   led.off()
    #   sleep(1.0)
      
    return

if __name__ == "__main__":
    main()