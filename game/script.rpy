# The script of the game goes in this file.

# Declare characters used by this game.
define p = Character(_("[name]"), color="#c8ffc8")
define g = Character(_("George"), color="#ffa500")

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

    python:
        name = renpy.input(_("My name is..."))

        name = name.strip() or __("Guy Shy")
 
     
    p "I'm a ~gender of choice~."

    p "I make my living by..."
    
    menu:

        "farming.":
            jump choice1_yes

        "raising goats.":
            jump choice1_no
            
    label choice1_yes:

        $ menu_flag = True

        p "Everyone in the community works hard, and I'm glad I have crops to trade with everyone."

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        p "Everyone in the community works hard, and I'm glad I have milk & cheese to trade with everyone."

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 
    

    #here's where we get into the meat of things- gotta intro the "romanceable" NPCs
    
    p "To keep up with communities further away, we settle in to listen to transmissions from across the continent"
    
    p "I listen every night, with my cat by my side"
    
    g "~purrrr~"
    
    p"Time to tune into my favorites this evening. First I think I'll listen to ~NPC choices will go here~"
    
    # This ends the game.

    return
