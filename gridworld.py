from random import choices

class Gridworld:

    # NOTE: 0 -> empty 1 -> blocked
    def __init__(self, dim, prob):

        # gridworld is an object attribute
        self.gridworld = []

        # start filling in grids by rows and columns
        for x in range(dim):
            for y in range(dim):
                row = []
                # first and last squares are guaranteed empty
                if (x, y) == ((0, 0) or (dim-1, dim-1)):
                    row.append(0)
                else:
                    row.append(choices([0, 1], [1-prob, prob]))
            # append the row to the gridworld
            self.gridworld.append(row)
    


