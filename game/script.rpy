# The script of the game goes in this file.

# Declare characters used by this game.
define p = Character(_("player character"), color="#c8ffc8")
define g = Character(_("George"), color="#ffa500f")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # This is the introduction

    "It's the year 20XX. Things are very different now. After the war, things became much more simple."

    "This is the community where I live. Arcadia"

    #begin multiple choice section here.

    "I'm Player Character. I'm a ~gender of choice~."

    "I make my living by ~pick job here~."
    
    "Everyone in the community works hard, and I'm glad I have ~insert goods based on job choice~ to trade with everyone."

    #here's where we get into the meat of things- gotta intro the "romanceable" NPCs
    
    "To keep up with communities further away, we settle in to listen to transmissions from across the continent"
    
    "I listen every night, with my cat by my side"
    
    "Time to tune into my favorites this evening. First I think I'll listen to ~NPC choices will go here~"
    
    # This ends the game.

    return
