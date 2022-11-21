import csv
lst = []
with open('countydata.csv', 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        lst.append(row)


print(f"{header[0]:^20} {header[1]:>10} {header[10]:>9} {'Growth':>9} {'Rate%':>9}")
print(f'-'* 20, '', '-'*8, '', '-'*8, '', '-'*8, '', '-'*8)
for item in lst:
    growth = int(item[10]) - int(item[1])
    rate = growth/int(item[1])*100
    print(f'{item[0]:<20} {item[1]:>9} {item[10]:>9} {growth:>9} {rate:>8.2f}%')