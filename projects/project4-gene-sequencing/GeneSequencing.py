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

import random

# Used to compute the bandwidth for banded version
MAXINDELS = 3

# Used to implement Needleman-Wunsch scoring
MATCH = -3
INDEL = 5
SUB = 1

class GeneSequencing:

	def __init__( self ):
		pass

# This is the method called by the GUI.  _seq1_ and _seq2_ are two sequences to be aligned, _banded_ is a boolean that tells
# you whether you should compute a banded alignment or full alignment, and _align_length_ tells you
# how many base pairs to use in computing the alignment

	def align( self, seq1, seq2, banded, align_length):
		self.banded = banded
		self.MaxCharactersToAlign = align_length


		if len(seq1) > len(seq2):
			seq1, seq2 = seq2, seq1
		n = self.MaxCharactersToAlign if len(seq1) > self.MaxCharactersToAlign else len(seq1)
		m = self.MaxCharactersToAlign if len(seq2) > self.MaxCharactersToAlign else len(seq2)

		if self.banded:
			score, backtrack = self.bandedAlgorithm(seq1[:n], seq2[:m], MAXINDELS)
		else:
			score, backtrack = self.unrestrictedAlgorithm(seq1[:n], seq2[:m])

		alignment1, alignment2 = self.constructAlignment(seq1[:n], seq2[:m], backtrack)

		return {'align_cost':score, 'seqi_first100':alignment1, 'seqj_first100':alignment2}
	
	def unrestrictedAlgorithm(self, seq1: str, seq2: str):

		# Initialize variables
		n = len(seq1)
		m = len(seq2)
		backtrack = []

		# Create a 2D array to store the cost of the alignment
		arr = self.initArray(n, m, -1)


		# Solve
		# Loop through the rows
		for i in range(1, n + 1):
			# Loop through the columns
			for j in range(1, m + 1):

				# Determine the minimum value of the left, up, and upLeft values
				arr[i][j], val = self.min_with_index(self.left(arr, i, j) + INDEL, self.upLeft(arr, i, j) + self.cost(seq1[i - 1], seq2[j - 1]), self.up(arr, i, j) + INDEL)
				
				# Determine the operation and add it to the backtrack list
				if val == 0:
					backtrack.append('INS')
				elif val == 1:
					backtrack.append('SUB')
				else:
					backtrack.append('DEL')
		
		# Return the score and the backtrack list
		return arr[n][m], backtrack




	def bandedAlgorithm(self, seq1: str, seq2: str, band: int):
		#Initialize variables
		n = len(seq1)
		m = len(seq2)
		k = 2 * band + 1
		backtrack = []

		# Create a 2D array to store the cost of the alignment
		arr = self.initArray(n, m, band, k)

		# Solve

		# If we are reaching the end of the sequence, we need to skip some columns
		skip = 0 

		# Loop through the rows
		for i in range(1, n + 1):

			# Col is the index of the column in the n * k array wheras j is the index of the column in the original sequence
			col = 1

			# Determine how many columns to skip based upon the current row
			if i > n - band:
				skip += 1

			# Loop through the columns
			for j in range(i - band, i + band + 1):

				# The current column we are working on is the col value + the number of columns we have skipped
				index = col + skip

				# If we are at the beginning, then we skip the column indexes that are less than 1
				if j < 1:
					continue

				# If we are at the end, then we skip the column indexes that are greater than k
				if index > k:
					break

				# If we are in the rows that don't have the full band, we check the values to the left, up, and upLeft
				if i <= band + 1 or i > n - band:
					arr[i][index], val = self.min_with_index(self.left(arr, i, index) + INDEL, (self.upLeft(arr,i,index) + self.cost(seq1[i - 1], seq2[j - 1])), self.up(arr, i, index) + INDEL)

				# If we are in the rows that have the full band, we check the values to the left, up, and upRight
				else:
					arr[i][index], val = self.min_with_index(self.left(arr, i, index) + INDEL, (self.up(arr, i, index) + self.cost(seq1[i - 1], seq2[j - 1])), (float('inf') if j >= k else self.upRight(arr, i, j) + INDEL))
				
				# Determine the operation and add it to the backtrack list
				if val == 0:
					backtrack.append('INS')
				elif val == 1:
					backtrack.append('SUB')
				else:
					backtrack.append('DEL')

				# Increment the column index
				col += 1
		
		# Return the score and the backtrack list
		return arr[n - 1][k - 1], backtrack
				

		

		



	def initArray(self, n: int, m: int, band: int, k: int = 0):
		arr = []
		if band != -1:

			#initialize the first row and column for banded
			for i in range(n + 1):
				arr.append([float('inf')] * (k + 1))
			for i in range(band + 1):
				arr[i][0] = i * INDEL
				arr[0][i] = i * INDEL

		else:
			#initialize the first row and column for unbanded
			for i in range(n + 1):
				arr.append([0] * (m + 1))
				arr[i][0] = i * INDEL

			for i in range(m + 1):
				arr[0][i] = i * INDEL

		return arr
	
	def constructAlignment(self, seq1: str, seq2: str, backtrack: list):
	# 	last = backtrack.pop()
	# 	alignment1 = ''
	# 	alignment2 = ''
	# 	while len(backtrack) > 0:
	# 		i, j = backtrack.pop()
	# 		if i == last[0] - 1 and j == last[1] - 1:
	# 			alignment1 = seq1[i] + alignment1
	# 			alignment2 = seq2[j] + alignment2
	# 		elif i == last[0] and j == last[1] - 1:
	# 			alignment1 = '-' + alignment1
	# 			alignment2 = seq2[j] + alignment2
	# 		else:
	# 			alignment1 = seq1[i] + alignment1
	# 			alignment2 = '-' + alignment2
	# 	return alignment1, alignment2
		return '', ''
		
	def left(self, arr: list, i: int, j: int):
		return arr[i][j - 1]
	
	def up(self, arr: list, i: int, j: int):
		return arr[i - 1][j]
	
	def upLeft(self, arr: list, i: int, j: int):
		return arr[i - 1][j - 1]
	
	def upRight(self, arr: list, i: int, j: int):
		return arr[i - 1][j + 1]

	def cost(self, a: str, b: str):
		if a == b:
			return MATCH
		else:
			return SUB
		
	def min_with_index(self, *args):
		# Check if there are any arguments provided
		if not args:
			raise ValueError("min_with_index() arg is an empty sequence")

		# Find the minimum value among the arguments
		min_value = min(args)
		
		# Find the index of the minimum value
		# Note: The first occurrence of the minimum value is returned in case of duplicates
		min_index = args.index(min_value)
		
		# Return both the minimum value and its index (position among the arguments)
		return min_value, min_index