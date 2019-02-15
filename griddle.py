GRID_SIZE = 5
ACROSS = 0
DOWN = 1

grid = [None]*GRID_SIZE
for x in range(0, GRID_SIZE):
    grid[x] = [None]*GRID_SIZE

def show(grid):
    print("- " * (GRID_SIZE+2))
    for row in grid:
        print('|', end=' ')
        for box in row:
            if box is None:
                print(u"\u25A0", end=' ')
            else:
                print(box, end=' ')
        print('|')
    print("- " * (GRID_SIZE+2))

def fill(grid, word, start, end):
    filltype = None
    if start[0] == end[0]:
        filltype = ACROSS
    elif start[1] == end[1]:
        filltype = DOWN
    else:
        raise ValueError("Coords don't compute")

    cursor = start

    if filltype == ACROSS:
        for w in word:
            grid[cursor[0]][cursor[1]] = w
            cursor = (cursor[0], cursor[1]+1)

    if filltype == DOWN:
        pass

fill(grid, "FLAP",  (0, 0), (0,3))
fill(grid, "ROSE",  (1, 0), (1,3))
fill(grid, "ARTSY", (2, 0), (2,4))
fill(grid, "DATE",  (3, 1), (3,4))
fill(grid, "EROS",  (4, 1), (4,4))
show(grid)
