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
The following files are the essence of our game: the python files that create the user interface and experience. We attempted to implement our classes in a way that they can, when possible, be interchangably used, to simplify the usage of the classes. This is mainly seen with the same collision functions working on enemies and players for jumping and movement around blocks, and with all the level types being placed in the same level array, with all the same methods called on them in main. This makes implementation and updating easier, as any new type of level just has to follow the archetype of the others, with the same methods. 

## block.py
Overview: 
The block.py file allows for the creation of blocks in main. In game, blocks are immovable black rectangles that act as obstacles to the player. They also can act as platforms. They are solid objects that are opaque to all entities. 

Contruction: 
block.py has a Block contructor that allows for the creation of new Block objects. Each block object represents an individual block on an individual level. Blocks must have a set position on screen, as dictated by the parameters x and y. As rectangles, they must also have set width and heights, as dictated by the parameters w and h. These are the only variables stored in the block itself, and they are the only variables necessary for implementing the collision of blocks. 

Functions:
.display 
When called through a Block object, the .display function shows the block on the win parameter, a window on the user's device. The block is displayed simply using a black rectangle. 

.objectCollision
When called through a block object, the .object collision function checks if the block is in contact with another entity(player or enemy). This prevents entities from passing through blocks, allows them to stand/jump on blocks. Essentially, giving each level structure. Tuning the collision physics ended up taking the most time of most of the methods implemented in the project, as bugs can arise from tiny imperfections in the code. I think that in its current iteration, it is almost or entirely bug-free. Many of the decisions made in the block collision have to do with how to handle ambiguous positions, like the duck colliding into the top left of the block, and whether the duck should be moved to the left of the block, or on top of it. This method can take as an input either a duck object or an enemy object, which allows it to be used to calculate the physics of both classes, cutting down on the code necessary. The exact purposes of all the conditionals in this method are detailed in comments. 

Why?
Blocks allow the player to interact with the world--it makes each level unique and interesting!

## boss.py
Overview: The boss.py file allows for the creation of the final boss. In game, the boss is an entity displayed with a health bar and the MIT logo. It is the final enemy and the end of the game.

Construction:
The boss is constructed with the MIT beaver, fitted to the screen, with full health, at a set point on the screen. It also holds the booleans that tell if the level has been completed. It uses an Enemy object to have a hitbox for the boss, which is logical because it is intuitively a special type of enemy. This also allows the enemy's methods for certain functions to be reused, cutting down on similar or copy-pasted code. 

Functions:
.populateEnemies
Starts the level with the boss at full health. This is its own method, and not in the constructor, as if the player restarts the game and ends up at this level again, it should restart the level with a new boss at full hp, which it does. This is similar to the implementation of populateEnemies in other levels, which serve the purpose of resetting levels to their default states in case palyers replay them. 

.levelPyhsics
Just like all other levels, this functions defines the physics of the game such as object collisions and collisions with the window. It keeps the boss in screen, bouncing off the edges for a different type of enemy movement that hasn't been in the rest of the game. It also handles boss collision with the player, recording in its variables that the player was contacted, and from which direction, so the player can take damage and move accordingly in main. It also handles the timing of boss bullets shooting, and moves the enemy bullets that are shot at the player, as well as recording if they hit the player. If they do hit the player, the same happens as when a boss or enemy hits, recording the direction so the player can get hit away. 

.bossCollision
This method simply takes in the duck, and records if it is in contact with the boss, so that the player can take damage properly. It does this by checking if the rectangles that correspond to the positions of the player and boss are overlapping.

.bulletCollisions
When the user shoots the boss the boss takes damage to the health, the bullet dissapears, and the level ends if the boss dies. This function checks if the rectangles corresponding to the bullets overlap with the boss's, and updates health and the bullets array accordingly.

.display
Displays the boss on the screen with its healthbar. 

Why?
The boss level gives a satisfying conclusion to a job well done and a legendary performance by the player! It's also a fun surprise to end the story with.


## bullet.py
Overview:
The bullet file has a Bulllet class that creates in-game bullet objects shot by the player. 

