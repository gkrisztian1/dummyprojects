import csv
path = "D:/Documents/GitHub/dummyprojects"

def read_file(filename):
    rows = []
    csvfile = open(path + filename, mode="r")
    file= csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for i in file:
        rows.append(i)
    return rows
    csvfile.close()

print(read_file("/data/42ae8.csv"))

