# -*- coding: UTF-8 -*-
import os
from colorama import init, AnsiToWin32, Fore

def cls():
	print("\033[2Jtest")
Points = 0   
Map =  [[1,1,1,1,1,1,1,1,1,1],
        [1,2,0,0,0,0,0,0,0,1],
        [1,0,3,0,0,0,0,0,0,1],
        [1,0,0,1,3,0,1,0,3,1],
        [1,0,0,1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1,0,0,1],
        [1,0,0,1,1,1,1,0,0,1],
        [1,0,0,0,0,0,0,3,0,1],
        [1,0,0,3,0,2,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]
        
Player = [5,5]


def CheckTile( x, y ):
    global Points
    if Map[y][x]==2:
        Points += 20
        Map[y][x]=0
    if Map[y][x]==3:
        Points += 10
        Map[y][x]=0

def CanMove( Input ):
    if Input == 'w':
        if Map[Player[1]-1][Player[0]]!=1:
            return True
    if Input == 'a':
        if Map[Player[1]][Player[0]-1]!=1:
            return True
    if Input == 's':
        if Map[Player[1]+1][Player[0]]!=1:
            return True
    if Input == 'd':
        if Map[Player[1]][Player[0]+1]!=1:
            return True

def Move( Input ):
    if Input == 'w':
        Player[1]-=1
    if Input == 'a':
        Player[0]-=1
    if Input == 's':
        Player[1]+=1
    if Input == 'd':        
        Player[0]+=1
    CheckTile(Player[0],Player[1])
        

while True:     
    cls()
    for row in range(10):
            for val in range(10):
                if row == Player[1] and val == Player[0]:
                    print ('╦', end = '╦')
                elif Map[row][val] == 0:
                    print(' ', end = ' ')
                elif Map[row][val] == 1:
                    print('█', end = '█')
                elif Map[row][val] == 2:
                    print('╭', end = '╮')
                elif Map[row][val] == 3:
                    print('╱', end = '╲')
            print()
    print("Player: " + str(Player))
    print("Points: " + str(Points)) 
    Answer = input()
    if Answer.strip() == 'x':
        break
    elif Answer.strip() == 'w':
        if CanMove('w') == True:
            Move('w')
    elif Answer.strip() == 'a':
        if CanMove('a') == True:
            Move('a')
    elif Answer.strip() == 's':
        if CanMove('s') == True:
            Move('s')
    elif Answer.strip() == 'd':
        if CanMove('d') == True:
            Move('d')
        
