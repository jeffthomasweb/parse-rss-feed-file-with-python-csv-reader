import csv

#The RSS feed was saved in a file. Open the file.
with open("nprxml.xml") as xmlfile: 
    #XML is used in RSS feeds. Use ">" as the delimiter.
    #This will create a list were the feed is separated 
    #by the ">" character.
    readerparse = csv.reader(xmlfile, delimiter=">")
    for x in readerparse:
        #x is another list. Access the elements in list x. 
        for y in x:
            #Feed story tiles and descriptions are saved in XML
            #blocks <title> story title </title> and 
            #<description> story description </description>.
            #Find the substrings that contains the last block
            #such as </title> and subtract the </title> tag.
            #Do the same for </description>
            if y.find("/title") > 0:
                print(y[:-7])
            if y.find("/description") > 0:
                print(y[:-13],"\n")
