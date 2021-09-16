# used to read in command line args (dim p heuristic algo)
import argparse
from gridworld import Gridworld

def solver(dim, prob, heuristic, algo):
    
    # create a gridworld
    g = Gridworld(dim, prob)

    print(g.gridworld)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-d", "--dimension", type=int, default=5, help="dimension of gridworld")
    p.add_argument("-p", "--probability", type=float, default=0.5, help="probability of a black square")
    p.add_argument("-m", "--heuristic", type=str, default="euclidian", help="heuristic of your desired algorithm (if possible)")
    p.add_argument("-a", "--algorithm", type=str, default="A*", help="algorithm used to traverse gridworld")

    # parse arguments and create the gridworld
    args = p.parse_args()
    solver(args.dimension, args.probability, args.heuristic, args.algorithm)

if __name__ == "__main__":
    main()