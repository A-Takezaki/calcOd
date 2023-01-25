import wiringpi as pi
import time
import mcp_adc
import csv
import os
import pandas as pd
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# LEDのピン設定
PIN_LASER = 21
# 何秒計測するか
measurementTime = 3
# LASERピン設定
factory = PiGPIOFactory()
led = LED(PIN_LASER, pin_factory=factory)

def getPhotodiodeSignal(measurementTime):
    SPI_CE = 0
    SPI_SPEED = 1000000
    READ_CH = 0
    VREF = 3.3

    adc = mcp_adc.mcp3208( SPI_CE, SPI_SPEED, VREF )

    # データフレームを初期化
    df = pd.DataFrame(columns=['Value', 'Volt'])

    # 一定期間のデータをDataFrameに蓄積
    for _ in range(measurementTime * 10):
        value = adc.get_value( READ_CH )
        volt = adc.get_volt( value )
        print ("Value:", value, " Volt:", volt )
        # with open('/home/raspi/script/lab/calcOd/voldata.csv', 'a') as f:
        #     writer = csv.writer(f)
        #     writer.writerow([value, volt])
        # df = df.concat([value,volt])
        df = df.append({'Value': value, 'Volt': volt}, ignore_index=True)
        time.sleep(0.1)

    print(df)
    max = df['Volt'].max()
    print("max:",max)
    return max

def turnOnLaserAndGetMaxVolt(led,measurementTime):
    # # LASERピン設定
    # factory = PiGPIOFactory()
    # led = LED(PIN_LASER, pin_factory=factory)

    # LEDを点灯し、フォトダイオードで計測する
    print("LED ON")
    led.on()
    volt = getPhotodiodeSignal(measurementTime)
    led.off()
    print("LED OFF")
    
    return volt


def outputPhotodiodeSignal():
    volt = turnOnLaserAndGetMaxVolt(led,measurementTime)
    print("outputPhotodiodeSignal",volt)
    # voltをcsvに書き込み
    append_volt_to_csv(volt)
    return volt


def append_volt_to_csv(volt):
    file_exists = os.path.isfile('data.csv')
    with open('data.csv', mode='a') as file:
        fieldnames = ['volt']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'volt': volt})