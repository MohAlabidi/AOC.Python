import csv

x= open('intlmigr.csv')
y= csv.reader(x)

for row in y:
    country = row[6]
    if country == 'Australia':
        print(row)

x.close()

