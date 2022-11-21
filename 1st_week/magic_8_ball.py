import random
r1 = "It's possible but only time will tell."
r2 = "The probability is good but not guaranteed."
r3 = "It's looking promising."
r4 = "You might rely on it."
r5 = "You can do anything if you put your mind to it."
r6 = "Yes, definitely."
r7 = "Whatever your heart tells you."
r8 = "It's too soon to tell."
answers = (r1, r2, r3, r4, r5, r6, r7, r8)
i = 1
def magic_8_ball(i):
  while True:
    user_input = input("Unsure about something? Ask the 8 ball: (press enter to exit)\n ")
    if user_input:
      answer = random.choice(answers)
      print(f"\n{answer}\n")
    else:
      print("Good Luck, hope it works out.")
      i = i - 1
      break
magic_8_ball(1)

# import random

# def magic_eight_ball():
#     print('Ask a question')
#     question = input()
#     answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 
#                'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
#                'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
#                'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
#                "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good',
#                'Very doubtful']
#     print(random.choice(answers))
    
# magic_eight_ball()