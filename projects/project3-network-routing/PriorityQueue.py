class PriorityQueueArray:
    def __init__(self, nodes):
        self.queue = []
        self.nodes = nodes

    # Insert a node into the queue
    def insert(self, node):
        self.queue.append(node.node_id)

    # Build the queue with a list of nodes
    def make_queue(self, nodes):
        for node in nodes:
            self.insert(node)

    # Remove the node with the smallest distance from the queue
    def delete_min(self):
        minIndex = 0
        nodeIndex = 0
        for i in range(len(self.queue)): # Iterate through the queue to find the node with the smallest distance
            if self.nodes[self.queue[i]].dist < self.nodes[self.queue[minIndex]].dist:
                minIndex = i
                nodeIndex = self.queue[i]
        del self.queue[minIndex] # Remove the node with the smallest distance from the queue
        return self.nodes[nodeIndex] 

    # Has no funcionality for this implementation
    def decrease_key(self, value, priority):
        return

class PriorityQueueBinaryHeap:
    def __init__(self, nodes):
        self.queue = []
        self.pointerDict = {}
        self.nodes = nodes

    # Returns the index of the parent node
    def parent(self, i):
        return (i-1)//2 
    
    # Returns the index of the left child node
    def left_child(self, i):
        return 2*i + 1
    
    # Returns the index of the right child node
    def right_child(self, i):
        return 2*i + 2
    
    # Insert a node into the heap
    def insert(self, node):
        self.queue.append(node.node_id) # Add the node to the end of the queue
        self.pointerDict[node.node_id] = len(self.queue)-1 
        self.__bubble_up(len(self.queue)-1) # Bubble up the node to its correct position
    
    # Build the queue with a list of nodes
    def make_queue(self, nodes):
        for node in nodes:
            self.insert(node)

    # Remove the node with the smallest distance from the heap
    def delete_min(self):
        if len(self.queue) == 0:
            return None
        minNode = self.nodes[self.queue[0]] # The node with the smallest distance is at the root of the heap
        self.queue[0] = self.queue[-1] # Replace the root with the last node in the heap 
        self.pointerDict[self.queue[0]] = 0
        del self.queue[-1]
        self.__bubble_down(0) # Bubble down the new root to its correct position
        return minNode
    
    # Decrease the distance of a node in the heap
    def decrease_key(self, value, priority):
        index = self.pointerDict[value.node_id]
        self.nodes[value.node_id].dist = priority # Update the distance of the node
        self.__bubble_up(index) # Bubble up the node to its correct position
        return
    
    # Helper function to swap two nodes in the heap
    def __swap(self, i, j):
        if i >= len(self.queue) or j >= len(self.queue):
            return
        self.pointerDict[self.queue[j]] = i
        self.pointerDict[self.queue[i]] = j
        tmp = self.queue[i]
        self.queue[i] = self.queue[j]
        self.queue[j] = tmp

    # Helper function to bubble up a node to its correct position
    def __bubble_up(self, i):
        # Keep bubbling until the node is at the root or its parent has a smaller distance
        while i > 0 and self.nodes[self.queue[self.parent(i)]].dist > self.nodes[self.queue[i]].dist:
            self.__swap(i, self.parent(i))
            i = self.parent(i)
    
    # Helper function to bubble down a node to its correct position
    def __bubble_down(self, i):
        # Keep bubbling until the node is a leaf or its children have a larger distance
        if i >= len(self.queue) or self.left_child(i) >= len(self.queue) or self.right_child(i) >= len(self.queue):
            return
        minIndex = i
        l = self.left_child(i)
        r = self.right_child(i)

        # Find the child with the smallest distance
        minIndex = l if self.nodes[self.queue[minIndex]].dist > self.nodes[self.queue[l]].dist else minIndex
        minIndex = r if self.nodes[self.queue[minIndex]].dist > self.nodes[self.queue[r]].dist else minIndex

        if i != minIndex:
            self.__swap(i, minIndex) # Swap the node with the child with the smallest distance
            self.__bubble_down(minIndex) # Recursively bubble down the node
        