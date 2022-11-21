def tree(n):
    for i in range(n):
        for j in range(n-i):
            print(' ', end=' ')
        for k in range(2*i+1):
            print('*', end=' ')
        print()


def trunk(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')

n = int(input('Enter height of tree: '))
tree(n)
trunk(n)