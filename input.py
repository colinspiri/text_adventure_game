def command_go(requested_direction):
    print('')
    for exit in pc.get_current_location().get_exits():
        if exit.get_direction() == requested_direction:
            pc.set_current_location(exit.get_leads_to())
            break
        if pc.get_current_location().get_exits().index(exit) == len(pc.get_current_location().get_exits())-1:
            print('You cannot go ' + requested_direction)
            break
    pc.get_current_location().show()

def look_for_input():
    command_input = raw_input('> ')

    # If current location has interactions, terate over Interactions to check for matching input
    if pc.get_current_location().get_interactions() != []:
        for interaction in pc.get_current_location().get_interactions():
            if command_input == interaction.get_name():
                interaction.interact()

    # Check input for command words
    if command_input.startswith('go'):
        requested_direction = command_input[3:]
        command_go(requested_direction)
    elif command_input == 'look':
        pc.get_current_location().show()
