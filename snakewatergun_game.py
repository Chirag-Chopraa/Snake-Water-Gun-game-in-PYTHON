import random
import os
clear = lambda: os.system('cls')
clear()
total = 0
points = 0
while(True):
    attacks = ['snake','water','gun']
    pc = random.choice(attacks)
    score = str(points)+'/'+str(total)
    print('\t\t\t\t\tWelcome to SNAKE, WATER, GUN game')
    print('\t\t\t\t\t\t\t-Developed by Chirag Chopra V1.1\n\n')
    print('\t\ts - snake\t\t\t\t\t\t\t\tScores -',score,'\n\t\tw - water\n\t\tg - gun')
    user = input('\n\t\tChoose your attack : ')
    if pc == 'snake' and user == 'water' or user == 'w':
        print('\t\tYou loss..!!\n')
        points = points+1
    elif pc == 'snake' and user == 'gun' or user == 'g':
        print('\t\tYou won..!!\n')
    elif pc == 'water' and user == 'gun' or user == 'g':
        print('\t\tYou loss..!!\n')
    elif pc == 'water' and user == 'snake' or user == 's':
        print('\t\tYou won..!!\n')
        points = points + 1
    elif pc == 'gun' and user == 'snake' or user == 's':
        print('\t\tYou loss..!!\n')
    elif pc == 'gun' and user == 'water' or user == 'w':
        print('\t\tYou won..!!\n')
        points = points + 1
    elif pc == user:
        print('\t\tTied..!!\n')
    else:
        print('\t\tPlease type valid attack\n')
    print('\tPlease type y for yes & n for no')
    again = input('\tWanna play again ???\n\t')
    if again == 'y' or again == 'yes':
        clear()
        total = total + 1
        continue
    elif again=='n' or again=='no':
        print('\tbye..have a nice day <3')
        break
    else:
        break