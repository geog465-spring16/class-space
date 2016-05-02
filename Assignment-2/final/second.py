import csv

# read entire csv file into the list
getdata = csv.reader(open('test.csv', 'rt'), delimiter=',', quotechar='"')

alldata = []

for row in getdata :
       alldata.append(row)

# assume that csv file contains first row as header
header = alldata[0]    

#remove header from data
alldata.pop(0)


for colindex in range (0,len(header)):
    print ("Analyzing column "+header[colindex])
    if ("ID" not in header[colindex].upper()) :
        distinctcoldata = []
        for rowindex in range (0,len(alldata)):
             if (alldata[rowindex][colindex] not in distinctcoldata):
                  #print(alldata[rowindex][colindex])
                  distinctcoldata.append(alldata[rowindex][colindex])
        #print(distinctcoldata)
        writer = open(header[colindex]+"_dict.csv", "w")
        writer.write(header[colindex]+"ID,"+header[colindex] + "\n")
        id = 0
        for line in set(distinctcoldata):
        #create csv dictionary file
            id = id + 1 
            writer.write(str(id)+","+line + "\n")
        writer.close()
        print ("Created dictionary file "+header[colindex]+"_dict.csv"+ " "+str(len(distinctcoldata))+" unique rows out of "+str(len(alldata)))