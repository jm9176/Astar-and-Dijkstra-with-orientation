'''
Finding the shortest path
input = [[0,0,0,0,0,G],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [S,0,0,0,0,0]]

where S and G represents start and goal position
'''

import numpy as np
from Node import Node
from chkNode import chk_Node
from retrace_path import retrace_path

    
# Calculating heuristic using distance formula
def distance(point_a, point_b):
    return pow(pow(point_a.x - point_b.x,2)+pow(point_a.y - point_b.y,2),0.5)


# Calculating the shortest path
def finding_path(grid, start, goal, n_r, n_c):

    # Initializing the closed and open list
    # dict_parent to store the previous (parent) node
    closed_list = []
    open_list = [start]
    dict_parent = {}

    # Initializing the g_cost and f_cost matrix
    g_cost = [[np.inf for i in range(n_c)] for j in range(n_r)]
    f_cost = [[np.inf for i in range(n_c)] for j in range(n_r)]


    # Initializing the g_cost for start = 0 and
    # f_cost = distance bewteen start and goal
    # f_cost = g_cost[start] + distance(start, goal)
    g_cost[start.x][start.y] = 0
    f_cost[start.x][start.y] = 0


    while open_list is not None:
        # Initializing the initial selection with the first node in the
        # open list. Later, using the other nodes, finding the node with
        # the low f_cost_value by comparing with the initial selection
        curr_f_cost = f_cost[open_list[0].x][open_list[0].y]
        curr_var = open_list[0]

        for var in open_list:
            if f_cost[var.x][var.y] < curr_f_cost:
                curr_f_cost = f_cost[var.x][var.y] 
                curr_var = var


        # if goal is found, retrace the path
        if curr_var == goal:
            return retrace_path(dict_parent, curr_var, start)
            
        open_list.remove(curr_var)
        closed_list.append(curr_var)


        # Finding the neighbor nodes of the current selection
        edges = chk_Node(curr_var, grid, n_r, n_c)

        # Updating the g_cost and f_cost of the nodes
        # to find the shortest path
        for var in edges:
            if var in closed_list:
                 continue

            temp_g_cost = g_cost[curr_var.x][curr_var.y] + distance(curr_var, var)

            if var not in open_list:
                open_list.append(var)
                
            elif temp_g_cost >= g_cost[var.x][var.y]:
                continue
            
            dict_parent[var] = curr_var

            g_cost[var.x][var.y] = temp_g_cost
            f_cost[var.x][var.y] = g_cost[var.x][var.y]


# Initialize the input grid, start and end goal
# n_r, n_c represents the no. of rows and cols in a grid
n_r, n_c = 4, 6         
grid = [[0 for i in range(n_c)] for j in range(n_r)]

# Defining the obstacles
#grid[1][2] = 1
#grid[2][2] = 1
#grid[1][4] = 1
#grid[2][4] = 1

start = Node(3,0,0)
goal = Node(0,4,1)

print(finding_path(grid, start, goal, n_r, n_c))


