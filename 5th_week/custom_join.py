def list_join(it_obj, separator):
    new_str = ''
    for i in range(len(it_obj)):
        if i == len(it_obj) - 1:
            new_str += str(it_obj[i])
        else:
            new_str += str(it_obj[i]) + separator
    return new_str

lst = ['apple', 'banana', 15, 17.6, 'orange']
my_join = list_join(lst, ', ')
print(my_join)