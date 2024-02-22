# class PriorityQueueArray:
#     def __init__(self):
#         self.queue = []

#     def __str__(self):
#         return ' '.join([str(i) for i in self.queue])

#     def insert(self, node):
#         self.queue.append(node)

#     def make_queue(self, nodes):
#         self.queue = nodes.copy()
#         for


#     def delete_min(self):
#             minIndex = 0
#             for i in range(len(self.queue)):
#                 if self.queue[i].dist < self.queue[minIndex].dist:
#                     minIndex = i
#             minNode = self.queue[minIndex]
#             del self.queue[minIndex]
#             return minNode

#     def decrease_key(self, value, priority):
#         return

#     def printQueue(self):
#         for i in self.queue:
#             print(i, end=' ')
#         print()

class PriorityQueueArray:
    def __init__(self, nodes):
        self.queue = []
        self.nodes = nodes

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def insert(self, node):
        self.queue.append(node.node_id)

    def make_queue(self, nodes):
        for node in nodes:
            self.insert(node)


    def delete_min(self):
            minIndex = 0
            for i in range(len(self.queue)):
                if self.nodes[self.queue[i]].dist < self.nodes[self.queue[minIndex]].dist:
                    minIndex = i
            del self.queue[minIndex]
            return minIndex

    def decrease_key(self, value, priority):
        return

    def printQueue(self):
        for i in self.queue:
            print(i, end=' ')
        print()