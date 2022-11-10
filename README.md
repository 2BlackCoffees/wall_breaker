# Candy Cat

To run this game please make sure you have python3 and pip3 installed.

Then:

* `python3 -m pip install -U pygame --user`
* Clone this repository.
* The program can be started as follows: `python3 candy_cat`
* Following are the tasks to be done, please make sure each and every task is done following software best practices:

    1. Assuming you take over this project without any addition documentation and all people from the original team left the company, how would you go forward to:
       1. Analyze the program and have a clear understanding of how it works?
       1. Complete the next tasks with long term maintenance in mind?

    1. We need to define a timer. A timer is related to one game, once the timer elapsed the player lost (as if he had lost all his balls).
    1. Create a new type of brick: when this brick is bumped by a ball, then the user gets an additional ball (the number of balls is incresed by 1)
    1. Create again a new type of brick, this time when a ball bumps against it, a new ball should be given to the user that is able to move independantly of the first ball. Each time the new brick is bumped a new ball is created. The new ball should be placed on the player's racket.
    1. There are several bugs that were left on purpose:
        * Bug 1: The ball does not start at the right position when a game is won and the next one starts.
        * Bug 2: When a game is lost we hear 2 sounds hoevering each other, only the sound rekated to fact that the game is lost should be kept.
        * Bug 3: Left and right arrow should be controlling the racket. They however do not work.
        * Bug 4: The ball sometimes bumps against an horizontal or vertical wall but goes in its opposite direction (as if it was a corner instead of horizontal or vertical wall). 
        * Bug 5: If there is just the sapce for the ball (between 2 walls) then the ball should move along horizontally or vertically. Currently this is not happening and this must be fixed.
        * Bug 6: When the ball touches the racket and the racket was moving in one direction or the other, the angle of the direction of the ball should be updated.
    1. Improvements:
        * Destroyable bricks have all a specific count of bumps before they get destroyed. The remaining number of bumbs should be displayed on the top right of each detroyable brick within a circle surrounding the number.
        * Each tme a brick is destroyed an anmiation should be played (each brick type should have its specific animation).
        * The racket should be able to shoot rockets and destroy the skull bricks. Rockets should destroy unbreakable walls but when a dollar brick is touched then many points should be lost.
        * A multi player game could be analyzed.

https://github.com/2BlackCoffees/candy_cat/blob/main/CandyCat.mp4
