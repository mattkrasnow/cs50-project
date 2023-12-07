# Design CS50-Project
This is our CS50 project! 

## Table of Contents

- [Premise](#premise)
- [Project Manual](#project-manual)
    - [block.py](#blockpy)
    - [boss.py](#bosspy)
    - [bullet.py](#bulletpy)
    - [duck.py](#duckpy)
    - [enemy.py](#enemypy)
    - [hpbar.py](#hpbarpy)
    - [level.py](#levelpy)
    - [main.py](#mainpy)
    - [mcquestion.py](#mcquestionpy)
    - [textscreen.py](#text-screenpy)




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

Why?
Blocks allow the player to interact with the world--it makes each level unique and interesting!

## boss.py
Overview: The boss.py file allows for the creation of the final boss. In game, the boss is an entity displayed with a health bar and the MIT logo. It is the final enemy and the end of the game.

Construction:
The boss is constructed with the MIT beaver, fitted to the screen, with full health, at a set point on the screen. It also holds the booleans that tell if the level has been completed. It uses an Enemy object to have a hitbox for the boss, which is logical because it is intuitively a special type of enemy. 

Functions:
.populateEnemies
Starts the level with the boss at full health.

.levelPyhsics
Just like all other levels, this functions defines the physics of the game such as object collisions, collisions with the window, collisions with blocks. It keeps the boss in screen, prevents that from moving through blocks and the player.

.bulletCollisions
When the user shoots the boss the boss takes damage to the leahbar, the bullet dissapears, and the level ends if the boss dies. 

.display
Displays the boss on the screen with its healthbar. Displays the blocks in the level as well. 

Why?
The boss level gives a satisfying conclusion to a job well done and a legendary performance by the player!


## bullet.py
Overview:
The bullet file has a Bulllet class that creates in-game bullet objects. 

Construction:
Bullet objects have screen positions and speeds as dictated by the two pairs of parameters. They are represented by images of the bullets.

Functions:
.display
Displays the bullet object on screen

.move
Moves the bullet with respect to the direction it was shot and its speed.

.enemyCollision
Returns true if the bullet is in contact with another object. 

Why?
Bullets allow for another dimension of user interactivity--the gameplay evolved to having both dodging enemies and striking them down!


## duck.py
Overview:
Create duck objects - aka the player. 

Construction:
Duck objects need to have an inputted position to start at. All otehr properties such as the image used, speed, and HP bar are intrensic to all Duck objects. 

Functions:

.display
Shows the duck on screen

.move
moves the duck based on the user's arrowkey inputs. 

Why?
Every show needs a star: enter the CS50 Duck!

## enemy.py
Overview:
The enemies that show up on the screen during levels. Under the hood, these are hitboxes that can do damage to the player. They obstruct the user's path.

Construction:
Enemies are constructed on the screen at designated positions with the MIT beaver icon as their in-game representation. 

Functions:
.display
Show the enemy on the screen

.move
Move the enemy towards the player without user input.

.duckCollision
Return true when it hits the duck. This allows the duck to take damage. 

Why?
The game needs a challenge--there's a reason a hero as strong as the CS50 duck is needed to save the day. 

## hpbar.py
Overview: Player, enemies, and the boss need a visual measure of their health! The HP bar is a common object that solves this problem. 

Construction:
Create a HP bar object that has the designated amount of health (parameter)

.display
Display the HPbar above its corresponding entity.

Why?
Having limited health adds an additional challenge. It raises the stakes--the threat of death is real!


## level.py
Overiew: 
We decided to have different Level objects for each level because this allows for a very modular game--we can add/remove levels at any point without changing the others. This was particudlarly helpful in helping us hit our goals becasue we could have a MVP and add increasing complexity as time allows. 

Construction:
Create a level with the neceessary components: enemies, blocks, an exit portal, a spawn point, and possible text. 

Functions:
.populateEnemies
Enter the enemies into the game 

.levelPhyiscs
Creates the phyics necessary for the game such as having window borders and accurate collisions. 

.bulletCollisions
Create the bullet properties such as hitting enemies

.display
Display blocks, enemies on the screen.


## main.py

Overview: 
Essentially assemble all the helper files into a cohesive game. 

Elements: 
Has a levels array that stores all level objects that are included in the game. The game proceeds linearly through them. 

Game loop
Contains a loop that runs until the game ends. Proceeds forward if the player wins, backwards if the player loses. 

Drawing elemtnt
Draw various entities in the game such as the duck, the screen background and color

Bullet Behavior
Allow the user to shoot 1 bullet every 15 ticks. Remove bullets that hit enemies or exit the screen. 

## mcquestion.py
Overview:
Not a level object, but contains the same functions as a level. Therefore, it behaves like a level but with key differences. Such differences include having 4 portals, a set block setup, set spawn point, and no enemies. 

Construction: 
Similar to that of Level objects but takes parameters that allow for specific questions to be asked with a given correct answer. 

Functions:
.display
Displays the given question, which acts like its own level. 

.levelPhysics
Dictates basic physics such as borders and if the player is contact with the right/wrong answer. 

.bulletCollisions
Does nothing, but is included so that mcquestion objects can have the same functions as levels. This adds a level of security; the developer can treat mcquestion objects just as levels--preventing errors.
 
.populateEnemies
Does nothing, but is included so that mcquestion objects can have the same functions as levels. This adds a level of security; the developer can treat mcquestion objects just as levels--preventing errors.

## Text-Screen.py

Overview: 
Creates a screen where text is dispalyed "Star Wars Style". Conveys story elements to the user.

Constructor:
Creates a blank level with text on the screen 

.populateEnemies
Prevents errors from calling a "level" without enemies

.levelPhysics
Makes the text move up the screen

.bulletCollisions
Prevents errors from calling a "level" without bullets

.display
Displays text on the screen that moves star wars style




