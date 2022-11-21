mylist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
list = []
for i in range(1, 101):
    list.append(i)
    print(i)
my_list = ["a", "b", "c", "d", "b", "a", "e"]
print(my_list)
for letter in my_list:
    if letter in "aeiou":
        print(letter)
print("Evens:")
for i in list:
    if i % 2 == 0:
        print(i)

print("Odds:")        
for i in list:
    if i % 2 > 0:
        print(i)
        
list.reverse()
print(list)