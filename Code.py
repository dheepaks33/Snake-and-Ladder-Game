import tkinter as tk # Importing Tkinter to use as GUI module
import random # To generate dice values we use random func

# Initialize the Tkinter app
root = tk.Tk()
root.title("Snake and Ladder")

# Define the game variables
player1_position = 1
player2_position = 1
current_player = 1

# Create a canvas to draw the game board
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Define the snake and ladder positions
snake_and_ladders = { 16: 6, 47: 26, 49: 11,56: 53, 62: 19, 64: 19, 87: 52, 93: 8, 95: 75, 98: 82 }

# Create the game board
for i in range(10):
    for j in range(10):
        if (i * 10 + j + 1) in snake_and_ladders:
            cell_text = f"{i * 10 + j + 1} -> {snake_and_ladders[i * 10 + j + 1]}"
        else:
            cell_text = i * 10 + j + 1
        canvas.create_rectangle(j * 40, i * 40, (j + 1) * 40, (i + 1) * 40, fill="white")
        canvas.create_text((j + 0.5) * 40, (i + 0.5) * 40, text=cell_text)

# Function to roll the dice
def roll_dice():
    global current_player, player1_position, player2_position
    dice_result = random.randint(1, 6)
    if current_player == 1:
        player1_position += dice_result
        if player1_position in snake_and_ladders:
            player1_position = snake_and_ladders[player1_position]
    else:
        player2_position += dice_result
        if player2_position in snake_and_ladders:
            player2_position = snake_and_ladders[player2_position]

    current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)

    # Update the player positions on the board
    canvas.delete("players")
    for pos, player in [(player1_position, "Player 1"), (player2_position, "Player 2")]:
        row = (pos - 1) // 10
        col = (pos - 1) % 10
        x = (col + 0.5) * 40
        y = (row + 0.5) * 40
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="red", tags="players")
        canvas.create_text(x, y, text=player, tags="players")

    if player1_position >= 100:
        canvas.create_text(200, 200, text="Player 1 wins!", font=("Helvetica", 20))
        canvas.unbind("<Button-1>")
    elif player2_position >= 100:
        canvas.create_text(200, 200, text="Player 2 wins!", font=("Helvetica", 20))
        canvas.unbind("<Button-1>")

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

root.mainloop()
