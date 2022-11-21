year = 1752
print("Enter a year after 1752:")
response = int(input(""))
if response % 4:
    print(f"{response} is a leap year!")
elif response % 400:
    print(f"{response} is a leap year!")
elif response % 100:
    print(f"{response} is not a leap year!")