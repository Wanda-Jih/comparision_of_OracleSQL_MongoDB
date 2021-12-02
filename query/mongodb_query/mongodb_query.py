import pymongo
import sys
import time

def connectDB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["project2"]
    return mydb

def question1(mydb):
    
    mycol = mydb['country']    

    mydoc = mycol.aggregate(
    [
        {
          "$lookup":
            {
              "from": "borders",
               "localField": "code",
               "foreignField": "country1",
              "as": "borders1"
            }
        },
        {
          "$lookup":
            {
              "from": "borders",
              "localField": "code",
              "foreignField": "country2",
              "as": "borders2"
            }
        },
        { "$match":{"$and" : [{ "borders1": { "$ne": [] } }, {"borders2": { "$ne": [] } } ] } },
        { "$addFields": { "borderLength1": { "$sum": "$borders1.length"} } },
        { "$addFields": { "borderLength2": { "$sum": "$borders2.length"} } },
        { "$addFields": { "borderLengthTotal": { "$add": ["$borderLength1", "$borderLength2"]} } },

        
       { "$sort": { "borderLengthTotal": -1 } },
       { "$limit": 1 },
       { "$project": { "_id": 0, "name": 1 } }
     ])
    

    for x in mydoc:
        print(x)

def question2(mydb):
    
    mycol = mydb['city']    

    mydoc= mycol.aggregate(
        [
            { "$match": {"$and" : [{ "population": { "$ne": "" } }, {"population": { "$ne": 0 } } ] }},
            { "$group" : {"_id" : "$country",  "num_tutorial" : {"$max" : "$population"}}},     
            {
              "$lookup":
                {
                  "from": "city",
                  "localField": "num_tutorial",
                  "foreignField": "population",
                  "as": "cityP"
                }
            },
            { "$addFields": { "city_name": "$cityP.name" } },
            { "$addFields": { "population": "$num_tutorial" } },
            { "$project": { "_id": 1, "city_name" : 1} }
        ])


    for x in mydoc:
        print(x)

def question3(mydb):
    
    mycol = mydb['economy']    

    mydoc= mycol.find( 
        {"$and":
              [ 
                  {"$where" : "this.agriculture > this.service"},
                  {"$where" : "this.agriculture > this.industry"},
                  {"$where" : "this.agriculture > 0"} 
              ]}
        );


    for x in mydoc:
        result = []
        result.append(x["country"]) 
        result.append(x["gdp"]) 
        result.append(x["agriculture"]) 
        result.append(x["inflation"]) 
        print(result)
      
def question4(mydb):
    
    mycol = mydb['ethnicgroup']    

    mydoc= mycol.aggregate(
        [{
        "$group" : 
            {"_id" : "$country_code", 
             "num_ethnic_group" : {"$sum" : 1},
             "max_ethnic_group_percentage" : {"$max" : "$ethnic_group_percentage"}
             }
        },
        {
          "$lookup":
            {
              "from": "country",
              "localField": "_id",
              "foreignField": "code",
              "as": "countryName"
            }
        },
        { "$addFields": { "countryName": "$countryName.name" } },
        { "$sort"  : {"num_ethnic_group" : -1} },
        { "$project": { "_id": 0, "countryName": 1, "num_ethnic_group": 1, "max_ethnic_group_percentage": 1} }
    ])

    for x in mydoc:
        print(x)
      
def question5(mydb):
    
    mycol = mydb['country'] 
    mydoc= mycol.aggregate(
    [
        {
            "$lookup": {
              "from": 'ethnicgroup',
              "localField": 'code',
              "foreignField": 'country_code',
              "as": 'ethnicgroup',
            }
        },
        {
            "$lookup": {
              "from": 'language',
              "localField": 'code',
              "foreignField": 'country',
              "as": 'language',
            }
        },
        {
            "$match": {
              "$expr": { "$eq": [{ "$size": '$ethnicgroup' }, { "$size": '$language' }] },
            },
        },
       { "$group": { "_id": "null", "count": { "$sum": 1 } } },
       { "$project": { "_id": 0, "count": 1 } },
    ])
        
    for x in mydoc:
        print(x)
    
def question6(mydb):
    
    mycol = mydb['economy']  
    
    mydoc = mycol.aggregate(
        [ 
            {
                "$lookup": {
                  "from": 'country',
                  "localField": 'country',
                  "foreignField": 'code',
                  "as": 'country'
                  }
            },
            { "$match" : {"gdp" : {"$gte" : 0}} },
            { "$sort"  : {"gdp" : -1} },
            { "$limit" : 10 },
            { "$addFields": { "countryName": "$country.name" } },
            { "$project": { "_id": 0, "countryName" : 1, "gdp" : 1, "inflation": 1} }
        ]
    )

    for x in mydoc:
        print(x)       
 