Construction:
Bullet objects have screen positions and speeds as dictated by the two pairs of parameters. They are represented by images of the bullets. The rectangle they are counted as contacting is determined by the pixel size of their images. 

Functions:
.display
Displays the bullet object on screen. This is done by drawing the image stored in the bullet class onto the screen in the bullet's position

.move
Moves the bullet with respect to the direction it was shot and its speed.

.enemyCollision
Returns true if the bullet is in contact with another object. The object tested is passed in as a parameter, and because of the variable conventions, this could be a player, enemy, block, or other object for future updates. 

Why?
Bullets allow for another dimension of user interactivity--the gameplay evolved to having both dodging enemies and striking them down!


## duck.py
Overview:
Create duck objects - aka the player. 

Construction:
Duck objects need to have an inputted position to start at. All other properties such as the image used, speed, and HP bar are intrensic to all Duck objects. Updating most of the player's attributes, like acceleration, jump height, size, and starting hp, can be updated within the duck object.

Functions:

.display
Shows the duck on screen. This is done by drawing the duck image, facing either left or right depending on the last input from the player, as well as drawing the "gun" the duck holds. This is done by drawing a series of circles close to each other, to make a cylinder-like object. 
.move
moves the duck based on the user's arrowkey inputs. 

Why?
Every show needs a star: enter the CS50 Duck!

## enemy.py
Overview:
The enemies that show up on the screen during levels. Under the hood, these are hitboxes that can do damage to the player. They obstruct the user's path.

Construction:
Enemies are constructed on the screen at designated positions with the MIT beaver icon as their in-game representation. Similar to the player, the image is duplicated, with one reversed, so that the beaver also appears to face the player on screen. 

Functions:
.display
Show the enemy on the screen. This is done by correctly displaying the left-facing or right-facing beaver onto the screen.

.move
Move the enemy towards the player without user input. This, under the hood, functions very similarly to a player, with the beavers essentially pressing 'A' or 'D' to move horizontally towards the player, and jumping to reach the player when the player is above them. Through this, they attempt to chase the player down, providing a little more challenge, while not being impossible to evade. In order to compensate for their impossible computer reaction times, they accelerate slower and jump shorter than the player can.

.duckCollision
Return true when it hits the duck. This allows the duck to take damage. This is done by checking for overlap between the rectangle that represents the hitbox of the enemy with that of the duck that is passed into this method. 

Why?
The game needs a challenge--there's a reason a hero as strong as the CS50 duck is needed to save the day. 

## hpbar.py
Overview: Player, enemies, and the boss need a visual measure of their health! The HP bar is a common object that solves this problem. 

Construction:
Create a HP bar object that has the designated amount of health (parameter). It also sets the width of the hp bar depending on the amount of health the enemy or player has, so the player can visually see this value. 

.display
Display the HPbar above its corresponding entity. This is done by drawing a background rectangle, and drawing another rectangle in a color between green and red depending on how much of the total hp is remaining. 

Why?
Having limited health adds an additional challenge. It raises the stakes--the threat of death is real!


## level.py
Overiew: 
We decided to have different Level objects for each level because this allows for a very modular game--we can add/remove levels at any point without changing the others. This was particudlarly helpful in helping us hit our goals becasue we could have a MVP and add increasing complexity as time allows. 

Construction:
Create a level with the neceessary components: enemies, blocks, an exit portal, a spawn point, and possible text. It takes an array of block objects as an input, as the blocks don't change. However, for enemies, it simply takes an array of positions, and generates the objects itself. This is because of the fact that once enemies are removed from the array (when they die), they have to be regenerated from something, which is easiest with an array that serves as a prototype for how to create all the enemies in the level. For this reason, we call populateEnemies in the constructor, as well as each time the level is reset. 

Functions:
.populateEnemies
Enter the enemies into the game. This works off the array of positions passed into the constructor, and populates the array of enemies within this instance of level. 

.levelPhyiscs
Creates the phyics necessary for the game such as having window borders and accurate collisions. this mostly has to do with player, duck, and block collisions, to ensure that all movement is correct, and that enemies behave properly. It also checks if the player hits the exit to the level.

