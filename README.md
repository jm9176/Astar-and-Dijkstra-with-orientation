# Astar-and-Dijkstra-with-orientation

Solving shortest path problem in case robot has a defined motion (orientation)

Finding the shortest path
input = 

         [[0,0,0,0,0,G],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [S,0,0,0,0,0]]

where S and G represents start and goal position

Orientations:
    0: Towards East
    1: Towards South
    2: Towards West
    3: Towards North

Defined Motion:
Consider a car like motion where the robot can move forward, if
direction is 3, then forward left will 2 , forward right is 0,
reverse is 3, reverse left is 0 and reverse right is 2. Moreover, 
robot can move only in 6 directions

    2 3 0
    - 3 -
    0 3 2
