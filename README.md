# Ping Pong Game (Python Turtle)

## Overview

This is a simple two-player Ping Pong (Pong) game built using Python’s `turtle` module. The project demonstrates basic game development concepts such as animation, collision detection, keyboard input handling, and score tracking.

It is designed to be easy to understand and is suitable for beginners learning how interactive graphical programs work in Python.

---

## Features

- Two-player gameplay on the same keyboard  
- Continuous ball movement  
- Paddle controls using keyboard  
- Collision detection (walls and paddles)  
- Real-time score display  
- Simple graphics using turtle  
- Optional sound on ball bounce  

---

## Technologies Used

- Python 3.x  
- `turtle` (for graphics)  
- `os` (for sound execution)

---

## Project Structure
project-folder/
│
├── main.py # Main game file
├── bounce.wav # Optional sound file
└── README.md # Documentation

---

## Requirements

Make sure you have:

- Python 3 installed  
- No external libraries required (everything is built-in)

Check Python version:python --version


---

## How to Run

1. Download or clone the project:

git clone https://github.com/incompetant-jellyfish/PingPong
cd 


2. (Optional) Add sound file:
- Place `bounce.wav` in the same directory as your Python file  
- Note: Sound currently works only on macOS (`afplay`)  

3. Run the program:

python game.py


---

## Controls

| Player            | Move Up | Move Down |
|------------------|--------|----------|
| Player 1 (Left)  | W      | X        |
| Player 2 (Right) | O      | N        |

---

## How the Game Works

### Screen Setup

- A window is created with a black background  
- Screen size is fixed (900x700)  
- Manual screen updates are used for smoother animation  

### Paddle Movement

- Paddles move vertically using key presses  
- Each key press shifts the paddle by a fixed amount  

### Ball Movement

- The ball moves continuously using velocity values:
  - `dx` → horizontal movement  
  - `dy` → vertical movement  

### Collision Handling

- Top/Bottom walls:
  - Ball bounces by reversing vertical direction  

- Paddles:
  - Ball bounces by reversing horizontal direction  

### Scoring

- If the ball passes the right side:
  - Player 1 scores  

- If the ball passes the left side:
  - Player 2 scores  

- After scoring:
  - Ball resets to center  
  - Direction reverses  
  - Score updates on screen  

### Game Loop

- The game runs inside an infinite loop:

while True:
wn.update()


- This continuously updates movement and collisions  

---

## Limitations

- No pause or exit button (close window manually)  
- Paddles can move outside the screen  
- Sound only works on macOS by default  
- No AI or single-player mode  

---

## Possible Improvements

- Add paddle boundary limits  
- Add AI opponent  
- Increase ball speed over time  
- Improve physics (angle-based bounce)  
- Add pause and restart options  
- Make sound work on all platforms  
- Add start menu or game over screen  

---

## Learning Outcomes

This project helps in understanding:

- Basic game loops  
- Animation using turtle  
- Keyboard event handling  
- Collision detection  
- Structuring simple games  

---

## Author

Beginner-level Python Turtle project for learning and practice.
