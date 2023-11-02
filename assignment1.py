from abc import ABCMeta, abstractmethod
import queue as Q

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

class Bottle:
    def __init__(self, capacity, initial, goal):
        self.capacity = capacity
        self.initial = initial
        self.goal = goal


def main():
    # WELCOME
    print("""
====================================================    
Solving Water Jug Problem
----------------------------------------------------

Please enter the following the 3 bottles information """)

    # BOTTLE CAPACITY
    print("\nCapacity")
    c1 = input("C1: ")
    c2 = input("C2: ")
    c3 = input("C3: ")
    capacity = [c1,c2,c3]

    # INITIAL STATE
    print("\nInitial State")
    b1 = input("B1: ")
    b2 = input("B2: ")
    b3 = input("B3: ")
    initial = [b1,b2,b3]

    # GOAL STATE
    print("\nGoal State")
    g1 = input("G1: ")
    g2 = input("G2: ")
    g3 = input("G3: ")
    goal = [g1,g2,g3]

    # CHOOSE ALGORITHM
    print("""
Algorihtm
1. BFS    | Breadth First Search
2. DFS    | Depth First Search
3. Greedy | Greedy Search
    """)

    al = input("Algorithm: ")

    def algorithm(al):
        switcher ={
            # 1: breadth_first_search()
            # 2: depth_first_search()
            # 3: greedy_search()
        }
        return switcher.get(al,"Invalid number")
    
    algorithm(al)
        

if __name__ == '__main__' : main()