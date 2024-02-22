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
        # TODO: RETURN THE SHORTEST PATH FOR destIndex
        #       INSTEAD OF THE DUMMY SET OF EDGES BELOW
        #       IT'S JUST AN EXAMPLE OF THE FORMAT YOU'LL 
        #       NEED TO USE
        path_edges = []
        total_length = 0
        node = self.network.nodes[destIndex]
        while node is not None:
            prev = node.prev
            if prev is None:
                break
            for edge in prev.neighbors:
                if edge.dest.node_id == node.node_id:   
                    path_edges.append( (edge.src.loc, edge.dest.loc, '{:.0f}'.format(edge.length)) )
                    total_length += edge.length
            node = node.prev
        # if node.dist == float('inf'):
        #     return {'cost':float('inf'), 'path':[]}
        return {'cost':total_length, 'path':path_edges}

    def computeShortestPaths( self, srcIndex, use_heap=False ):
        self.source = srcIndex
        t1 = time.time()
        # TODO: RUN DIJKSTRA'S TO DETERMINE SHORTEST PATHS.
        #       ALSO, STORE THE RESULTS FOR THE SUBSEQUENT
        #       CALL TO getShortestPath(dest_index)

        #print("Running Dijkstra's")
        if use_heap:
            q = None
        else:
            q = PriorityQueueArray(self.network.nodes)
        
        for node in self.network.nodes:
            node.dist = float('inf')
            node.prev = None
        self.network.nodes[srcIndex].dist = 0

        q.make_queue(self.network.nodes)

        while len(q.queue) > 0:
            minIndex = q.delete_min()
            u = self.network.nodes[minIndex]
            for edge in u.neighbors:
                dest = edge.dest
                if u.dist + edge.length < dest.dist:
                    dest.dist = u.dist + edge.length
                    dest.prev = u
                    q.decrease_key(dest, dest.dist)

        t2 = time.time()
        return (t2-t1)

