lst = []      
for i in range(1, 28):
    lst.append(i)
def slicefunction(iter_obj, start=1, stop=None, step=1):
    new_lst = []
    if stop < 0:
        stop = len(lst)-abs(stop)
    elif stop == None:
        stop = len(lst)
    for i in range(start, stop - 1, step):
        new_lst.append(iter_obj[i])
    return new_lst

print(slicefunction(lst,3,-1,2))