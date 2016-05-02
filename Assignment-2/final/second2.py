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
        distinctcolid = []
        j=0
        for rowindex in range (0,len(alldata)):
             if (alldata[rowindex][colindex] not in distinctcoldata):
                  # print(alldata[rowindex][colindex])
                  distinctcoldata.append(alldata[rowindex][colindex])
                  j=j+1
                  distinctcolid.append(j)

        # replace value with id
        
        for rowindex in range (0,len(alldata)):
            alldata[rowindex][colindex]=distinctcolid[distinctcoldata.index(alldata[rowindex][colindex])]
        
        #print(distinctcoldata)
        writer = open(header[colindex]+"_dict.csv", "w")
        writer.write(header[colindex]+"ID,"+header[colindex] + "\n")
        header[colindex]=header[colindex]+"ID"
        for x in range (0,j):
        #create csv dictionary file
            writer.write(str(distinctcolid[x])+","+distinctcoldata[x] + "\n")
        writer.close()
        print ("Created dictionary file "+header[colindex]+"_dict.csv"+ " "+str(len(distinctcoldata))+" unique rows out of "+str(len(alldata)))
        #replace data
        
 
newfile = csv.writer(open('testnew.csv', 'wt'), delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

newfile.writerow(header)
newfile.writerows(alldata)


