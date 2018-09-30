from location import Location
from exit import Exit

# This function converts a grid of standard locations into a combination of Locations and Exits that link to each other
# 'd' = Desert
# 'f' = Forest
# 'p' = Plain
#
def setup_locations(location_grid):
    # Replace the markers with actual locations
    for r in range(len(location_grid)):
        for c in range(len(location_grid[r])):
            location_marker = location_grid[r][c]
            markers = {
            'd': Location('You find yourself in the middle of a desert. ', 'The sun drains you of your energy. '),
            'f': Location('You are in the dense brush of a forest. ', 'Birds caw and insects buzz around you. '),
            'p': Location('Knee-high grass surrounds you. ', 'There is nobody in sight. '),
            }
            location = markers[location_marker]
            location_grid[r][c] = location

    # Add Exits to the Locations based on their positions
    for r in range(len(location_grid)):
        for c in range(len(location_grid[r])):
            location = location_grid[r][c]
            if r != 0:
                exitN = Exit('north', location_grid[r-1][c], '')
                location.add_exit(exitN)
            if r != len(location_grid)-1:
                exitS = Exit('south', location_grid[r+1][c], '')
                location.add_exit(exitS)
            if c != 0:
                exitW = Exit('west', location_grid[r][c-1], '')
                location.add_exit(exitW)
            if c != len(location_grid[r])-1:
                exitE = Exit('east', location_grid[r][c+1], '')
                location.add_exit(exitE)
