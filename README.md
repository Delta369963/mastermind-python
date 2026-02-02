# Mastermind Game (Python)

A modern, dark-themed implementation of the classic code-breaking game. Built with Python and styled with a sleek "Wordle-like" interface using CustomTkinter.

## 🚀 Features
* **Modern UI:** High-DPI, dark-mode interface with rounded corners.
* **Visual Feedback:** Color-coded clues (Green = Correct, Yellow = Wrong Position, Grey = Incorrect).
* **Keyboard Support:** Full typing interaction just like the web-based Wordle.
* **Responsive Design:** Clean layout that works on macOS and Windows.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **GUI Framework:** CustomTkinter (CTk)
* **Version Control:** Git & GitHub

## 💻 Installation & Usage
<details>
<summary><strong>Click here to view setup instructions</strong></summary>
<br>

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Delta369963/mastermind-python.git](https://github.com/Delta369963/mastermind-python.git)
    cd mastermind-python
    ```

2.  **Set up the Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    # OR if you haven't created the requirements file yet:
    # pip install customtkinter
    ```

4.  **Run the Game**
    ```bash
    python mastermind.py
    ```
</details>

## 🎮 How to Play
1.  **Objective:** Guess the hidden 4-digit code (numbers 0-9).
2.  **Type:** Enter 4 numbers on your keyboard and press **Enter**.
3.  **Clues:**
    * 🟢 **Green:** Number is correct and in the right spot.
    * 🟡 **Yellow:** Number is in the code, but in the wrong spot.
    * ⚫ **Grey:** Number is not in the code.
4.  **Win:** Guess the correct code within 6 tries!

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
