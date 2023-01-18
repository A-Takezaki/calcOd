import wiringpi as pi
import time
import mcp_adc
import csv
import pandas as pd

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

adc = mcp_adc.mcp3208( SPI_CE, SPI_SPEED, VREF )

# データフレームを初期化
df = pd.DataFrame(columns=['Value', 'Volt'])

# 一定期間のデータをDataFrameに蓄積
for _ in range(10):
    value = adc.get_value( READ_CH )
    volt = adc.get_volt( value )
    print ("Value:", value, " Volt:", volt )
    # with open('/home/raspi/script/lab/calcOd/voldata.csv', 'a') as f:
    #     writer = csv.writer(f)
    #     writer.writerow([value, volt])
    # df = df.concat([value,volt])
    df = df.append({'Value': value, 'Volt': volt}, ignore_index=True)

    time.sleep(1)

print(df)
max = df['Volt'].max()
print("max:",max)


