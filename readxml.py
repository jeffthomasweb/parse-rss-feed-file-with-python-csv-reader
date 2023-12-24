import csv

with open("nprxml.xml") as xmlfile: 
    readerparse = csv.reader(xmlfile, delimiter=">")
    for x in readerparse:
        for y in x:
            if y.find("/title") > 0:
                print(y[:-7])
            if y.find("/description") > 0:
                print(y[:-13],"\n")
