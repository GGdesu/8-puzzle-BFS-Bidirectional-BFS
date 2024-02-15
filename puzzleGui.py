import tkinter as tk


class PuzzleGUI:
    def __init__(self, master, puzzle_states):
        self.master = master
        self.tiles = []
        self.puzzle_states = puzzle_states
        self.current_state_index = 0
        self.create_board()
        self.update_puzzle()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                tile = tk.Label(self.master, text="", font=("Helvetica", 16), width=5, height=2, relief=tk.RIDGE, borderwidth=2)
                tile.grid(row=row, column=col, padx=5, pady=5)
                self.tiles.append(tile)

    def update_puzzle(self):
        current_state = self.puzzle_states[self.current_state_index]
        for tile, value in zip(self.tiles, current_state):
            tile.config(text=str(value))
        if(len(self.puzzle_states)-1 > self.current_state_index):
            self.current_state_index = (self.current_state_index + 1) % len(self.puzzle_states)
            self.master.after(500, self.update_puzzle)