# 🧩 Sudoku Solver & CLI Game

A command-line Sudoku puzzle **generator, game, and solver** written in Python.
Developed as part of the **CS50P: Introduction to Programming with Python** course, this project demonstrates recursion, backtracking, user input handling, and clean CLI design.

---

## 📜 Overview

This is a fully interactive **command-line Sudoku game and solver**.
It can both **generate playable puzzles** with selectable difficulty and **solve puzzles entered by the user** using a recursive backtracking algorithm.

The program features:
- 🎮 **Play mode**: Generate a Sudoku puzzle and play interactively in your terminal.
- 🧮 **Solver mode**: Input your own Sudoku board and watch the algorithm solve it.
- ⚙️ **Recursive backtracking** algorithm for efficient solving.
- 🎨 **Colorized terminal UI** with ASCII art headers (via `colorama` and `pyfiglet`).
- ✅ **Unique puzzle generation** with solution validation.

This project emphasizes **algorithmic problem-solving**, **recursion**, and **clean code structure** while maintaining an engaging user experience.

---

## 🧰 Requirements

The solver runs on **Python 3.10+** and works with standard libraries.
However, your development environment may use additional packages from the `requirements.txt` file (auto-generated via `pip freeze` during CS50P coursework).

Install dependencies (only necessary if running within that environment):

To run the program in a python virtual environment follow these steps:
# 1. Create a virtual environment.
python -m venv venv

# 2. Activate it
# on macOS/Linux:
source venv/bin/activate
# on Windows:
venv\Scripts\activate

# 3. Install dependencies:
pip install -r requirements.txt

# 4. Run the program:
python sudoku.py

# to exit the venv:
deactivate
