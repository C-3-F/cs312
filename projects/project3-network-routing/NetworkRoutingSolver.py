#!/usr/bin/python3


from CS312Graph import *
from PriorityQueue import *
import time


class NetworkRoutingSolver:
    def __init__( self):
        pass

    def initializeNetwork( self, network ):
        assert( type(network) == CS312Graph )
        self.network = network

    def getShortestPath( self, destIndex ):
        self.dest = destIndex


        path_edges = []
        #Set start node as the destination node
        node = self.network.nodes[destIndex]
        total_length = node.dist

        # Work backwards from the destination node to the source node
        while node is not None:
            prev = node.prev
            if prev is None: # Found the source node
                break
            for edge in prev.neighbors: # Find the edge that connects the previous node to the current node
                if edge.dest.node_id == node.node_id:   
                    path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
            node = node.prev # Move to the previous node
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        if use_heap:
            q = PriorityQueueBinaryHeap(self.network.nodes)
        else:
            q = PriorityQueueArray(self.network.nodes)
        
        # Initialize all nodes with distance of infinity and no previous node
        for node in self.network.nodes:
            node.dist = float('inf')
            node.prev = None
        self.network.nodes[srcIndex].dist = 0

        # Build and populate queue object with all nodes
        q.make_queue(self.network.nodes)

        # Run Dijkstra's algorithm iteratively removing the node with the smallest distance
        while len(q.queue) > 0:
            u = q.delete_min()
            # Find each neighbor of the current node and update its distance if it is less than the current distance
            for edge in u.neighbors:
                dest = edge.dest
                if u.dist + edge.length < dest.dist:
                    dest.dist = u.dist + edge.length
                    dest.prev = u
                    # Decrease the key of the node in the queue
                    q.decrease_key(dest, dest.dist)

        t2 = time.time()
        return (t2-t1)

