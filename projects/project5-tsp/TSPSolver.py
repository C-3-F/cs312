#!/usr/bin/python3

from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
	from PyQt5.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT4':
	from PyQt4.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT6':
	from PyQt6.QtCore import QLineF, QPointF
else:
	raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))


import time
import numpy as np
from TSPClasses import *
import heapq
import itertools


class TSPSolver:
	def __init__( self, gui_view ):
		self._scenario = None

	def setupWithScenario( self, scenario ):
		self._scenario = scenario


	''' <summary>
		This is the entry point for the default solver
		which just finds a valid random tour.  Note this could be used to find your
		initial BSSF.
		</summary>
		<returns>results dictionary for GUI that contains three ints: cost of solution,
		time spent to find solution, number of permutations tried during search, the
		solution found, and three null values for fields not used for this
		algorithm</returns>
	'''

	def defaultRandomTour( self, time_allowance=60.0 ):
		results = {}
		cities = self._scenario.getCities()
		ncities = len(cities)
		foundTour = False
		count = 0
		bssf = None
		start_time = time.time()
		while not foundTour and time.time()-start_time < time_allowance:
			# create a random permutation
			perm = np.random.permutation( ncities )
			route = []
			# Now build the route using the random permutation
			for i in range( ncities ):
				route.append( cities[ perm[i] ] )
			bssf = TSPSolution(route)
			count += 1
			if bssf.cost < np.inf:
				# Found a valid route
				foundTour = True
		end_time = time.time()
		results['cost'] = bssf.cost if foundTour else math.inf
		results['time'] = end_time - start_time
		results['count'] = count
		results['soln'] = bssf
		results['max'] = None
		results['total'] = None
		results['pruned'] = None
		return results


	''' <summary>
		This is the entry point for the greedy solver, which you must implement for
		the group project (but it is probably a good idea to just do it for the branch-and
		bound project as a way to get your feet wet).  Note this could be used to find your
		initial BSSF.
		</summary>
		<returns>results dictionary for GUI that contains three ints: cost of best solution,
		time spent to find best solution, total number of solutions found, the best
		solution found, and three null values for fields not used for this
		algorithm</returns>
	'''

	def greedy(self, time_allowance=60.0, start_city=0):
		# Initialize variables
		cities = self._scenario.getCities().copy()
		ncities = len(cities)
		start_time = time.time()
		bssf = None
		solvable = True

		#Start with Empty Route
		# Iterate through cities and find the closest city to the last city in the route
		route = []
		for i in range(ncities):
			cities_copy = cities.copy()
			min_dist = math.inf
			min_city = None
			for j in range(len(cities_copy)):
				# Logic for the first city in the route. It will always be the start city
				if route == []:
					route.append(cities_copy[start_city])
					cities.remove(cities_copy[start_city])
					break
				# Find the closest city to the last city in the route
				if route[-1].costTo(cities_copy[j]) < min_dist:
					min_dist = route[-1].costTo(cities_copy[j])
					min_city = cities_copy[j]
			# If no city is found, the route is not solvable
			if min_city is None:
				if i > 0:
					solvable = False
				continue
			# Add the closest city to the route and remove it from the cities list
			route.append(min_city)
			cities.remove(min_city)
		
		# Create a TSPSolution object from the route
		bssf = TSPSolution(route) if solvable else None
		if solvable is False:
			return self.greedy(time_allowance, start_city+1)
		end_time = time.time()
		results = {}
		results['cost'] = bssf.cost if bssf is not None else math.inf
		results['time'] = end_time - start_time
		results['count'] = 1
		results['soln'] = bssf
		return results

	''' <summary>
		This is the entry point for the branch-and-bound algorithm that you will implement
		</summary>
		<returns>results dictionary for GUI that contains three ints: cost of best solution,
		time spent to find best solution, total number solutions found during search (does
		not include the initial BSSF), the best solution found, and three more ints:
		max queue size, total number of states created, and number of pruned states.</returns>
	'''

	def branchAndBound( self, time_allowance=60.0 ):
		# Initialize variables
		initial_bssf = self.getInitialBssf()
		bssfCost = initial_bssf
		bssfRoute = []
		cities = self._scenario.getCities().copy()
		start_time = time.time()
		solution_count = 0	
		max_queue_size = 0
		total_states_created = 0
		pruned_states = 0

		# Create a PartialPath object with the initial matrix
		initial_matrix = self.getInitialMatrix(cities)
		init = PartialPath([0],initial_matrix,0)

		# Create a priority queue and add the initial PartialPath object
		queue = []
		heapq.heappush(queue, init)

		# Loop through the queue until it is empty or the time allowance is reached
		while queue:
			if len(queue) > max_queue_size:
				max_queue_size = len(queue)

			p: PartialPath = heapq.heappop(queue)

			if time.time() - start_time > time_allowance:
				break
			
			
			if p.lower_bound < bssfCost:
				t = self.expandAndTest(p)
				for p_i in t:
					total_states_created += 1

					# Check if the PartialPath object is a complete route
					if len(p_i.route) == len(cities):
						cost_to_start = cities[p_i.route[-1]].costTo(cities[0])
						# If the cost of the route is less than the current bssf, update the bssf
						if p_i.cost + cost_to_start < bssfCost:
							p_i.cost += cost_to_start
							bssfCost = p_i.cost
							bssfRoute = p_i.route
							solution_count += 1
					# Otherwise, if the lower bound is less than the current bssf, add it to the queue for a potential improvement
					elif p_i.lower_bound < bssfCost:
						heapq.heappush(queue, p_i)
					# If the lower bound is greater than the current bssf, prune the state
					else:
						pruned_states += 1

		# Create a TSPSolution object from the route
		bssf = TSPSolution([cities[i] for i in bssfRoute]) if bssfRoute != [] else None

		end_time = time.time()
		results = {}
		results['cost'] = bssfCost
		results['time'] = end_time - start_time
		results['count'] = solution_count
		results['soln'] = bssf
		results['max'] = max_queue_size
		results['total'] = total_states_created
		results['pruned'] = pruned_states
		return results
	

	# Create a matrix of costs between cities
	def getInitialMatrix(self, cities):
		matrix = np.full((len(cities), len(cities)), np.inf)
		for i in range(len(cities)):
			for j in range(len(cities)):
				matrix[i,j] = cities[i].costTo(cities[j])
		return matrix

	# Get the initial BSSF. This is configurable to use a greedy tour, infinity, or a random tour
	def getInitialBssf(self):
		init = self.greedy()['cost'] # Greedy Tour
		# init = np.inf # Infinity
		# init = self.defaultRandomTour()['cost'] # Random Tour
		return init

	# Expand the PartialPath object and create new matrices for each possible route
	def expandAndTest(self, p: PartialPath):
		exp = []
		for i in range(len(p.matrix)):
			if i not in p.route:
				partial_path_matrix = p.matrix.copy()
				partial_path_matrix[p.route[-1], i] = np.inf
				for j in range(len(partial_path_matrix)):
					partial_path_matrix[p.route[-1], j] = np.inf
					partial_path_matrix[j, i] = np.inf
				partial_path = PartialPath(p.route + [i], partial_path_matrix, p.cost + p.matrix[p.route[-1], i])
				exp.append(partial_path)
		return exp







	''' <summary>
		This is the entry point for the algorithm you'll write for your group project.
		</summary>
		<returns>results dictionary for GUI that contains three ints: cost of best solution,
		time spent to find best solution, total number of solutions found during search, the
		best solution found.  You may use the other three field however you like.
		algorithm</returns>
	'''

	def fancy( self,time_allowance=60.0 ):
		pass
		