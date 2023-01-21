# calOd
OD測定のためのプログラム for Takeya

## プログラム起動方法
1. 左上のターミナルアイコン（黒い四角に白で>_と書いてあるアイコン）をタップ
2. 以下コマンドを入力
```
pi@raspberrypi:~ $ sudo pigpiod
pi@raspberrypi:~ $ python3 calcOd/app.py
```
以下のような表示が出たら成功
```
pi@raspberrypi:~ $ python3 calcOd/app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 121-474-916
```
## 使用する電子回路
![ブレッドボード図](https://user-images.githubusercontent.com/75236064/213842254-f8aa3dae-f33b-4fdf-8cb3-b7959118c38e.png)
※2023/01/21現在
※分圧回路実装予定


## Webインターフェース使用方法
※準備中

## プログラムアップデート方法
1. ターミナルアイコンをタップ
2. 以下コマンドを入力
```
pi@raspberrypi:~ $ cd calcOd
pi@raspberrypi:~ $ git pull https://github.com/A-Takezaki/calcOd
```