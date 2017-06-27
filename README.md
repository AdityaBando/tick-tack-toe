# tick-tack-toe
This is a two player game.
Players alternate placing Xs and Os on the board until either (a) one player has three in a row, horizontally, vertically or diagonally; or (b) all nine squares are filled.
If a player is able to draw three Xs or three Os in a row, that player wins.

# APPROACH:

1. Initilize a variable __turn="O"__.
2. Display matrix of the game.
3. Get input from the first player.
4. Use another function (__game_brain()__) to see if vertical/horizontal/diagonals contains same string or not.
5. If not, give __turn__ to 2nd player by assingning __turn="X"__.
6. repeat same for second player.
