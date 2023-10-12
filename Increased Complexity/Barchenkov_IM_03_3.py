# Rock Paper Scissors
player1 = input("Player 1: ")
player2 = input("Player 2: ")

p1 = player1.lower()
p2 = player2.lower()

r = "rock"
p = "paper"
s = "scissors"


def game(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == r and p2 == s or p1 == p and p2 == r or p1 == s and p2 == p:
        return "Player 1 won!"
    else:
        return "Player 2 won!"


print(game(p1, p2))
