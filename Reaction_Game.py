# Wire the signal LED to GPIO 17
# Wire player 1's cheater LED to GPIO 22
# Wire player 2's cheater LED to GPIO 27
# Wire player 1's winning LED to GPIO 15
# Wire player 2's winning LED to GPIO 14
# Wire player 1's button to GPIO 4
# Wilre player 2's a button to GPIO 18

#                               OBJECT OF THE GAME:
# The first player to press their buttion after the signal light goes off wins!
# Be sure not to cheat.

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
sec = 0
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
        print("Player 1 wins!")
        player_1_winner.pulse(2)
        break
    if player_2.is_pressed:
        print("Player 2 wins!")
        player_2_winner.pulse(2)
        break
    else:
        print(sec)
        sec = sec + 1
        sleep(0.01)
led.off()
