# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mysterious Voice")


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

    "I make my living by ~pick job here~"

    # This ends the game.

    return
