from Node import Node

# Defining the traversable node
def chk_Node(curr_var, grid, n_r, n_c):
    final_edge_list = []
    edge_list = edge(curr_var)

    # stateent to check if the node lies within the grid and
    # if it is a valid node and not an obstacle
    for var in edge_list:
        if var.x < n_r and var.y < n_c and var.x>=0 and var.y>=0:
            if grid[var.x][var.y] == 0:
                final_edge_list.append(var)
            
    return final_edge_list


# Defining the edges
def edge(curr_var):

    x_c = curr_var.x
    y_c = curr_var.y
    o_c = curr_var.o

    # Appending the neighboring nodes all at once 
    if o_c == 0:
        edge_list = [Node(x_c - 1, y_c + 1, 3), Node(x_c, y_c + 1, 0),
                     Node(x_c + 1, y_c + 1, 1), Node(x_c - 1, y_c - 1, 1),
                     Node(x_c, y_c - 1, 0), Node(x_c + 1, y_c - 1, 3)]

    elif o_c == 1:
        edge_list = [Node(x_c + 1, y_c + 1, 0), Node(x_c + 1, y_c, 1),
                     Node(x_c + 1, y_c - 1, 2), Node(x_c - 1, y_c + 1, 2),
                     Node(x_c - 1, y_c, 1), Node(x_c - 1, y_c - 1, 0)]

    elif o_c == 2:
        edge_list = [Node(x_c + 1, y_c - 1, 1), Node(x_c, y_c - 1, 2),
                     Node(x_c - 1, y_c - 1, 3), Node(x_c - 1, y_c + 1, 1),
                     Node(x_c, y_c + 1, 2), Node(x_c + 1, y_c + 1, 3)]

    elif o_c == 3:
        edge_list = [Node(x_c - 1, y_c + 1, 0), Node(x_c - 1, y_c, 3),
                     Node(x_c - 1, y_c - 1, 2), Node(x_c + 1, y_c + 1, 2),
                     Node(x_c + 1, y_c, 3), Node(x_c + 1, y_c - 1, 0)]


    return edge_list