def question7(mydb):
    mycol = mydb['religion']  
    
    mydoc = mycol.aggregate(
        [         
            { "$group" : 
                  {
                      "_id" :"$country",
                      "count" : {"$sum" : 1}
                  }
            },
            { "$sort"  : {"count" : -1} },
            { "$limit" : 10 },
            {
              "$lookup":
                {
                  "from": "country",
                   "localField": "_id",
                   "foreignField": "code",
                  "as": "countryName"
                }
            },  
            { "$unwind": '$countryName' },
            { "$project": { "_id": 0, "country_id" : "$countryName._id", "name" : "$countryName.name", "count" : 1, } },
            { "$group" : 
                  {
                      "_id" :"$count",
                      "country": { "$addToSet": { "id": "$country_id", "name": "$name" } },
                  }
            },
            { "$sort": { "_id": -1 } },
            { "$limit": 1 },
            { "$unwind": '$country' },
            {
              "$lookup":
                {
                  "from": "country",
                  "localField": "country.name",
                  "foreignField": "name",
                  "as": "countryName"
                }
            }, 
            {
              "$lookup":
                {
                  "from": "religion",
                  "localField": "countryName.code",
                  "foreignField": "country",
                  "as": "religion"
                }
            },      
            { "$unwind": '$religion' },
            { "$project": { "_id": 0, "country" : "$country.name", "religion" : "$religion.name" } },
       
        ]
    )


    for x in mydoc:
        print(x)

def question8(mydb):
    mycol = mydb['economy']  

    mydoc= mycol.aggregate(
    [
        { "$match": { "gdp": { "$ne": "" }  } },
        { "$sort"  : {"gdp" : -1} },
        { "$limit" : 100 },
        { "$project": { "_id": 0, "country" : 1} },
        {
          "$lookup":
            {
              "from": "ismember",
                "localField": "country",
                "foreignField": "country",
              "as": "ismember"
            }
        }, 
        { "$unwind" : '$ismember' },
        { "$match" : {"ismember.organization" : "C" } },
        { "$group" : { "_id": "", "count": { "$sum": 1 } } },
        { "$project" : { "_id": 0, "proportion": { "$divide": ["$count", 100] } } },
     ])


    for x in mydoc:
        print(x)

def question9(mydb):
    mycol = mydb['country'] 
    
    mydoc = mycol.aggregate(
    [ 
        { "$project" : { "_id": 0, "code": "$code", "encompasses_continent" : "$encompasses_continent",  "density" : { "$divide": ["$population", "$area"] } } },
        {
          "$lookup":
            {
              "from": "continent",
                "localField": "code",
                "foreignField": "country_code",
              "as": "continent"
            }
        }, 
        { "$unwind" : '$continent' },    
        { "$group" : { 
            "_id": "$continent.encompasses_continent" , 
            "max_continent" : { "$max" : "$density"} 
            } 
        },   
        {
          "$lookup":
            {
              "from": "continent",
              "localField": "_id",
              "foreignField": "encompasses_continent",
              "as": "continent"
            }
        },     
        { "$unwind" : '$continent' },  
        {
          "$lookup":
            {
              "from": "country",
              "localField": "continent.country_code",
              "foreignField": "code",
              "as": "country"
            }
        },    
        { "$unwind" : '$country' },  
        { "$addFields": { "density" : { "$divide": ["$country.population", "$country.area"] } } },           
        { "$project" : { 
            "_id": 0, 
            "continent": "$_id", 
            "country_name" : "$country.name", 
            # "max_continent" : { "$eq": [ "$max_continent",  ] }
            "max_continent" : "$max_continent", 
            "density" : "$density"} 
        },
        {
            "$match": {
              "$expr": { "$eq": ["$max_continent" , "$density"] },
            },
        },      
        { "$project" : { 
            "country_name": "$country_name", 
            "encompasses_continent" : "$continent", 
            "density" : "$max_continent"}
        },
         
   ])
    
    for x in mydoc:
        print(x)
       
def question10(mydb):
    
    mycol = mydb['country']

    mydoc = mycol.aggregate(
    [
        {
          "$lookup":
            {
              "from": "airport",
              "localField": "capital",
              "foreignField": "city",
              "as": "airport"
            }
        }, 
        { "$unwind" : '$airport'},    
        { "$group" : 
            {"_id" : "$name", 
              "city" : {"$sum" : 1},
            }
        },
        { "$match": { "$expr": { "$gt": ['$city' , 1] } } },
        { "$project" : { 
            "_id": 0, 
            "country" : "$_id", 
            "city#" : "$city"}
        },
    ])


    for x in mydoc:
        print(x)


           
if __name__ == '__main__':
    
 
    if len(sys.argv) != 2:
        q = 10
    else:
        q = sys.argv[1]
 

    start_time = time.time()
    mydb = connectDB()      

    if int(q) == 1:
        question1(mydb)
    elif int(q) == 2:
        question2(mydb)
    elif int(q) == 3:
        question3(mydb)
    elif int(q) == 4:
        question4(mydb)
    elif int(q) == 5:
        question5(mydb)
    elif int(q) == 6:
        question6(mydb)
    elif int(q) == 7:
        question7(mydb)
    elif int(q) == 8:
        question8(mydb)
    elif int(q) == 9:
        question9(mydb)
    elif int(q) == 10:
        question10(mydb)
    
    print("--- %s seconds ---" % (time.time() - start_time))