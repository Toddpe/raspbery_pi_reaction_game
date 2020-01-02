
from gpiozero import Button, LED, PWMLED
from time import sleep
import random

led = LED(17)
player_1_cheater = LED(22)
player_2_cheater = LED(27)
player_1_winner = PWMLED(15)
player_2_winner = PWMLED(14)

player_1 = Button(4)
player_2 = Button(18)
num = 0
cheater = False

time = random.uniform(5, 10)
sleep(time)
if player_1.is_pressed:
    print('Player 1 is a cheater!')
    player_1_cheater.on()
    cheater = True
if player_2.is_pressed:
    print('Player 2 is a cheater!')
    player_2_cheater.on()
    cheater = True
led.on()

while True:
    if cheater == True:
        break
    if player_1.is_pressed:
        print ("Player 1 wins in {} tenths of a second!".format(num))
        player_1_winner.pulse(2)
        break
    if player_2.is_pressed:
        print (" Player 2 wins! in {} tenths of a second!".format(num))
        player_2_winner.pulse(2)
        break
    else:
        num = num + 1
        sleep(0.1)
led.off()
