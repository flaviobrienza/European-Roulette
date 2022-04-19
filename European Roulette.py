import random
import time

def game():
    red = [3, 12, 7, 18, 9, 14, 1, 16, 5, 23, 30, 36, 27, 34, 25, 21, 19, 32]
    black = [26,35,28,29,22,31,20,33,24,10,8,11,13,6,17,2,4,15]
    green = [0]
    allnum = red + black + green
    betnum = int(input('Choose a number from 0 to 36 (if you do not want to bet on a number type a value higher than 36): '))
    # if you want to bet only on "0", without choosing a color, type "/" in betcolor
    betcolor = input('Choose a color between red and black (if you do not want to bet on a number type "/"): ')
    print('Thanks, the roulette starts')
    roulette = random.choice(allnum)  
    for x in range(4):
        print(x)
        time.sleep(1)
    print('The number is', roulette) 
    if betnum == roulette:
        print('Congratulations, you won your bet X35')
    if betcolor == 'red' and roulette in red:
        print('Congratulations, you won your bet X2')
    if betcolor == 'black' and roulette in black:
        print('Congratulations, you won your bet X2')
    if betnum > 36:
        print('You have not betted on a number')
    if betcolor == '/':
        print('You have not betted on a color') 
    if roulette != betnum and (0 <= betnum <= 36) :
        print('Wrong number')
    if betcolor == 'red' and roulette in black:
        print('Wrong color')
    if betcolor == 'black' and roulette in red:
        print('Wrong color')
    if betcolor == 'black' and roulette in green:
        print('Wrong color')
    if betcolor == 'red' and roulette in green:
        print('Wrong color') 
    print('Restart the program to play again') 


            
game() 