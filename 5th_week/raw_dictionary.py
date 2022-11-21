with open('raw_dictionary.txt', 'r') as f:
    dict = {}
    for line in f:
        new_line = line.strip()
        words = new_line.split(' ')
        dict[words[0]] = words[1]
    print(dict)