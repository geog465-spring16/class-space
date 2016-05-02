import csv

# Defining Column header names for each table

building_permit = ['ID', 'PermitNumber', 'PermitType', 'Status']
address = ['ID', 'Street', 'Longitude', 'Latitude', 'BuildingPermit_id']
value = ['ID', 'value', 'BuildingPermit_id']
applicant = ['ID', 'Name', 'BuildingPermit_id']
date = ['ID', 'ApplicationDate', 'IssueDate', 'ExpirationDate', 'BuildingPermit_id']

table_00 = open('/Users/alisonjkolberg/Code/303/table_00.csv', 'w')

my_dwriter = csv.DictWriter(table_00, fieldnames = building_permit)
my_dwriter.writeheader()



a = open('/Users/alisonjkolberg/Code/303/building_permits.csv')
dreader = csv.DictReader(a)
#loop_dreader = csv.DictReader(f)
buildingpermit_list = []

i = 1
#for row in loop_dreader:
for row in dreader:
    buildingpermit_list.append({'ID': i, 'PermitNumber': row['Application/Permit Number'],'PermitType': row['Permit Type'], 'Status': row['Status']})
    i += 1



my_dwriter.writerows(buildingpermit_list)
table_00.close()
a.close()


# doing the same exact steps as above - but for "Address Table"

table_01 = open('/Users/alisonjkolberg/Code/303/table_01.csv','w')
a = open('/Users/alisonjkolberg/Code/303/building_permits.csv')
dreader = csv.DictReader(a)
my_dwriter_2 = csv.DictWriter(table_01, fieldnames = address)
my_dwriter_2.writeheader()
#loop_dreader_2 = csv.DictReader(a)
address_list = []
i = 1
for row in dreader:
    address_list.append({'ID': i, 'Street': row['Address'], 'Longitude': row['Longitude'], 'Latitude': row['Latitude'], 'BuildingPermit_id': ''})
    i += 1
my_dwriter_2.writerows(address_list)

table_01.close()
a.close()

#same steps for the applicant table

table_02 = open('/Users/alisonjkolberg/Code/303/table_02.csv','w')
#needs to be before loop
a = open('/Users/alisonjkolberg/Code/303/building_permits.csv')
dreader = csv.DictReader(a)

my_dwriter_3 = csv.DictWriter(table_02, fieldnames = applicant)
my_dwriter_3.writeheader()
loop_dreader_3 = csv.DictReader(a)
applicant_list = []

i = 1
for row in loop_dreader_3:
    applicant_list.append({'ID': i, 'Name': row['Applicant Name'], 'BuildingPermit_id': ''})    
    i += 1
my_dwriter_3.writerows(applicant_list)

table_02.close()
a.close()

#same steps for the date table

table_03 = open('/Users/alisonjkolberg/Code/303/table_03.csv','w')

a = open('/Users/alisonjkolberg/Code/303/building_permits.csv')
dreader = csv.DictReader(a)

my_dwriter_4 = csv.DictWriter(table_03, fieldnames = date)
my_dwriter_4.writeheader()
loop_dreader_4 = csv.DictReader(a)
date_list = []

i = 1
for row in loop_dreader_4:
    date_list.append({'ID': i, 'ApplicationDate': row['Application Date'], 'IssueDate': row['Issue Date'], 'ExpirationDate': row['Expiration Date'], 'BuildingPermit_id': ''})
    i += 1
my_dwriter_4.writerows(date_list)

table_03.close()
a.close()


#same song and dance for Value Table

table_04 = open('/Users/alisonjkolberg/Code/303/table_04.csv','w')

a = open('/Users/alisonjkolberg/Code/303/building_permits.csv')
dreader = csv.DictReader(a)

my_dwriter_5 = csv.DictWriter(table_04, fieldnames = value)
my_dwriter_5.writeheader()
loop_dreader_5 = csv.DictReader(a)
value_list = []

i = 1
for row in loop_dreader_5:
    value_list.append({'ID': i, 'value': row['Value'], 'BuildingPermit_id': ''})
    i += 1
print(value_list)
print(value)
my_dwriter_4.writerows(value_list)

table_04.close()

a.close()





