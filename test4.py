# -*- coding: UTF-8 -*-
import os
import curses
import random


Points = 0   
Map =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        
Player = [5,5]

Pop2 = 1
while Pop2 <= 10:
    x = random.randint(2,38)
    y = random.randint(2,22)

    if Map[y][x] == 0:
        Map[y][x] = 2
        Pop2 += 1

Pop3 = 1
while Pop3 <= 20:
    x = random.randint(2,38)
    y = random.randint(2,22)

    if Map[y][x] == 0:
        Map[y][x] = 3
        Pop3 += 1


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
        
def main(stdscr):
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    while True:     
        stdscr.clear()

        for row in range(24):
                for val in range(40):

                    x = val*2
                    #x = max(min(val*2, 80), 0)
                    y = row
                    if row == Player[1] and val == Player[0]:
                        try: stdscr.insstr(y, x,'▜▛')
                        except curses.error: pass
                    elif Map[row][val] == 0:
                        try: stdscr.insstr(y, x,'v^',curses.color_pair(3))
                        except curses.error: pass
                    elif Map[row][val] == 1:
                        try: stdscr.insstr(y, x, '██',curses.color_pair(3))
                        except curses.error: pass
                    elif Map[row][val] == 2:
                        try: stdscr.insstr(y, x,'╭╮' )
                        except curses.error: pass
                    elif Map[row][val] == 3:
                        try: stdscr.insstr(y, x,'╱╲')
                        except curses.error: pass
                print()

        try: stdscr.addstr(23,0,'{:20}'.format("Player: " + str(Player)),curses.A_BOLD | curses.color_pair(2))
        except curses.error: pass
        try: stdscr.addstr(23,20,'{:20}'.format("Points: [" + str(Points) + "]"),curses.color_pair(1))
        except curses.error: pass

        c = stdscr.getch()
        if c == ord('q'):
            break
        elif c == ord('w'):
            if CanMove('w') == True:
                Move('w')
        elif c == ord('a'):
            if CanMove('a') == True:
                Move('a')
        elif c == ord('s'):
            if CanMove('s') == True:
                Move('s')
        elif c == ord('d'):
            if CanMove('d') == True:
                Move('d')

        """for row in range(10):
                for val in range(10):
                    if row == Player[1] and val == Player[0]:
                        print ('╦', end = '╦')
                    elif Map[row][val] == 0:
                        print(' ', end = ' ')
                    elif Map[row][val] == 1: 
                        stdscr.addstr(2, 2, '█')
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
        """
curses.wrapper(main)

