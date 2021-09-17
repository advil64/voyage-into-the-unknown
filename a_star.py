# solves gridworld using A* algorithm
from priority_queue import Priority_Queue
from fringe_node import Fringe_Node

# contains nodes to be discovered
fringe = Priority_Queue()

# contains nodes that were visited
visited = {}

def pathfinder(grid, dim, heuristic):

    # create the first fringe node
    start = Fringe_Node((0, 0), None, heuristic((0, 0), (dim-1, dim-1)))
    fringe.append(start)

    # loop through the unvisited nodes
    while len(fringe) > 0:
        curr = fringe.pop(0)

        # Check if the goal node was popped
        if curr.curr_block == (dim-1, dim-1):
            # do stuff
            print("Path Found")
        else:
            check_neighbors(grid, dim, heuristic, curr)

    print("No Path Found")
        
            
def check_neighbors(grid, dim, heuristic, curr_node):
    curr_coord = curr_node.curr_block
    if curr_coord[0] - 1 >= 0:
        if not (curr_coord[0] - 1, curr_coord[1]) in visited:
            new_node = Fringe_Node((curr_coord[0] - 1, curr_coord[1]), curr_coord, curr_node.distance + heuristic((curr_coord[0] - 1, curr_coord[1]), (dim-1, dim-1)))
            fringe.enqueue(new_node)
    if curr_coord[0] + 1 < dim:
        if not (curr_coord[0] + 1, curr_coord[1]) in visited:
            new_node = Fringe_Node((curr_coord[0] + 1, curr_coord[1]), curr_coord, curr_node.distance + heuristic((curr_coord[0] + 1, curr_coord[1]), (dim-1, dim-1)))
            fringe.enqueue(new_node)
    if curr_coord[1] - 1 >= 0:
        if not (curr_coord[0], curr_coord[1] - 1) in visited:
            new_node = Fringe_Node((curr_coord[0], curr_coord[1] - 1), curr_coord, curr_node.distance + heuristic((curr_coord[0], curr_coord[1] - 1), (dim-1, dim-1)))
            fringe.enqueue(new_node)
    if curr_coord[1] + 1 >= dim:
        if not (curr_coord[0], curr_coord[1] + 1) in visited:
            new_node = Fringe_Node((curr_coord[0], curr_coord[1] + 1), curr_coord, curr_node.distance + heuristic((curr_coord[0], curr_coord[1] + 1), (dim-1, dim-1)))
            fringe.enqueue(new_node)