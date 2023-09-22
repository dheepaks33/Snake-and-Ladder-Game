import tkinter as tk # act as a GUI interface
import random #to get random dice values

# Create the main window
root = tk.Tk()
root.title("Snake and Ladder Game")

# Create a canvas to draw the game board
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Define the dimensions of the game board
rows = 10
columns = 10
cell_size = 40

# Create a list to store the player's position
player_position = [0]

# Create a list of snakes and ladders positions
snakes_and_ladders = {2: 38, 7: 14, 16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 13, 87: 37, 93: 69, 95: 75, 98: 78 }

# Function to roll the dice and update the player's position
def roll_dice():
    roll = random.randint(1, 6)
    player_position[0] += roll

    # Check for snakes and ladders
    if player_position[0] in snakes_and_ladders:
        player_position[0] = snakes_and_ladders[player_position[0]]

    # Update the player's position on the canvas
    update_player_position()

# Function to update the player's position on the canvas
def update_player_position():
    canvas.delete("player")
    row, col = position_to_row_col(player_position[0])
    x = col * cell_size + cell_size // 2
    y = (9 - row) * cell_size + cell_size // 2
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="blue", tags="player")

# Function to convert position to row and column
def position_to_row_col(position):
    row = position // columns
    col = position % columns
    if row % 2 == 1:
        col = columns - 1 - col
    return row, col

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

# Create the game board
for row in range(rows):
    for col in range(columns):
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray")

# Create snakes and ladders on the board
for start, end in snakes_and_ladders.items():
    row1, col1 = position_to_row_col(start)
    row2, col2 = position_to_row_col(end)
    x1 = col1 * cell_size + cell_size // 2
    y1 = (9 - row1) * cell_size + cell_size // 2
    x2 = col2 * cell_size + cell_size // 2
    y2 = (9 - row2) * cell_size + cell_size // 2
    canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

# Initialize the player's position
update_player_position()

root.mainloop()
