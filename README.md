# 🧩 Maze Game

A maze navigation game built with Python's `turtle` graphics module. Play it manually with the arrow keys, or watch an automatic **Breadth-First Search (BFS)** algorithm solve the maze and animate the shortest path to the goal in real time.

## ✨ Features

- **Two play modes**, chosen at launch:
  - **Player mode (`P`)** — navigate the maze yourself using the arrow keys
  - **Auto-solve mode (`A`)** — the BFS algorithm computes and animates the shortest path from your position to the goal
- **Randomized spawn point** — the player starts at a random open (non-wall) location each run
- **Collision detection** against maze walls, so you can't walk through obstacles
- **Win detection** — reaching a goal zone changes the player's color and ends the game
- **In-maze auto-solve trigger** — even in Player mode, press `A` at any time to let BFS finish the maze for you

## 🎮 Controls

| Key | Action |
|---|---|
| ↑ ↓ ← → | Move the player (Player mode) |
| `A` | Trigger the BFS auto-solver |
| At launch: `P` / `A` | Choose Player mode or Auto mode |

## 🧠 How the Auto-Solver Works

The maze is stored as a list of wall segments (rectangular bounding boxes). The BFS solver treats each reachable coordinate as a graph node, expanding outward in fixed steps in all four directions, and returns the shortest path once a goal zone is reached. The path is then animated by moving the turtle step-by-step.

## 🛠️ Built With

- Python 3
- `turtle` (standard library — graphics/rendering)
- `random`, `time` (standard library)

## 🚀 Getting Started

**Requirements:** Python 3.x (turtle is included in the standard library on most installations).

```bash
git clone https://github.com/tahreem7926/Maze.git
cd Maze
python maze.py
```

When the game window opens, a prompt will ask you to choose a mode: enter `P` to play manually or `A` to watch the auto-solver.

## 📄 License

Educational project
