# solves gridworld using A* algorithm
from priority_queue import Priority_Queue
from fringe_node import Fringe_Node

# returns the path found as a list of tuples
def path_planner(grid, dim, heuristic):
    # contains nodes to be discovered
    fringe = Priority_Queue()

    # contains nodes that were visited
    closed = {}

    # create the first fringe node
    start = Fringe_Node((0, 0), None, heuristic((0, 0), (dim-1, dim-1)), 0)
    fringe.enqueue(start)

    # loop through the unvisited nodes
    while len(fringe.queue) > 0:
        curr = fringe.de_queue()
        closed[curr.curr_block] = curr

        # Check if the goal node was popped
        if curr.curr_block == (dim-1, dim-1):
            print("Path Found")
            path = []
            # we reached the end trace the path back to start
            x = curr
            while x.curr_block != (0,0):
                path.append(x)
                x = closed[x.parent_block]
            path.append(x)
            path.reverse()
            return path
        else:
            check_neighbors(grid, dim, heuristic, curr, fringe, closed)

    print("No Path Found")
    return []
        
            
def check_neighbors(grid, dim, heuristic, curr_node, fringe, closed):
    curr_coord = curr_node.curr_block
    # check the neighbor above the block
    if curr_coord[0] - 1 >= 0:
        if grid.gridworld[curr_coord[0] - 1][curr_coord[1]] == 0 and not (curr_coord[0] - 1, curr_coord[1]) in closed:
            new_node = Fringe_Node((curr_coord[0] - 1, curr_coord[1]), curr_coord, curr_node.dist_from_start + 1 + heuristic((curr_coord[0] - 1, curr_coord[1]), (dim-1, dim-1)), curr_node.dist_from_start + 1)
            fringe.enqueue(new_node)
    # check the neighbor below the block
    if curr_coord[0] + 1 < dim:
        if grid.gridworld[curr_coord[0] + 1][curr_coord[1]] == 0 and not (curr_coord[0] + 1, curr_coord[1]) in closed:
            new_node = Fringe_Node((curr_coord[0] + 1, curr_coord[1]), curr_coord, curr_node.dist_from_start + 1 + heuristic((curr_coord[0] + 1, curr_coord[1]), (dim-1, dim-1)), curr_node.dist_from_start + 1)
            fringe.enqueue(new_node)
    # check the neighbor left of the block
    if curr_coord[1] - 1 >= 0:
        if grid.gridworld[curr_coord[0]][curr_coord[1] - 1] == 0 and not (curr_coord[0], curr_coord[1] - 1) in closed:
            new_node = Fringe_Node((curr_coord[0], curr_coord[1] - 1), curr_coord, curr_node.dist_from_start + 1 + heuristic((curr_coord[0], curr_coord[1] - 1), (dim-1, dim-1)), curr_node.dist_from_start + 1)
            fringe.enqueue(new_node)
    # check the neighbor right of the block
    if curr_coord[1] + 1 < dim:
        if grid.gridworld[curr_coord[0]][curr_coord[1] + 1] == 0 and not (curr_coord[0], curr_coord[1] + 1) in closed:
            new_node = Fringe_Node((curr_coord[0], curr_coord[1] + 1), curr_coord, curr_node.dist_from_start + 1 + heuristic((curr_coord[0], curr_coord[1] + 1), (dim-1, dim-1)), curr_node.dist_from_start + 1)
            fringe.enqueue(new_node)