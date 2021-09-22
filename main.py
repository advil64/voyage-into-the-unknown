# used to read in command line args (dim p heuristic algo)
import argparse
from gridworld import Gridworld
from heuristics import euclidian, manhattan, chebyshev
from a_star import path_planner
from time import sleep

def solver(dim, prob, heuristic, algo):

    # create a gridworld
    complete_grid = Gridworld(dim, prob, False)
    complete_grid.print()

    # create gridworld that agent uses to take note of blocks
    discovered_grid = Gridworld(dim)

    path = []

    if heuristic == "euclidian":
        path = path_planner(complete_grid, dim, euclidian)
    
    complete_grid.update_grid(path)
    complete_grid.print()
        

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-d", "--dimension", type=int, default=5, help="dimension of gridworld")
    p.add_argument("-p", "--probability", type=float, default=0.35, help="probability of a black square")
    p.add_argument("-m", "--heuristic", type=str, default="euclidian", help="heuristic of your desired algorithm (if possible)")
    p.add_argument("-a", "--algorithm", type=str, default="a_star", help="algorithm used to traverse gridworld")

    # parse arguments and create the gridworld
    args = p.parse_args()
    
    solver(args.dimension, args.probability, args.heuristic, args.algorithm)
        

if __name__ == "__main__":
    main()