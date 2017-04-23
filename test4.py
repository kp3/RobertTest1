# -*- coding: UTF-8 -*-
import os
import curses


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
        
def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    while True:     
        stdscr.clear()

        for row in range(10):
                for val in range(10):

                    x = val*2
                    y = row
                    if row == Player[1] and val == Player[0]:
                        stdscr.addstr(y, x,'╦╦')
                    elif Map[row][val] == 0:
                        stdscr.addstr(y, x,'v^',curses.color_pair(3))
                    elif Map[row][val] == 1:
                        stdscr.addstr(y, x, '██',curses.color_pair(3))
                    elif Map[row][val] == 2:
                        stdscr.addstr(y, x,'╭╮' )
                    elif Map[row][val] == 3:
                        stdscr.addstr(y, x,'╱╲')
                print()

        stdscr.addstr(10,0,'{:20}'.format("Player: " + str(Player)),curses.color_pair(2))
        stdscr.addstr(11,0,'{:20}'.format("Points: [" + str(Points) + "]"),curses.color_pair(1))

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

