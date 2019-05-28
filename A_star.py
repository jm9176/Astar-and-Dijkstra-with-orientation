'''
Finding the shortest path
input = [[0,0,0,0,0,G],
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
reverse is 3, reverse left is 0 and reverse right is 2
    2 3 0
    - 3 -
    0 3 2
'''

import numpy as np
from Node import Node
from chkNode import chk_Node
from retrace_path import retrace_path
import matplotlib.pyplot as plt


# Calculating heuristic using distance formula
def distance(point_a, point_b):
    return pow(pow(point_a.x - point_b.x, 2) + pow(point_a.y - point_b.y, 2), 0.5)


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
    f_cost[start.x][start.y] = distance(start, goal)

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
            f_cost[var.x][var.y] = g_cost[var.x][var.y] + distance(var, goal)



# Initialize the input grid, start and end goal
# n_r, n_c represents the no. of rows and cols in a grid
n_r, n_c = 20, 20
grid = np.full([n_r,n_c], 0, dtype = float)

# Defining the obstacles
grid[7:11, 7:11] = 1
grid[2:4, 2:10] = 1

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]==0:
            plt.plot(i,j, color = 'azure', marker = 'o')
        else:
            plt.plot(i,j, color = 'red', marker = 'o')

start = Node(3,0, 0)
goal = Node(15, 15,1)

final_list = finding_path(grid, start, goal, n_r, n_c)

for var in final_list:
    if var.o == 0:
        plt.arrow(var.x, var.y, 0.0, 0.5, fc = "k", ec = "k",
                  head_width = 0.1, head_length = 0.1)
    elif var.o == 1:
        plt.arrow(var.x, var.y, 0.5, 0.0, fc="k", ec="k",
                  head_width=0.1, head_length=0.1)
    elif var.o == 2:
        plt.arrow(var.x, var.y, 0.0, -0.5, fc="k", ec="k",
                  head_width=0.1, head_length=0.1)
    elif var.o == 3:
        plt.arrow(var.x, var.y, -0.5, 0.0, fc="k", ec="k",
                  head_width=0.1, head_length=0.1)

plt.show()

