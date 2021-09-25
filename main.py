# used to read in command line args (dim p heuristic algo)
import argparse
from gridworld import Gridworld
from heuristics import euclidian, manhattan, chebyshev
from a_star import path_planner
from time import sleep, time

def repeated_solver(dim, prob, heuristic):

    # create a gridworld
    complete_grid = Gridworld(dim, prob, False)
    complete_grid.print()

    # create gridworld that agent uses to take note of blocks
    discovered_grid = Gridworld(dim)

    final_path = None

    if heuristic == "chebyshev":
        heuristic_pointer = chebyshev
    elif heuristic == "manhattan":
        heuristic_pointer = manhattan
    else:
        heuristic_pointer = euclidian

    starting_time = time()
    # start planning a path from the starting block
    new_path = path_planner((0,0), final_path, discovered_grid, dim, heuristic_pointer)
    # while A* finds a new path
    while len(new_path) > 0:
        # execute the path
        last_node = execute_path(new_path, complete_grid, discovered_grid, dim)
        final_path = last_node
        # get the last unblocked block
        last_block = (0,0)
        last_unblock_node = None
        if last_node:
            last_block = last_node.curr_block
            last_unblock_node = last_node.parent_block
        # check if the path made it to the goal node
        if last_block == (dim-1, dim-1):
            break
        # create a new path from the last unblocked node
        new_path = path_planner(last_block, last_unblock_node, discovered_grid, dim, heuristic_pointer)

    print("Completed in %s seconds" % (time() - starting_time))
    
    complete_grid.update_grid_with_path(final_path)
    complete_grid.print()
   
        
def execute_path(path, complete_grid, discovered_grid, dim):
    for index, node in enumerate(path):
        curr = node.curr_block
        # check if path is blocked
        if complete_grid.gridworld[curr[0]][curr[1]] == 1:
            # update our knowledge of blocked nodes
            discovered_grid.update_grid_obstacle(curr)
            return node.parent_block
        # update knowledge of neighbor blocks
        update_neighbor_obstacles(curr, discovered_grid, complete_grid, dim)
    return path[-1]

def known_grid_solver(dim, prob, heuristic):

    # create a gridworld
    complete_grid = Gridworld(dim, prob, False)
    # complete_grid.print()

    final_path = None

    if heuristic == "chebyshev":
        heuristic_pointer = chebyshev
    elif heuristic == "manhattan":
        heuristic_pointer = manhattan
    else:
        heuristic_pointer = euclidian

    starting_time = time()
    # start planning a path from the starting block
    new_path = path_planner((0,0), final_path, complete_grid, dim, heuristic_pointer)
    
    if new_path:
        final_path = new_path[-1]
        print("Completed in %s seconds" % (time() - starting_time))
        
        complete_grid.update_grid_with_path(final_path)
    
    # complete_grid.print()

def update_neighbor_obstacles(curr, discovered_grid, complete_grid, dim):
    # check the neighbor above the block
    if curr[0] - 1 >= 0:
        if complete_grid.gridworld[curr[0] - 1][curr[1]] == 1:
            discovered_grid.update_grid_obstacle((curr[0] - 1, curr[1]))
    # check the neighbor below the block
    if curr[0] + 1 < dim:
        if complete_grid.gridworld[curr[0] + 1][curr[1]] == 1:
            discovered_grid.update_grid_obstacle((curr[0] + 1, curr[1]))
    # check the neighbor left of the block
    if curr[1] - 1 >= 0:
        if complete_grid.gridworld[curr[0]][curr[1] - 1] == 1:
            discovered_grid.update_grid_obstacle((curr[0], curr[1] - 1))
    # check the neighbor right of the block
    if curr[1] + 1 < dim:
        if complete_grid.gridworld[curr[0]][curr[1] + 1] == 1:
            discovered_grid.update_grid_obstacle((curr[0], curr[1] + 1))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-d", "--dimension", type=int, default=10, help="dimension of gridworld")
    p.add_argument("-p", "--probability", type=float, default=0.33, help="probability of a black square")
    p.add_argument("-m", "--heuristic", type=str, default="euclidian", help="heuristic of your desired algorithm (if possible)")
    p.add_argument("-a", "--algorithm", type=str, default="repeated_a_star", help="algorithm used to traverse gridworld")

    # parse arguments and create the gridworld
    args = p.parse_args()
    
    if args.algorithm == "a_star":
        known_grid_solver(args.dimension, args.probability, args.heuristic)
    elif args.algorithm == "repeated_a_star":
        repeated_solver(args.dimension, args.probability, args.heuristic)
        

if __name__ == "__main__":
    main()