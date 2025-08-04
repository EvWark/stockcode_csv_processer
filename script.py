import csv
class Samples:
    def __init__(stockcode="NULL", pstockcode="NULL", sampletype="NULL", department="NULL", location="NULL"):
        self.stockcode = stockcode
        self.pstockcode = pstockcode
        self.sampletype = sampletype
        self.department = department
        self.location = location
    
    def __str__():
        return "In department: " + self.department + " at " + self.location + ". The Parent: " + self.pstockcode + " and the child: " + self.stockcode

discprodarr = []
file = open('discontinued_products.csv', newline='\r\n')
reader = csv.reader(file, delimiter=',')
for column in reader:
    discprodarr.append(column[0])

samplesarr = []
file = open('samples.csv', newline='\r\n')
reader = csv.reader(file, delimiter=',')
for column in reader:
    samplesarr.append(Samples(column[0], column[1], column[2], column[3], column[4]))

discsamplesarr = []
for x in discprodarr:
    for y in samplesarr:
        if x == y.pstockcode:
            discsamplesarr.append(y)
        elif x == y.stockcode:
            discsamplesarr.append(y)

with open("output.txt", 'w') as f:
    for x in discsamplesarr:
        f.write(x + "\n")

