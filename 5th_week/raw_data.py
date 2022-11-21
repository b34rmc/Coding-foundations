with open('raw_data.txt', 'r') as file:
    readfile = file.read()
    readfile = readfile.split('|')
    with open('new_data.txt', 'w') as new_file:
        new_file.write(','.join(readfile))