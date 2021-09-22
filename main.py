# used to read in command line args (dim p heuristic algo)
import argparse
from gridworld import Gridworld
from heuristics import euclidian, manhattan, chebyshev
from a_star import path_planner
from time import sleep, time

def solver(dim, prob, heuristic, algo):

    # create a gridworld
    complete_grid = Gridworld(dim, prob, False)
    complete_grid.print()

    # create gridworld that agent uses to take note of blocks
    discovered_grid = Gridworld(dim)

    final_path = []

    if heuristic == "euclidian":
        starting_time = time()
        # start planning a path from the starting block
        new_path = path_planner((0,0), discovered_grid, dim, euclidian)
        # while A* finds a new path
        while len(new_path) > 0:
            # execute the path
            new_path = execute_path(new_path, complete_grid, discovered_grid, dim)
            # get the last unblocked block
            last_node = new_path.pop()
            last_unblock = last_node.curr_block
            # append the rest to the final path
            final_path.extend(new_path)
            # check if the path made it to the goal node
            if last_unblock == (dim-1, dim-1):
                final_path.append(last_node)
                break
            # create a new path from the last unblocked node
            new_path = path_planner(last_unblock, discovered_grid, dim, euclidian)

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
            # remove the path starting with the blocked node
            path = path[:index]
            return path
        # update knowledge of neighbor blocks
        update_neighbor_obstacles(curr, discovered_grid, complete_grid, dim)
    return path


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
    p.add_argument("-p", "--probability", type=float, default=0.1, help="probability of a black square")
    p.add_argument("-m", "--heuristic", type=str, default="euclidian", help="heuristic of your desired algorithm (if possible)")
    p.add_argument("-a", "--algorithm", type=str, default="a_star", help="algorithm used to traverse gridworld")

    # parse arguments and create the gridworld
    args = p.parse_args()
    
    solver(args.dimension, args.probability, args.heuristic, args.algorithm)
        

if __name__ == "__main__":
    main()