from random import choices

class Gridworld:

    # NOTE: 0 -> empty 1 -> blocked
    def __init__(self, dim, prob=0, empty=True):

        # gridworld is an object attribute
        self.gridworld = []

        # start filling in grids by rows and columns
        if empty:
            for x in range(dim):
                self.gridworld.append([0 for i in range(dim)])
        else:
            for x in range(dim):
                row = []
                for y in range(dim):
                    # first and last squares are guaranteed empty
                    if (x, y) == (0, 0) or (x, y) == (dim-1, dim-1):
                        row.append(0)
                    else:
                        row.append(choices([0, 1], [1-prob, prob])[0])
                # append the row to the gridworld
                self.gridworld.append(row)
    
    def print(self):
        for row in self.gridworld:
            print(row)

    def update_grid_with_path(self, path):
        for node in path:
            self.gridworld[node.curr_block[0]][node.curr_block[1]] = 2
    

    def update_grid_obstacle(self, coord):
        self.gridworld[coord[0]][coord[1]] = 1


