# -*- coding: utf-8 -*-


# GPIO 라이브러리
import wiringpi
import sys

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = _GetchUnix()


# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0



# 실제 핀 정의
#PWM PIN
ENA = 25
ENB = 30

#GPIO PIN
IN1 = 24
IN2 = 23
IN3 = 22
IN4 = 21


# 핀 설정 함수
def setPinConfig(EN, INA, INB):
    wiringpi.pinMode(EN, OUTPUT)
    wiringpi.pinMode(INA, OUTPUT)
    wiringpi.pinMode(INB, OUTPUT)
    wiringpi.softPwmCreate(EN, 0, 255)

# 모터 제어 함수
def setMotorContorl(PWM, INA, INB, speed, stat):
    #모터 속도 제어 PWM
    wiringpi.softPwmWrite(PWM, speed)

    #앞으로
    if stat == FORWARD:
        wiringpi.digitalWrite(INA, HIGH)
        wiringpi.digitalWrite(INB, LOW)
    #뒤로
    elif stat == BACKWARD:
        wiringpi.digitalWrite(INA, LOW)
        wiringpi.digitalWrite(INB, HIGH)
    #정지
    elif stat == STOP:
        wiringpi.digitalWrite(INA, LOW)
        wiringpi.digitalWrite(INB, LOW)

# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorContorl(ENA, IN1, IN2, speed, stat)
    else:
        setMotorContorl(ENB, IN3, IN4, speed, stat)

#GPIO 라이브러리 설정
wiringpi.wiringPiSetup()

#모터 핀 설정
setPinConfig(ENA, IN1, IN2)
setPinConfig(ENB, IN3, IN4)

if __name__ == '__main__':
#제어 시작
c=''
extra_go=0
extra_left=0
extra_right=0
while c != 'q':
    sys.stdout.write("cmd : ")
    c=getch()

    if c == 'h':	#left
	print('h')
        extra_go=0
        extra_right=0
        setMotor(CH1, 150+extra_left, FORWARD)
        setMotor(CH2, 100, FORWARD)
        extra_left += 50
    elif c == 'k':	#right
	print('k')
        extra_go=0
        extra_left=0
        setMotor(CH1, 100, FORWARD)
        setMotor(CH2, 150+extra_right, FORWARD)
        extra_right += 50
    elif c == 'u':	#go
	print('u')
        extra_left=0
        extra_right=0
        setMotor(CH1, 100+extra_go, FORWARD)
        setMotor(CH2, 100+extra_go, FORWARD)
        extra_go += 50
    elif c == 'j':	#stop
	print('j')
        extra_go=0
        extra_left=0
        extra_right=0
        setMotor(CH1, 100, STOP)
        setMotor(CH2, 100, STOP)
    elif c == 'm':	#back
	print('m')
        extra_go=0
        extra_left=0
        extra_right=0
        setMotor(CH1, 150, BACKWARD)
        setMotor(CH2, 150, BACKWARD)
    elif c == 'q':
	print('q')
        extra_go=0
        extra_left=0
        extra_right=0
        setMotor(CH1, 100, STOP)
        setMotor(CH2, 100, STOP)
        break;
    else:
        print(c)

print("done")
            

# FORWARD, BACKWARD, STOP




