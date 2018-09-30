from player_character import PlayerCharacter
from location import Location
from exit import Exit
from location_setup import setup_locations
from interaction import Interaction

print('\nWelcome to a text adventure game!')

forest = Location('There are trees all around you. ', 'Squirrels and rabbbits run about. ')
river = Location('A river rushes past you. ', 'Fish swim in the river. ')
rock = Location('A large rock stands in front of you. ', 'The rock is about 5 feet tall. ')

# Forest
forest_to_river = Exit('east', river, 'The sounds of a river come from the east. ')
forest.add_exit(forest_to_river)
forest_to_rock = Exit('north', rock, 'A trail leads north. ')
forest.add_exit(forest_to_rock)

# Rock
rock_to_forest = Exit('south', forest, 'A trail leads south. ')
rock.add_exit(rock_to_forest)

# River
river_to_forest = Exit('west', forest, 'There is a gap in the dense forest to the west. ')
river.add_exit(river_to_forest)

location_grid = [
['d', 'f', 'p'],
['f', 'd', 'p'],
]
setup_locations(location_grid)

# pc = PlayerCharacter(location_grid[0][0])
pc = PlayerCharacter(forest)

pc.get_current_location().show()


# ask for a direction to go, then show the current location
while True:
    requested_direction = input('Where do you go?\n')
    print('')
    for exit in pc.get_current_location().get_exits():
        if exit.get_direction() == requested_direction:
            pc.set_current_location(exit.get_leads_to())
            break
        if pc.get_current_location().get_exits().index(exit) == len(pc.get_current_location().get_exits())-1:
            print('You cannot go ' + requested_direction)
            break

    pc.get_current_location().show()
