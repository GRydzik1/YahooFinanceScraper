import csv
listofstocks = []

def get_stock_list():
    with open("Stock_Names.csv", newline = '') as csvfile:
        rows = csv.reader(csvfile, delimiter = ',')
        for row in rows:
            listofstocks.append(row[0])
    del listofstocks[0]






