from playsound import playsound
from time import sleep
for c in range(10, 0, -1):
    print('{}'.format(c), end='')
    sleep(0.334)
    print('.', end='')
    sleep(0.334)
    print('.', end='')
    sleep(0.334)
    print('.', end='')
print('\033[1;32mHAPPY NEW YEAR!!!\033[m')
playsound('Fireworks NYE.mp3')
