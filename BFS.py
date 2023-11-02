from abc import ABCMeta, abstractmethod
import queue as Q

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def add(self, item):
        self.items.insert(0, item)
    def get(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

#Solver class
class Solver(metaclass=ABCMeta):
    @abstractmethod
    def get(self):
        raise notImplementedError()
    @abstractmethod
    def add(self):
        raise NotImplementedError()


#Breadth-first search
class Solver1(Solver):
    def __init__(self):
        self.queue = Queue()
    def get(self):
        return self.queue.get()
    def add(self, state):
        self.queue.add(state)
    def size(self):
        return self.queue.size()

class Solver3(Solver):
    def __init__(self, start, goal):

        def heuristic(self, state):
            #start state
            a, b, c = self.s[0], self.s[1], self.s[2]
            
            #current state (n)
            b1, b2, b3 = state[0], state[1], state[2]
            
            #goal
            g1, g2, g3 = self.g[0], self.g[1], self.g[2]
            
            heuristic1 = abs(b1-g1)
            
            return heuristic2

#globals 
found = False

class Bottle:
    def __init__(self, capacity, startState, goalState):
        self.capacity = capacity
        self.startState = startState
        self.goalState = goalState
        
        # ADD SOLVERS HERE
        self.Solver = Solver1()   #BFS

     
    
    def solve(self):
        global found
        self.visited = [] #visited node
        self.Solver.add(self.startState) #add the state to the solver
        state_eval = self.Solver.get()  #visit/solve this state
        cost = 0
        
        print("------------------------------------------")
        print("\n  Start State:", startState, "\n Goal State:", self.goalState)
        print("------------------------------------------")
        

        while not (found):
            # we only continue if we're not at the goal
            if state_eval != self.goalState:
                temp = self.chooseAction(state_eval)
                print("\n Exploring State", state_eval)
                
                
                #add into self.visited if never visited
                if(state_eval not in self.visited):
                    self.visited.append(state_eval)
                
                for i in temp:
                    if not (i in self.visited):
                        self.Solver.add(i)
                        
                        # add to visited
                        self.visited.append(i)
                        yield i
                        if (i == self.goalState):
                            print("\nReach Goal State:", i)

                            found = True
                            break
                state_eval = self.Solver.get() #get new state to visit
            else:
                print("Found goal state.")
                found = True
                    
        yield "Task Completed"
        
    # Operators    
    def chooseAction(self, state_eval):
    # include your conditions here

        c1 = self.capacity[0]
        c2 = self.capacity[1]
        c3 = self.capacity[2]
    #
        b1 = state_eval[0]
        b2 = state_eval[1]
        b3 = state_eval[2]
    #
    #
        #empty the bottles
        if(b1 > 0 and found == False):
            #print("empty b1")
            state = (c1, b2, b3)
            states.append(state)
            
        if(b2 > 0 and found == False):
            #print("empty b2")
            state = (b1, c2, b3)
            states.append(state)

        if(b3 > 0 and found == False):
            #print("empty b3")
            state = (b1, b2, c3)
            states.append(state)
        
        #Transfer
        if(b1>0 and b2<c2):
            #print("Transfer from B1 to B2")
            if(b1+b2<=c2):
                state(0,b1+b2,b3)
            
            
    def main():
        bot = Bottle((10,6,5), (10,0,0), (8,0,0))
        b = bot.solve()
        for i in b:
            print(i) 
        

#run the program            
Bottle.main()