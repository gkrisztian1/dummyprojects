import csv

def read_file(path):
    rows = []
    csvfile = open(path, mode="r")
    file= csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for i in file:
        rows.append(i)
    return rows

print(read_file("/data/42ae8.csv"))

