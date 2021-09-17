class Fringe_Node:

    # curr_block: coordinates for the block [x, y]
    # parent_block: coordinates for the block's parent block [x, y]
    # priority: g(n) + h(n)
    def __init__(self, curr_block, parent_block, distance):
        self.curr_block = curr_block
        self.parent_block = parent_block
        self.distance = distance

    def is_same(self, compare_block):
        if self.curr_block == compare_block.curr_block:
            return True

        return False

    def compare_2(self, compare_block):
        if self.distance > compare_block.distance:
            return 1
        elif self.distance < compare_block.distance:
            return -1
        
        return 0


    