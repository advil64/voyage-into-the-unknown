class Fringe_Node:

    # curr_block: coordinates for the block [x, y]
    # parent_block: coordinates for the block's parent block [x, y]
    # priority: g(n) + h(n)
    def __init__(self, curr_block, parent_block, priority):
        self.curr_block = curr_block
        self.parent_block = parent_block
        self.priority = priority

    