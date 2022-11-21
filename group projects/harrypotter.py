# class which_house():
#     gryffindor = 0
#     slytherin = 0
#     ravenclaw = 0
#     hufflepuff = 0
    
#     def gryffindor_add(self):
#         self.gryffindor += 1
#     def slytherin_add(self):
#         self.gryffindor += 1
#     def ravenclaw_add(self):
#         self.ravenclaw += 1
#     def hufflepuff_add(self):
#         self.hufflepuff += 1
#     def questions(self):
#         question1 = input(f"You are trying to escape a crumbling cliff when your unathletic friend twists his ankle. You choose to:\n A)Risk a painful death by carrying your friend to safety or\n B)Save yourself.\n")
#         if question1.upper() == 'A':
#             self.gryffindor_add()
#         else:
#             self.slytherin_add()
            
#         question2 = input(f"Your neighbor's dog is leaving yellow spots all over your lawn, despite all of your efforts to compromise with your neighbor. You choose to:\n A)Use a charm to make your grass green or\n B)Curse the dog.\n")
#         if question2.upper() == 'A':
#             self.gryffindor_add()
#         else:
#             self.slytherin_add()
            
#         question3 = input("A troll is charging at you. You have seconds to decide your next action before you're trampled. In your left hand you have a rock. In your right hand you have your wand. You:\n A)Throw the rock and run away. \n B)Cast a paralysis charm and then pull out your notebook to document your observations of the immobile troll.\n")
#         if question3.upper() == 'A':
#             self.hufflepuff_add()
#         else:
#             self.ravenclaw_add()
            
#         question4  = input("You've been asked by your crush to go to the Yule Ball. You: \n A)Go to the ball. \n B)Decide it's better to spend the free time studying rather than dancing all night.\n")
#         if question4.upper() == 'A':
#             self.hufflepuff_add()
#         else:
#             self.ravenclaw_add()
            
#         question5 = input(f"Do you plan your week ahead of time? \n A)Always plan or \n B)Never just go with the flow.\n")
#         if question5.upper() == 'A':
#             self.ravenclaw_add()
#         else:
#             self.hufflepuff_add()
            
#         question6 = (input(f"How reliable are you?\n A)You can count on me! \n B)Worry about yourself\n"))
#         if question6.upper() == 'A':
#             self.hufflepuff_add()
#         else:
#             self.ravenclaw_add()
            
#         question7 = input(f"You walk into a mall with your mom and 6ft shredded man just disrespected your mom, how would you react?\n A)either think, I wonder if he had a bad day or\n B)stand up for your mom and say, you cant disrespect my mom like that and get ready to fight him.\n")
#         if question7.upper() == 'A':
#             self.gryffindor_add()
#         else:
#             self.slytherin_add()
                  
# print('Which house do you belong to?')
# house = which_house()
# while True:
#     q = input('Do you want to find out which house you belong to? (y / n):\n')
#     if q == 'y':
#         house.questions()
#         house_dict = {'gryffindor': house.gryffindor, 'slytherin': house.slytherin, 'ravenclaw': house.ravenclaw, 'hufflepuff': house.hufflepuff}
#         t = max(house_dict.values())
#         for i in house_dict:
#             if t == house_dict[i]:
#                 print(f"\nYou are in the house of {i.upper()}!")
#                 break
#         break
#     elif q == 'n':
#         print('Okay then, be that way.')
#         break
#     else:
#         print('Wrong command')