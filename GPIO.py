import RPi.GPIO as GPIO

IN = 17
LED = 22
PWM = 12

HIGH = True
LOW = False

try:
    GPIO.setmode(GPIO.BCM)      # GPIO番号指定

    GPIO.setup(IN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)     # 入力指定
    GPIO.setup(LED, GPIO.OUT)   # 出力指定
    GPIO.setup(PWM, GPIO.OUT)
    pwm_out = GPIO.PWM(PWM, 1000)
    pwm_out.start(0)

    while True:
        value = GPIO.input(IN)
        if value == HIGH:
            GPIO.output(LED, HIGH)
            pwm_out.ChangeDutyCycle(5)
        elif value == LOW:
            GPIO.output(LED, LOW)
            pwm_out.ChangeDutyCycle(0)
        print(value)   # ピンの電圧状態を表示する

finally:
    pwm_out.stop()       # PWM出力を停止する
    GPIO.cleanup()   # GPIO設定をリセット
