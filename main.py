# used to read in command line args (dim p heuristic algo)
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-d", "--dimension", type=int, default=100, help="dimension of gridworld")
    p.add_argument("-p", "--probability", type=float, default=0.5, help="probability of a black square")
    p.add_argument("-h", "--heuristic", type=str, default="euclidian", help="heuristic of your desired algorithm (if possible)")
    p.add_argument("-a", "--algorithm", type=str, default="A*", help="algorithm used to traverse gridworld")

if __name__ == "__main__":
    main()