import random
import time

# ---------------- LUDO CONFIG ----------------
BOARD_SIZE = 57
PLAYERS = ["RED", "BLUE", "GREEN", "YELLOW"]

# Each player has 4 tokens
tokens = {
    "RED": [-1, -1, -1, -1],
    "BLUE": [-1, -1, -1, -1],
    "GREEN": [-1, -1, -1, -1],
    "YELLOW": [-1, -1, -1, -1]
}

current_player_index = 0


# ---------------- UTILITY FUNCTIONS ----------------
def roll_dice():
    return random.randint(1, 6)


def all_tokens_home(player):
    return all(pos == BOARD_SIZE for pos in tokens[player])


def print_tokens(player):
    print(f"{player} tokens:", tokens[player])


def can_move(player, token_index, dice):
    pos = tokens[player][token_index]

    if pos == -1 and dice == 6:
        return True
    if pos >= 0 and pos + dice <= BOARD_SIZE:
        return True
    return False


def move_token(player, token_index, dice):
    pos = tokens[player][token_index]

    if pos == -1 and dice == 6:
        tokens[player][token_index] = 0
    else:
        tokens[player][token_index] += dice

    if tokens[player][token_index] == BOARD_SIZE:
        print(f"🎉 {player} token {token_index} reached HOME!")


# ---------------- GAME LOOP ----------------
print("========== LUDO CLI GAME ==========")
print("Players:", ", ".join(PLAYERS))
print("-----------------------------------")

while True:
    player = PLAYERS[current_player_index]
    print(f"\n🔴 {player}'s TURN")

    print_tokens(player)
    input("Press ENTER to roll dice...")
    dice = roll_dice()
    print(f"Dice rolled: {dice}")

    movable = []
    for i in range(4):
        if can_move(player, i, dice):
            movable.append(i)

    if not movable:
        print("No valid moves. Turn skipped.")
    else:
        print("Movable tokens:", movable)
        choice = -1
        while choice not in movable:
            choice = int(input("Choose token index to move: "))

        move_token(player, choice, dice)

    if all_tokens_home(player):
        print(f"\n🏆 {player} WINS THE GAME!")
        break

    if dice != 6:
        current_player_index = (current_player_index + 1) % len(PLAYERS)

    time.sleep(1)

print("========== GAME OVER ==========")
