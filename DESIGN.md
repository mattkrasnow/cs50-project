# Design CS50-Project
This is our CS50 project! 

## Table of Contents

- [Premise](#premise)
- [Project Manual](#project-manual)
    - [block.py]



## PREMISE:
Our project is a Pygame video game that features our class's mascot: the infamous CS50 duck! However, it has a problem! Hackers at MIT, jealous of Harvard and Yale's course, destroyed CS50. Now, it's overrun with MIT beavers that are keeping CS50 in shambles. Our hero must adventure through MIT's tricks and puzzles to finally reclaim our favorite introduction to computer science!


## PROJECT MANUAL:

In the following sections, we will discuss the functionality of our code.

## Code:
The following files are the essence of our game: the python files that create the user interface and experience. 


## block.py
Overview: 
The block.py file allows for the creation of blocks in main. Ingame, blocks are immovable black rectangles that act as obstacles to the player. They also can act as platforms. They are solid objects that are opaque to all entities. 

Contruction: 
block.py has a Block contructor that allows for the creation of new Block objects. Each block object represents an individual block on an individual level. Blocks must have a set position on screen, as dictated by the parameters x and y. As rectangles, they must also have set width and heights, as dictated by the parameters w and h.

Functions:
.display 
When called through a Block object, the .display function shows the block on the win parameter, a window on the user's device. 

.objectCollision
When called through a block object, the .object collision function checks if the block is in contact with another entity(player or enemy). This prevents entities from passing through blocks, allows them to stand/jump on blocks. Essentially, giving each level structure. 

## boss.py
Overview: The boss.py file allows for the creation of the final boss. In game, the boss is an entity displayed with a health bar and the MIT logo. It is the final enemy and the end of the game.

Construction:
The boss is constructed with the MIT beaver, fitted to the screen, with full health, at a set point on the screen. It also holds the booleans that tell if the level has been completed. It also acts as an Enemy object, which is logical because it is intuitively a special type of enemy. 

Functions:
.populateEnemies
Starts the level with the boss at full health.

.levelPyhsics
Just like all other levels, this functions defines the physics of the game such as object collisions, collisions with the window, collisions with blocks. It keeps the boss in screen, prevents that from moving through blocks and the player.

.bulletCollisions
When the user shoots the boss the boss takes damage to the leahbar, the bullet dissapears, and the level ends if the boss dies. 

.display
Displays the boss on the screen with its healthbar. Displays the blocks in the level as well. 


## bullet.py
Overview:
The bullet file has a Bulllet class that creates in-game bullet objects. 

Constructions


## duck.py

## enemy.py

## hpbar.py

## level.py

## main.py

## mcquestion.py

 





