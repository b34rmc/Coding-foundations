from operator import truediv


def checkout_time(customers, n):
    time = [0] * n
    for c in customers:
        time[0] += c
        time.sort()
    return time[-1]
print(checkout_time([5,3,4], 1))
print(checkout_time([10,2,3,3], 2))
print(checkout_time([2,3,10], 2))
print(checkout_time([], 1))
print(checkout_time([1,2,3,4], 1))
print(checkout_time([2,2,3,3,4,4], 2))
print(checkout_time([1,2,3,4,5], 100))