# Table-Tennis
This project is a recreation of the classic Pong game, implemented using Python and the turtle graphics library. It features smooth paddle movement, ball collision detection, scoring, and a win condition for competitive play.

Features
Two-Player Gameplay

Player 1 uses the W and S keys to move the left paddle up and down.
Player 2 uses the Up and Down arrow keys for the right paddle.
Collision Detection

Ball bounces off the top and bottom walls.
Ball reflects when it hits the paddles.
Dynamic Difficulty

The speed of the ball increases slightly with each successful paddle hit.
Score Tracking

Left and right players' scores are displayed on the screen.
The game ends when one player reaches 10 points, declaring them the winner.
Wall Barriers

Red wall barriers prevent the ball from leaving the vertical play area.
Classes and Responsibilities
1. Paddle
Manages paddle creation and movement.

Attributes:
Position: Sets the paddle's initial position.
Methods:
up(): Moves the paddle up, limited to the screen boundary.
down(): Moves the paddle down, limited to the screen boundary.
2. Ball
Handles the ball's movement and behavior.

Attributes:
xmove, ymove: Determines the ball's speed and direction.
Methods:
move(): Updates the ball's position.
bouncewall(): Reflects the ball when it collides with the top or bottom walls.
bouncepaddle(): Reflects the ball when it hits a paddle.
3. Scoreboard
Manages and displays scores for both players.

Attributes:
l_score, r_score: Track left and right players' scores.
Methods:
update_scoreboard(): Updates the displayed scores.
l_point(): Adds a point to the left player and updates the scoreboard.
r_point(): Adds a point to the right player and updates the scoreboard.
result_l(): Declares the left player as the winner.
result_r(): Declares the right player as the winner.
Controls
Player	Action	Key
Left Paddle	Move Up	W
Left Paddle	Move Down	S
Right Paddle	Move Up	Up Arrow
Right Paddle	Move Down	Down Arrow
How to Run
Install Python
Ensure Python 3.x is installed on your system.

Download the Files

main.py: Contains the game logic.
paddle.py: Defines the Paddle class.
ball.py: Defines the Ball class.
scoreboard.py: Defines the Scoreboard class.
Run the Game
Open a terminal or command prompt in the project directory and execute:

bash
Copy code
python main.py
Play
Enjoy the game and compete with a friend to reach 10 points first!

Game Rules
The ball starts moving automatically.
The ball reflects off paddles and walls.
If the ball passes the right paddle, Player 1 scores.
If the ball passes the left paddle, Player 2 scores.
The game ends when a player reaches 10 points, and the winner is announced.
