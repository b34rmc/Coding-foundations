import csv

data = []
with open('cars.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ';')
    skip = next(reader)
    header = skip[0], skip[4]
    for row in reader:
        car = row[0]
        horsepower = row[4]
        car_object = car, horsepower
        data.append(car_object)
data.sort()

with open('matts_cars.csv', 'w') as car_data:
    wrt = csv.writer(car_data)
    wrt.writerow(header)
    wrt.writerows(data)    