# PS1: Slide Puzzle Solver Version 1.1 10/3/2017 
# by Dr Loke K.S.
# based on Al Sweigart al@inventwithpython.com
# Released under a "Simplified BSD" license
# to install pygame: python -m pip install pygame

from copy import deepcopy
import pygame, sys, random
from abc import ABCMeta, abstractmethod
from pygame.locals import *
import queue as Q
import pdb  #python debugger

#################
# Globals     ###
SIZE=3       #Size of the Puzzle, number of columns=number of rows
INITSTEPS=10   #Number of steps to scramble the puzzle at the start
start=[[1,4,7],[0,5,8],[2,3,6]]  #fixed starting position:must be same SIZExSIZE
SCRAMBLE=True    #if false then use the start[] data as starting position, 
                  #if true then scramble the tiles random for INITSTEPS times
#################

#
# Basic data structure Stack
#
#
class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)
#
# Basic data structure Queue
# (Use my own Queue instead of import) 
#        
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def add(self, item):
        self.items.insert(0,item)
    def get(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


#
# Solver Class: propose moves to the Board Class 
#
#
class Solver(metaclass=ABCMeta):
    """
     ABC=Abstract base class
     Abstract Solver class that searches through the state space, called by the Board class
    """
    @abstractmethod
    def get(self):
         raise NotImplementedError()
    @abstractmethod
    def add(self):
         raise NotImplementedError()
     
class Solver1(Solver):
    """
     Concrete solver: must implement abstract methods from abstract class Solver
     uses a Queue
    """
    def __init__(self):
        self.queue=Queue()
    def get(self):
        return self.queue.get()
    def add(self,board):
        self.queue.add(board)

class Solver2(Solver):
    """
     Concrete solver: must implement abstract methods from abstract class Solver
     Uses a Stack
    """
    def __init__(self):
        self.stack=Stack()
    def get(self):
        return self.stack.pop()
    def add(self,board):
        self.stack.push(board)

class Solver3(Solver):
    """
     Concrete solver 3: must implement abstract methods from abstract class Solver
     Uses the Python built-in Priority Queue
    """

    def __init__(self, goal,width,height):
        self.pq=Q.PriorityQueue()
        self.goal=goal
        self.w=width
        self.h=height
    def get(self):
        if not self.pq.empty():
             (val,board)=self.pq.get()
             return board
        else:
             return None
    def add(self, board):
        value=self.heuristic(board)
        self.pq.put((value,board))
    def heuristic(self,board):
        count=0;
        for x in range(self.w):
             for y in range(self.h):
                  if self.goal[x][y]!=board[x][y]:
                       count+=1
        return count
     
#  Board Class (Model): keep track on the abstract game state data. No animation or drawing
#                       methods. 
#
class Board:
    """Model class for the game that stores states about the game board.
       This class also include all the necessary operators.
       Does not handle Animation or screen processses.
    """
    BLANK=0
    
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    
    def __init__(self, bwidth, bheight):
        self.bwidth=bwidth
        self.bheight=bheight
        self.board=[]
        self.goal=[]
    
        # Initialize a board data structure with tiles in the solved state.
        # For example, if BWIDTH and BHEIGHT are both 3, this function
        # creates [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
        # From the initial state we later scramble the positions to start the puzzle
        counter = 1
        for x in range(self.bwidth):
            column = []
            for y in range(self.bheight):
                column.append(counter)
                counter += self.bwidth
            self.board.append(column)
            counter -= self.bwidth * (self.bheight - 1) + self.bwidth - 1
        self.board[self.bwidth-1][self.bheight-1] = Board.BLANK
        self.goal=deepcopy(self.board)
    
       
        #### CHANGE THE SOLVER METHOD HERE ##
        self.Solver=Solver1()
        #self.Solver=Solver2()
        #self.Solver=Solver3(self.goal,bwidth,bheight)
        #####################################
               
    def solve(self): #generator function
        #get board
        #get valid moves
        #put new board state in a data structure
        #repeat
        self.used=[]
        self.Solver.add(self.board)
        board=self.Solver.get()
        #pdb.set_trace()

        found=False
        while not(found):
            moves=self.getMoves(board)
            print("moves=",moves)
            for move in moves:
                print("trying ...",move)
                temp=self.makeMove(board,move)
                self.used.append(board)
                if not (temp in self.used):
                     self.printBoard(temp,"moved "+move)
                     self.Solver.add(temp)
                     yield [board, move]
                     if (temp==self.goal):
                          print("Found answer")
                          found=True
                          break
            board=self.Solver.get()
        yield [None,None]
 
    def printBoard(self, board, msg=None):
        print(msg)
        counter = 1
        for x in range(self.bwidth):
            for y in range(self.bheight):
               if board[y][x]==Board.BLANK:
                    print('X', end=' ')
               else:                       
                    print (board[y][x], end=' ')
            print()
        print()
        return
    
    def getBlankPosition(self,board):
        # Return the x and y of board coordinates of the blank space.
        for x in range(self.bwidth):
            for y in range(self.bheight):
                if board[x][y] == Board.BLANK:
                    return (x, y)
               
    def makeMove(self,original_board, move):
        # This function does not check if the move is valid.
        blankx, blanky = self.getBlankPosition(original_board)
        board=deepcopy(original_board)
        if move == Board.UP:
            board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
        elif move == Board.DOWN:
            board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
        elif move == Board.LEFT:
            board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
        elif move == Board.RIGHT:
            board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
        return board
            
    def isValidMove(self,board, move):
        blankx, blanky = self.getBlankPosition(board)
        return (move == Board.UP and blanky != len(board[0]) - 1) or \
           (move == Board.DOWN and blanky != 0) or \
           (move == Board.LEFT and blankx != len(board) - 1) or \
           (move == Board.RIGHT and blankx != 0)            

    def getMoves(self,board, lastMove=None):
        self.printBoard(board,"getMoves for .. ")
        
        # start with a full list of all four moves
        validMoves = [Board.UP, Board.DOWN, Board.LEFT, Board.RIGHT]
        # remove moves from the list as they are disqualified
        if lastMove == Board.UP or not self.isValidMove(board,Board.DOWN):
            validMoves.remove(Board.DOWN)
        if lastMove == Board.DOWN or not self.isValidMove(board,Board.UP):
            validMoves.remove(Board.UP)
        if lastMove == Board.LEFT or not self.isValidMove(board,Board.RIGHT):
            validMoves.remove(Board.RIGHT)
        if lastMove == Board.RIGHT or not self.isValidMove(board,Board.LEFT):
            validMoves.remove(Board.LEFT)

        # return a list of remaining moves
        return validMoves
    
    def getRandomMove(self,board, lastMove=None):
        # start with a full list of all four moves
        validMoves = [Board.UP, Board.DOWN, Board.LEFT, Board.RIGHT]
        # remove moves from the list as they are disqualified
        if lastMove == Board.UP or not self.isValidMove(board,Board.DOWN):
            validMoves.remove(Board.DOWN)
        if lastMove == Board.DOWN or not self.isValidMove(board,Board.UP):
            validMoves.remove(Board.UP)
        if lastMove == Board.LEFT or not self.isValidMove(board,Board.RIGHT):
            validMoves.remove(Board.RIGHT)
        if lastMove == Board.RIGHT or not self.isValidMove(board,Board.LEFT):
            validMoves.remove(Board.LEFT)

        # return a random move from the list of remaining moves
        return random.choice(validMoves)
    
    def scramble(self, num):
        lastMove=None
        for i in range(num):
            move = self.getRandomMove(self.board,lastMove)
            self.board=self.makeMove(self.board, move)
            lastMove=move
        self.printBoard(self.goal,"Goal")
        self.printBoard(self.board,"Start")


#
#  Animation Class: Handle the nitty-gritty of drawing and animation given the game
#                   state. Do not generally need to be modified.
#

class Animation:
    """
    Animation loop: Responsible for drawing and animation on screeen, and capturing mouse events.
    
    """
    def __init__(self, bwidth, bheight):
        
        #Game initialization
        pygame.init()
        self.BOARDWIDTH=bwidth
        self.BOARDHEIGHT=bheight
        self.XMARGIN = int((640 - (80 * self.BOARDWIDTH + (self.BOARDWIDTH - 1))) / 2)
        self.YMARGIN = int((480 - (80 * self.BOARDHEIGHT + (self.BOARDHEIGHT - 1))) / 2)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((640,480))
        pygame.display.set_caption('SwinPuzzle: Intro to AI')
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        
        #Model initialization
        self.Board=Board(self.BOARDWIDTH,self.BOARDHEIGHT)

        
    def checkForQuit(self):
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self.terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back
            
    def terminate(self):
        pygame.quit()
        sys.exit()
        
    def startState(self):
        """ Show the final state """
        loop=True
        while loop: #GAME LOOP
            
            self.drawBoard(self.Board.board)
            self.checkForQuit()
            for event in pygame.event.get(): #check for KEY or MOUSE events
                if event.type == MOUSEBUTTONUP: # get MOUSE EVENT
                    x,y=self.getSpotClicked(event.pos[0],event.pos[1])
                    if not((x,y)==(None,None)):
                        loop=False
                        break
                    
            pygame.display.update()
            self.clock.tick(30)
        if SCRAMBLE==True:
             self.Board.scramble(INITSTEPS) #Random positions
        else:
             self.Board.board=start          #pre-fixed starting positions
        self.drawBoard(self.Board.board)
        pygame.display.update()
        pygame.time.delay(2000)
        self.run() #run the actual Game loop
        
    #auto run the search program     
    def run(self):
        pause=False
        end=False
        moves=self.Board.solve() #Generator
        while True: #GAME LOOP
            self.checkForQuit()
            #check for MOUSE events
            for event in pygame.event.get(): 
                if event.type == MOUSEBUTTONUP: # get MOUSE EVENT
                    x,y=self.getSpotClicked(event.pos[0],event.pos[1])
                    if not((x,y)==(None,None)):
                        pause=True if not(pause) else False
            if not(pause):
                 if not(end):
                      board,move=next(moves) #Generator next
                 if move!=None:
                      self.drawBoard(board)
                      self.slideAnimation(board,move,10) # show slide on screen
                 else:
                      end=True
                      
                 pygame.time.delay(300)
                 pygame.display.update()
                 self.clock.tick(10)
            
        #pygame.time.delay(1300)
        
    def drawBoard(self, board):
        self.display.fill((  3,  54,  73))

        for tilex in range(len(board)):
            for tiley in range(len(board[0])):
                if board[tilex][tiley]:
                    self.drawTile(tilex, tiley, board[tilex][tiley])

        left, top = self.getLeftTopOfTile(0, 0)
        width = self.BOARDWIDTH * 80
        height = self.BOARDHEIGHT * 80
        font=pygame.font.Font('freesansbold.ttf', 14)
        txtsurf=font.render("N-Tile Sliding Puzzle", True, (255,255,255))
        pygame.draw.rect(self.display, (0, 50,255), (left - 5, top - 5, width + 11, height + 11), 4)
        self.display.blit(txtsurf, (left+42,top-20))
        txtsurf=font.render("Introduction to AI", True, (255,255,255))
        self.display.blit(txtsurf, (left+32,top+height+4))

    def getLeftTopOfTile(self,tileX, tileY):
        left = self.XMARGIN + (tileX * 80) + (tileX - 1)
        top = self.YMARGIN + (tileY * 80) + (tileY - 1)
        return (left, top)
    
    def drawTile(self,tilex, tiley, number, adjx=0, adjy=0):
        # draw a tile at board coordinates tilex and tiley, optionally a few
        # pixels over (determined by adjx and adjy)
        left, top = self.getLeftTopOfTile(tilex, tiley)
        pygame.draw.rect(self.display, (  0, 204,   0), (left + adjx, top + adjy, 80, 80))
        textSurf = self.font.render(str(number), True, (255, 255, 255))
        textRect = textSurf.get_rect()
        textRect.center = left + int(80 / 2) + adjx, top + int(80 / 2) + adjy
        self.display.blit(textSurf, textRect)
    
    def slideAnimation(self,board, direction, animationSpeed):
        # Note: This function does not check if the move is valid.

        blankx, blanky = self.Board.getBlankPosition(board)
        if direction == self.Board.UP:
            movex = blankx
            movey = blanky + 1
        elif direction == self.Board.DOWN:
            movex = blankx
            movey = blanky - 1
        elif direction == self.Board.LEFT:
            movex = blankx + 1
            movey = blanky
        elif direction == self.Board.RIGHT:
            movex = blankx - 1
            movey = blanky

        # prepare the base surface
        self.drawBoard(board)
        baseSurf = self.display.copy()
        # draw a blank space over the moving tile on the baseSurf Surface.
        moveLeft, moveTop = self.getLeftTopOfTile(movex, movey)
        pygame.draw.rect(baseSurf, (  3,  54,  73), (moveLeft, moveTop, 80, 80))

        for i in range(0, 90, animationSpeed):
            # animate the tile sliding over
            self.checkForQuit()
            self.display.blit(baseSurf, (0, 0))
            if direction == self.Board.UP:
                self.drawTile(movex, movey, board[movex][movey], 0, -i)
            if direction == self.Board.DOWN:
                self.drawTile(movex, movey, board[movex][movey], 0, i)
            if direction == self.Board.LEFT:
                self.drawTile(movex, movey, board[movex][movey], -i, 0)
            if direction == self.Board.RIGHT:
                self.drawTile(movex, movey, board[movex][movey], i, 0)

            pygame.display.update()
            self.clock.tick(10)
            
    def getSpotClicked(self, x, y):
        # from the x & y pixel coordinates, get the x & y board coordinates
        for tileX in range(len(self.Board.board)):
            for tileY in range(len(self.Board.board[0])):
                left, top = self.getLeftTopOfTile(tileX, tileY)
                tileRect = pygame.Rect(left, top, 80,80)
                if tileRect.collidepoint(x, y):
                    return (tileX, tileY)
        return (None, None)
    
def main():
    game=Animation(SIZE,SIZE)
    game.startState()

if __name__ == '__main__':
    main()
