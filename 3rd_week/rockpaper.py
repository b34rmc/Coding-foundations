# import random

# player = ['Rock', 'Paper', 'scissors']
# computer = random(player[0, 2])

# player = False

# while player == False:
#     ui = input('Rock', 'Paper', 'Scissors').upper()
#     if ui == computer:
#         print('Tie!')
#     elif player == 'Rock':
#         if computer =='Paper':
#             print('Loser!', computer, 'covers', ui)
#         else:
#             print('You win', ui, 'smashes', computer)
#     elif ui == 'Paper':
#         if computer == 'Scissors':
#             print('Loser!')
#         else:
#             print('You win', ui, 'cuts', computer)
#     elif ui == 'Scissors':
#         if computer == 'Rock':
#             print('Loser!', computer, 'smashes', ui)
#         else:
#             print('You win', ui, 'cuter', computer)
#     else:
#         print('please enter Rock, Paper, or scissors')

# import random

# options = ["rock", "paper", "scissors"]

# player_wins = 0
# computer_wins = 0

# while player_wins < 2 and computer_wins < 2:
#     player = input("Choose rock, paper, or scissors: ")
#     computer = random.choice(options)

#     if player == computer:
#         print("Draw!")
#     elif player == "rock":
#         if computer == "paper":
#             print("Computer wins!")
#             computer_wins += 1
#         else:
#             print("Player wins!")
#             player_wins += 1
#     elif player == "paper":
#         if computer == "scissors":
#             print("Computer wins!")
#             computer_wins += 1
#         else:
#             print("Player wins!")
#             player_wins += 1
#     elif player == "scissors":
#         if computer == "rock":
#             print("Computer wins!")
#             computer_wins += 1
#         else:
#             print("Player wins!")
#             player_wins += 1
#     else:
#        print('enter Rock, Paper or Scissors')
       
width = int(input("What is the width of the bat?"))

height = width // 2

for i in range(height):
    print(" " * (height - i) + "\\" + " " * (width - 2) + "/")
print(" " * (height) + "-" * (width))
for i in range(height):
    print(" " * (i) + "/" + " " * (width - 2) + "\\")