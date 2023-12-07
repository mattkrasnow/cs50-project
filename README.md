# README Cs50-Project


Table of Contents

- [Our Video!](https://youtu.be/W3D0rbpKQ80)
- [Overiview](#overview)
- [How to Start](#how-to-start)
- [Controls](#controls)
- [Quitting](#quitting)

## Overview
Our project is a story-based game that follows the CS50 duck on an adventure. The general outline of the story is that MIT has hacked CS50, taking away all the psets we have made and all the code for next year's work as well. The duck debugger must step up and be the hero he was always meant to be, and save CS50 from this unfortunate outcome. In the game, the player controls the duck, going through levels that each correspond to a pset, and has to answer questions to reinforce CS50 knowledge. 

## How to Start
The game starts by running the python file main.py.

It will start by opening a new pygame window with the game visuals therein. 

You can close the game by simply pressing the x in the top of the screen. 

## Controls
The controls are also described in the game via text seen by the user. 

The keyboard controls for gameplay are as follows:

Trackpad/Mouse: Aims the player's bullets
Clicking or holding down the mouse: Player shoots a bullet in the direction of the mouse

ArrowKeys:
\[D\]: Accelerate the player to the right
\[A\]: Accelerate the player to the left
\[W\]: Move the player up (jump)


## Playing

Basic game fundamentals: 
- The goal of most levels is to reach the portal, not to kill all the enemies (exception of story slides and the boss level). For the text levels, the player doesn't have to do anything, and they end automatically
- Questions are answered by passing through the corresponding portal. Getting the question right on the first attempt will reward the player with an extra damage to their bullets for the rest of the game
- Answering a question wrong will send the player back 1 level. This will also mean they can no longer get the powerup to their bullets from that question.
- Blocks (black rectangles) are impassable by the player. They act like the ground, with the player and enemies being able to jump and collide with them
- When the player dies, the whole game is restarted. Their health is reset, as are all the other levels. Text levels won't play again. 

## Quitting
Depending on the operating system; the window can be closed like any other window. On mac, use CMD+Q or the red x. On Windows, use ALT+F4. Additionally, it can be closed by just pressing the 'x' at the top of the window. 



