import customtkinter as ctk
import random

# --- Configuration ---
THEME_COLOR = "#121213"       # Wordle Dark Background
BOX_DEFAULT = "#3a3a3c"       # Empty Box Border
CORRECT_POS = "#538d4e"       # Green
WRONG_POS   = "#b59f3b"       # Yellow
NOT_IN_CODE = "#3a3a3c"       # Grey (Box background)
TEXT_COLOR  = "#ffffff"       # White text

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class MastermindGame(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Mastermind")
        self.geometry("400x650")
        self.configure(fg_color=THEME_COLOR)
        self.resizable(False, False)

        # Game State
        self.secret_code = self.generate_code()
        self.current_row = 0
        self.guesses = [["" for _ in range(4)] for _ in range(6)] # 6 rows, 4 digits

        # UI Layout
        self.create_title()
        self.create_grid()
        self.create_input_area()
        
        # Bind keyboard
        self.bind("<Key>", self.handle_keypress)

    def generate_code(self):
        # Generates a 4-digit code (numbers 0-9)
        # Note: Mastermind usually allows duplicates.
        return [str(random.randint(0, 9)) for _ in range(4)]

    def create_title(self):
        title_label = ctk.CTkLabel(
            self, 
            text="MASTERMIND", 
            font=("Helvetica", 30, "bold"),
            text_color=TEXT_COLOR
        )
        title_label.pack(pady=20)

    def create_grid(self):
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(pady=10)

        self.cells = [] # Will hold the UI labels for the 6x4 grid

        for row in range(6):
            row_cells = []
            for col in range(4):
                cell = ctk.CTkLabel(
                    self.grid_frame,
                    text="",
                    width=60,
                    height=60,
                    font=("Helvetica", 32, "bold"),
                    fg_color="transparent",
                    text_color=TEXT_COLOR,
                    corner_radius=4
                )
                # Add a border using a frame container if strictly needed, 
                # but for simplicity in CustomTkinter, we style the fg_color later.
                cell.configure(fg_color=THEME_COLOR, width=60, height=60)
                
                # To simulate the border, we can check logic or just use background colors
                # Initial state: Empty with border color
                cell.configure(fg_color=BOX_DEFAULT) 
                
                cell.grid(row=row, column=col, padx=5, pady=5)
                row_cells.append(cell)
            self.cells.append(row_cells)

    def create_input_area(self):
        self.message_label = ctk.CTkLabel(
            self,
            text="Type 4 numbers & press Enter",
            font=("Arial", 14),
            text_color="#818384"
        )
        self.message_label.pack(pady=20)

    def handle_keypress(self, event):
        key = event.keysym
        
        # Game Over Check
        if self.current_row >= 6:
            return

        current_guess = self.guesses[self.current_row]
        filled_slots = len("".join(current_guess))

        # Handle Backspace
        if key == "BackSpace":
            if filled_slots > 0:
                # Find the last filled slot and clear it
                for i in range(3, -1, -1):
                    if current_guess[i] != "":
                        current_guess[i] = ""
                        self.cells[self.current_row][i].configure(text="")
                        break
            return

        # Handle Enter
        if key == "Return":
            if filled_slots == 4:
                self.check_guess(current_guess)
            else:
                self.flash_message("Not enough numbers!")
            return

        # Handle Numbers (0-9)
        if len(key) == 1 and key.isdigit():
            if filled_slots < 4:
                # Find first empty slot
                for i in range(4):
                    if current_guess[i] == "":
                        current_guess[i] = key
                        self.cells[self.current_row][i].configure(text=key)
                        break

    def check_guess(self, guess_list):
        # Algorithm to handle Green vs Yellow logic correctly
        secret_copy = self.secret_code[:]
        guess_copy = guess_list[:]
        result_colors = [NOT_IN_CODE] * 4

        # 1. Check for GREENS (Correct Position)
        for i in range(4):
            if guess_copy[i] == secret_copy[i]:
                result_colors[i] = CORRECT_POS
                secret_copy[i] = None # Mark as handled
                guess_copy[i] = None

        # 2. Check for YELLOWS (Wrong Position)
        for i in range(4):
            if guess_copy[i] is not None: # If not already green
                if guess_copy[i] in secret_copy:
                    result_colors[i] = WRONG_POS
                    # Remove one instance of this number from secret so we don't double count
                    secret_copy[secret_copy.index(guess_copy[i])] = None

        # Apply animations/colors to UI
        self.reveal_row(result_colors)

    def reveal_row(self, colors):
        # Update the UI colors
        for i in range(4):
            self.cells[self.current_row][i].configure(fg_color=colors[i])

        # Check Win/Loss
        if all(c == CORRECT_POS for c in colors):
            self.flash_message(f"YOU WON! Code: {''.join(self.secret_code)}")
            self.current_row = 7 # Stop game
        elif self.current_row == 5:
            self.flash_message(f"Game Over. Code: {''.join(self.secret_code)}")
            self.current_row += 1
        else:
            self.current_row += 1

    def flash_message(self, text):
        self.message_label.configure(text=text)

if __name__ == "__main__":
    app = MastermindGame()
    app.mainloop()