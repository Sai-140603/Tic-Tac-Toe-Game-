# Tic-Tac-Toe (Console-based Game)

This is a simple **console-based Tic-Tac-Toe game** written in Python. It allows two players to take turns placing X and O on a 3x3 board. The game checks for win conditions across rows, columns, and diagonals, and announces the winner or a draw after 9 turns.Includes input validation, turn switching, and win/draw detection.

## 🎮 How It Works

- The game board is a 3x3 grid displayed using list outputs.
- Players are prompted to select a row and a column (1–3 each).
- The input is validated, and if the cell is taken, the player is asked to try again.
- The game continues until a player wins or all 9 moves are used (draw).

## 🧠 Features

- Input validation for rows and columns.
- Prevention of overwriting occupied cells.
- Win detection across:
  - All rows
  - All columns
  - Both diagonals
- Draw detection if no player wins after 9 turns.
- Turn alternation between player X and O.

## 🚀 How to Run

python tic_tac_toe.py
