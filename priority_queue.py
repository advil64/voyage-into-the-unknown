# Queue to hold frings
from fringe_node import Fringe_Node

class Priority_Queue:
    def __init__(self):
        self.queue = []
        self.fringe_set = set()
    
    # checks if it is empty
    def is_empty(self):
        return True if len(self.queue) == 0 else False
    
    # adds a fringe node to the queue
    def enqueue(self, node):

        # check if the node exists in the queue
        for n in self.queue:
            if node.is_same(n):
                if node.distance < n.distance:
                    self.queue.remove(n)
                else:
                    return

        # add the new node into the queue
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for i, n in enumerate(self.queue):
                if n.distance < node.distance:
                    self.queue.insert(i, node)
                    return
            self.queue.append(node)

    # pops the lowest distance node from the queue
    def de_queue(self):
        return self.queue.pop()