.bulletCollisions
This method takes in an array of bullets stored in the main file, which is all the bullet objects the player has fired. This method then checks each bullet against the enemies present in this level, properly decrementing enemy hp and deleting bullet objects that have collided with enemies. 

.display
This calls the display methods of all the blocks and enemies, as well as the exit portal. It also displays the text that can be passed into a level constructor on the top of the level.


## main.py

Overview: 
Essentially assemble all the helper files into a cohesive game. 

Elements: 
Has a levels array that stores all level objects that are included in the game. The game proceeds linearly through them. 
The main file also holds variables and arrays recording various other properties of the game, such as the player's Duck object itself, the timers for player damage and bullet shooting timer, and the array of bullets shot by the player.

Game loop
Contains a loop that runs until the game ends. This loop is kept at a constant 60 iterations per second by the pygame clock initiated at the start of the game. Within the loop, the methods of all the functions necessary to run the game are called, notably level physics, all of the collisions, and moving the player and bullets. It also handles upper-level logic such as moving between levels, updating player hp, and resetting the properties of levels when visiting them for the second time.

Drawing element
From the main loop, a few things are drawn manually, such as the background color, while many methods are called, such as that of the Duck, current level, and bullets, which each display themselves. Within these methods, some others are called as well, such as blocks, enemies, and portals within levels, and hp bars within the Duck and enemies. 

Bullet Behavior
Allow the user to shoot 1 bullet every 30 ticks. Remove bullets that exit the screen. 

## mcquestion.py
Overview:
Not a level object, but contains the same functions as a level. Therefore, it behaves like a level but with key differences. Such differences include having 4 portals, a set block setup, set spawn point, and no enemies. However, within the multiple choice question constructor, it also generates a level that has these elements within it, so that code for block and player handling is not reused. 

Construction: 
Similar to that of Level objects but takes parameters that allow for specific questions to be asked with a given correct answer. In the constructor, a level is created with a set arrangement of blocks to hand player-block collision for the question. Additionally, the order of the questions is randomized, with each being assigned to a location in our arrangement for multiple choice question levels. This way, when playing the game for a second time, the positions of correct answers aren't the same. Additionally, variables are assigned within this object so that the correct properties are available when main attempts to access them.

Functions:
.display
Displays the given question, which acts like its own level. In order to do this, the level with blocks stored within the question object is displayed, which in turn shows the text passed into it and its blocks. After that, the four answers display methods are called, which each draw a portal, as well as the text above the portal that describes the answer.

.levelPhysics
Dictates basic physics such as borders and if the player is contact with the right/wrong answer. This is done by calling the levelPhysics method of the level object stored within the question, as well as checking collisions between the player and the four portals. Finally, this returns true if the player is on their first try and in contact with the correct answer, which means they get a power-up to damage in main. The level is marked as complete if the player touches the correct portal, and incomplete if they touch one of the wrong portals.

.bulletCollisions
Does nothing, but is included so that mcquestion objects can have the same functions as levels. This adds a level of security; the developer can treat mcquestion objects just as levels--preventing errors.
 
.populateEnemies
Does nothing, but is included so that mcquestion objects can have the same functions as levels. This adds a level of security; the developer can treat mcquestion objects just as levels--preventing errors.

## Text-Screen.py

Overview: 
Creates a screen where text is dispalyed "Star Wars Style". Conveys story elements to the user.

Constructor:
Creates a blank level with text on the screen. Again, this object has many of the same properties as the other level types, which allows error prevention from accessing these attributes in main.

.populateEnemies
Prevents errors from calling a "level" without enemies

.levelPhysics
This method increments the "time" of the level, such that each successive frame displays the text farther up the screen and smaller. 

.bulletCollisions
Prevents errors from calling a "level" without bullets

.display
Displays text on the screen that moves star wars style. This is done by calculating the size text should be based on its order in teh array of lines stored in the object, as well as the time stored in the object. Based on this size, the spacing between the lines is determined, and the text is scaled and drawn onto the main screen accordingly. This method also records whether the level is complete by if the lowermost text object is off the screen.




