from grid import Grid

grid = Grid()

print("This is an example of filling the grid acrossways.")

grid.fill_across("FLAP", (0, 0))
grid.fill_across("ROSE", (1, 0))
grid.fill_across("ARTSY", (2, 0))
grid.fill_across("DATE",  (3, 1))
grid.fill_across("EROS",  (4, 1))
print(grid)

print("Downways...")
grid.fill_down("FRA", (0, 0))
grid.fill_down("LORDE", (0, 1))
grid.fill_down("ASTAR", (0, 2))
grid.fill_down("PESTO",  (0, 3))
grid.fill_down("YES",  (2, 4))

print(grid)

print("You can also mutate directly: ")
for i in range(0, 5):
    grid[2][i] = None #Erases the word at row 2
print(grid)

#TODO
# - Error checking (especially for out of bounds)
# Validation:
#   - is grid already filled in that spot
#- check if new word is a valid fill
# - import a list of <5 letter words
#    - for testing generation/validaton of grids
