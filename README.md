# 🎲 Ludo CLI Game (Python)

This project is a **console-based Ludo game** implemented in Python.  
The game simulates a simplified version of Ludo where multiple players take turns rolling a dice and moving their tokens until one player gets all tokens home.

The project is designed as a **single-file CLI application**, making it easy to understand, run, and extend.

---

## 🚀 Features

- 4 Players: RED, BLUE, GREEN, YELLOW
- 4 tokens per player
- Dice rolling (1–6)
- Token entry only on rolling 6
- Turn-based gameplay
- Extra turn on rolling 6
- Win detection
- Simple and readable logic

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Interface:** Command Line (CLI)  
- **Libraries Used:**  
  - `random`
  - `time`

(No external dependencies)

---

## 🎮 How to Play

1. Each player has 4 tokens initially at home (`-1`)
2. A token enters the board only when dice = 6
3. Players choose which token to move
4. First player to move all 4 tokens to position 57 wins

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ludo-cli-python.git
cd ludo-cli-python
