class Grid():
	def __init__(self, size=5):
		self._grid =[None]*size
		for x in range(0, size):
			self._grid[x] = [None]*size

	def __len__(self):
		return len(self._grid)

	def __getitem__(self, position):
		return self._grid[position]

	def __repr__(self):
		size = len(self._grid)
		grid = ("- " * (size+2) + "\n")
		for row in self._grid:
			grid += '| '
			for box in row:
				if box is None:
					grid += u"\u25A0 "
				else:
					grid += (box + ' ')
			grid += '|\n'
		grid += ("- " * (size+2) + "\n")
		return grid

	def fill_across(self, word, start):
		end = (start[0], start[0]+len(word))
		self.fill(word, start, end)

	def fill_down(self, word, start):
		end = [start[1]+len(word), start[1]]
		self.fill(word, start, end)

	def fill(self, word, start, end):
		if start[0] == end[0]:
			type = "across"
		elif start[1] == end[1]:
			type = "down"
		else:
			raise ValueError()

		cursor = start
		if type == "across":
			for w in word:
				self._grid[cursor[0]][cursor[1]] = w
				cursor = (cursor[0], cursor[1]+1)
		if type == "down":
			for w in word:
				self._grid[cursor[0]][cursor[1]] = w
				cursor = (cursor[0]+1, cursor[1])
