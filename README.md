# Snake Game
This challenge is to build your own version of the classic game snake.

Many of us think of snake as one of the first games that was available on a mobile phone (it appeared on the Nokia 6110 in 1997). But snake goes back much further than that. It’s heritage dates back to 1976, with the first version of what was then called Worm written in 1978.

These days there are thousands of versions and it’s available for just about any device you care to try.

The Challenge - Building Snake
Snake is a simple game. The player controls a snake which move around the playing grid at a fixed speed. The goal is to eat food that appears at random locations on the grid.

For each item of food eaten the snake becomes longer and the player scores points. The game ends when the snake hits the edge of the game grid or it’s own body.

## Step Zero
In this step, pick the programming language and development environment you’re going to use. Consider trying something different - this would be a great project to try a frontend stack if you’re a backend developer and vice versa.

If you’re from a data engineering or site-reliability engineering background you could leverage your knowledge of Python with PyGame or Go with Ebitenegine. Rustaceans can check out are we game yet for useful crates.

Snake is relatively simple and as such, it’s a great platform for learning a new technology, or programming language.

## Step 1
In this step your goal is to draw the game grid and score display. That’s going to loop quite simple

Don’t forget to consider the size of the grid in both pixels and cells within the grid. For example the game screen might be 20 cells by 20 cells and each cell be 20 pixels by 20 pixels.

## Step 2
In this step your goal is to draw the snake and have it move around the grid. You should decide where the snake will start for your version of the game. It could be in a corner, the centre or in a random cell. Play around and see what you think gives the best gameplay.

To do this you’ll have to create a game look, in which you detect user input, update the game state and then render the state to the display. Every cell in the snakes body should ‘move’ to the board cell of the preceding body cell every turn. The simple way to do this is to remove the tail cell and add a new head cell.

Give the head of the snake a different colour so the user can recognise it. The snake’s body should be a number of cells long when the game starts. Try four initially but feel free to experiment.

## Step 3
In this step your goal is to detect when the snake collides with the wall. At that point end the game and show the score. Offer the user the chance to play a new game.

If they decided to start a new game reset the game state and begin a new game.

## Step 4
In this step your goal is to insert food at a random location on the game world. Once inserted the food should be rendered in the world and you will need to detect when it is eaten (a collision occurs between the head of the snake and the food) and then lengthen the snake and increase the score. On top of that you will remove the food from the screen and spawn a new item of food in a new random location.

## Step 5
In this step your goal is to detect when the snake collides with itself. When it does so, end the game.