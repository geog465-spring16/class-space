#! python3

print("Assignment 1: Eric Tang")

# Establish connection to my database
# Database name : testdatabase
# Database server: localhost (my computer)
# Database port: 5432 (default portnumber)
# Username : postgres
# Password : admin

from pg import DB

db = DB(dbname='testdatabase', host='localhost', port=5432, user='postgres', passwd='admin')

print("Connection to the database: OK")

print("Clear database...")


db.query("drop TABLE IF EXISTS location")
db.query("drop TABLE IF EXISTS cityfeatures")
db.query("drop TABLE IF EXISTS feature")
db.query("drop TABLE IF EXISTS city")


print("Now creating database objects :")



print("Table - Feature")

db.query(" CREATE TABLE feature ( "
         "   featureId smallint  NOT NULL,"
         "   featureName character varying(50)  NOT NULL,"
         "   CONSTRAINT Feature_pk PRIMARY KEY (featureId))"
         ) 


print("Table - City")
db.query("CREATE TABLE city ("
         "cityid smallint  NOT NULL,"
         "cityName character varying(50)  NULL,"
         "CONSTRAINT city_pk PRIMARY KEY (cityid))"
         ) 


print("Table - cityfeatures")
db.query("CREATE TABLE cityfeatures ("
         "featureId smallint NOT NULL,"
         "cityid smallint  NOT NULL,"
         "CONSTRAINT citifeatures_pk PRIMARY KEY (featureId,cityid))"
          ) 

print ("Table: Location")

db.query("CREATE TABLE Location ("
         "locationId smallint  NOT NULL,"
         "featureId smallint  NOT NULL,"
         "cityid smallint  NOT NULL,"
         "commonName character varying(50)  NOT NULL,"
         "address character varying(60)  NOT NULL,"
         "website character varying(250)  NOT NULL,"
         "LNG numeric(15,7)  NOT NULL,"
         "LAT numeric(15,7)  NOT NULL,"
         "CONSTRAINT Location_pk PRIMARY KEY (locationId))"
         )

print ("Relation: LocationCityFeatures");

db.query("ALTER TABLE Location ADD CONSTRAINT LocationCityFeatures " 
         "FOREIGN KEY (featureId,cityid)"
         "REFERENCES cityfeatures (featureId,cityid)")

print ("Relation: cityfeaturesFeature");

db.query("ALTER TABLE cityfeatures ADD CONSTRAINT cityfeaturesFeature "
         "FOREIGN KEY (featureId) "
         "REFERENCES Feature (featureId)"
         ) 

print ("Relation: cityfeaturescity ");

db.query("ALTER TABLE cityfeatures ADD CONSTRAINT cityfeaturescity "
         "FOREIGN KEY (cityid) "
         "REFERENCES city (cityid)"
         )

print ("Inserting data into the database")

print ("Table City - multiple rows at once")
cities = 'Seattle Spokane Tacoma Vancouver'.split()
data = list(enumerate(cities, start=1))
db.inserttable('city', data)


print ("Table Feature - multiple rows at once")
features = 'Library Park Museum Theatre'.split()
data = list(enumerate(features, start=1))
db.inserttable('feature', data)

print ("Table cityfeature - single row at once")


db.insert('cityfeatures',featureid=1,   cityid=1)
db.insert('cityfeatures',featureid=2,   cityid=1)
db.insert('cityfeatures',featureid=3,   cityid=1)
db.insert('cityfeatures',featureid=4,   cityid=1)

db.insert('cityfeatures',featureid=3,   cityid=2)
db.insert('cityfeatures',featureid=2,   cityid=3)
db.insert('cityfeatures',featureid=4,   cityid=4)


print ("Table location - single row at once")


db.insert('location', locationid =1,   featureid =1,    cityid=1 ,    commonname='Dorothy Stimson Bullitt Library',    address='100 University St',    website ='seattleartmuseum.org',    lng=47.6057,    lat=-122.3371 )
db.insert('location', locationid =2,   featureid =1,    cityid=1 ,    commonname='Region 10 Library',    address='1200 6th Ave #900',    website ='epa.gov',    lng=47.6090,    lat=-122.3320 )


db.insert('location', locationid =3, featureid =1,cityid=1,commonname='Virginia Mason Med Center Library'	,address='925 Seneca St'	, website ='masnomed.org'				,lng=47.6098,lat=-122.3285);
db.insert('location', locationid =4, featureid =2,cityid=1,commonname='Westlake Park'						,address='401 Pine St'		, website ='seattle.gov'				,lng=47.6109,lat=-122.3373);
db.insert('location', locationid =5, featureid =2,cityid=1,commonname='Jim Ellis Freeway Park'				,address='700 Seneca St'	, website ='seattle.gov'				,lng=47.6092,lat=-122.3312);
db.insert('location', locationid =6, featureid =3,cityid=1,commonname='Frye Art Museum'					,address='704 Terry Ave'	, website ='fryemuseum.org'				,lng=47.6069,lat=-122.3241);
db.insert('location', locationid =7, featureid =3,cityid=1,commonname='Seattle Pinball Museum'				,address='508 Maynard Ave S', website ='seattlepinballmuseum.com'	,lng=47.5976,lat=-122.3251);
db.insert('location', locationid =8, featureid =4,cityid=1,commonname='Paramount Theatre'					,address='911 Pine St'		, website ='stgpresents.org'			,lng=47.6132,lat=-122.3315);
db.insert('location', locationid =9, featureid =4,cityid=1,commonname='ACT Theatre'						,address='700 Union St'		, website ='acttheatre.org'				,lng=47.6112,lat=-122.3328);
db.insert('location', locationid =10,featureid =4,cityid=1,commonname='Annex Theatre'						,address='1100 E Pike St'	, website ='annextheatre.org'			,lng=47.6140,lat=-122.3180);
db.insert('location', locationid =11,featureid =3,cityid=2,commonname='Mobius Childrens Museum'			,address='River Park Square', website ='mobiusspokane.org'			,lng=47.6578,lat=-117.4292);
db.insert('location', locationid =12,featureid =2,cityid=3,commonname='Jefferson Park'						,address='801 N Mason Ave'	, website ='metroparkstacoma.org'		,lng=47.2543,lat=-122.5168);
db.insert('location', locationid =13,featureid =4,cityid=4,commonname='The Orpheum'						,address='601 Smithe St'	, website ='vancouver.ca'				,lng=49.2801,lat=-123.1209);

print ("Printout table contents")
print ("")

print ("Table :City")

print(db.query('select * from city'))

print ("")

print ("Table :Feature")

print(db.query('select * from feature'))

print ("")

print ("Table :cityfeatures ")

print(db.query('select * from cityfeatures '))


print ("")

print ("Table : Location")

print(db.query('select * from location'))



db.commit
