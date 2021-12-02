import pymongo
from pymongo.errors import CollectionInvalid
from collections import OrderedDict

def connectDB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["project2"]
    return mydb

def collection_schema(col):
    collection_schema = {}
    if col == 'country':
        collection_schema = {
            'name' : {
                'type' : 'string'
                },
            'code' : {
                'type' : 'string',
                'required': True
                },
            'capital' : {
                'type' : 'string'
                },
            'area' : {
                'type' : 'double'
                },
            'population' : {
                'type' : 'int'
                }
            } 
    elif col == 'country_other_localname':
        collection_schema = {
            'country' : {
                'type' : 'string',
                'required': True
                },
            'localname' : {
                'type' : 'string',
                'required': True
                },
            'othername' : {
                'type' : 'string'
                }
            } 
    elif col == 'countrypopulations':
        collection_schema = {
            'country' : {
                'type' : 'string',
                'required': True
                },
            'population' : {
                'type' : 'int',
                'required': True
                },
            'year' : {
                'type' : 'int',
                'required': True
                }
            }   
    elif col == 'economy':
        collection_schema = {
            'country' : {
                'type' : 'string',
                'required': True
                },
            'gdp' : {
                'type' : [ "double", "null", "undefined", "string" ]
                },
            'agriculture' : {
                'type' : [ "double", "null", "string" ],
                "minimum":  0.0,
                "maximum" : 100.0
                },
            'service' : {
                'type' : [ "double", "null", "string" ],
                "minimum":  0.0,
                "maximum" : 100.0
                },
            'industry' : {
                'type' : [ "double", "null", "string" ],
                "minimum":  0.0,
                "maximum" : 100.0
                },
            'inflation' : {
                'type' : [ "double", "null", "string" ]
                },
            'unemployment' : {
                'type' : [ "double", "null",  "string" ],
                "minimum":  0.0,
                "maximum" : 100.0
                }
            }          
    elif col == 'ethnicgroup':
        collection_schema = {
            'country_code' : {
                'type' : 'string',
                'required': True
                },
            'ethnic_group_name' : {
                'type' : 'string',
                'required': True
                },
            'ethnic_group_percentage' : {
                'type' :  [ "int", "double", "null", "string" ],
                "minimum":  0.0,
                "maximum" : 100.0
                }
            } 
    elif col == 'language':
        collection_schema = {
            'country' : {
                'type' : 'string',
                'required': True
                },
            'language' : {
                'type' : 'string',
                'required': True
                },
            'percentage' : {
                'type' :  [ "int", "double", "null", "string" ],
                "minimum":  0.0,
                "maximum" : 100.0
                }
            } 
    elif col == 'politics':
        collection_schema = {
            'country' : {
                'type' : 'string',
                'required': True
                },
            'independence' : {
                'type' : [ "date", "string" ]
                },
            'wasdependent' : {
                'type' :  [ "null", "string" ]
                },
            'dependent' : {
                'type' :  [ "null", "string" ]
                },
            'government' : {
                'type' :  [ "null", "string" ]
                }
            } 
    elif col == 'population': 
        collection_schema = {
            'country_code' : {
                'type' : 'string',
                'required': True
                },
            'population_growth' : {
                'type' : [ "double", "string" ,"int"]
                },
            'infant_mortality' : {
                'type' :  [ "double", "string","int" ]
                }
            }         
    elif col == 'religion':         
        collection_schema = {
            'country' : {
                'type' : 'string',
                'required': True
                },
            'name' : {
                'type' : ["string"],
                'required': True
                },
            'percentage' : {
                'type' :  [ "double","int" ]
                }
            } 
    elif col == 'borders':         
       collection_schema = {
           'country1' : {
               'type' : 'string',
               'required': True
               },
           'country2' : {
               'type' : ["string"],
               'required': True
               },
           'length' : {
               'type' :  [ "double", "int" ]
               }
           } 
    elif col == 'province':         
       collection_schema = {
           'name' : {
               'type' : 'string',
               'required': True
               },
           'country' : {
               'type' : "string",
               'required': True
               },
           'area' : {
               'type' :  ["int", "double"]
               },
           'population' : {
               'type' :  ["int", "string"]
               },
           'capprov' : {
               'type' :  "string"
               }
           } 
    elif col == 'city':         
       collection_schema = {
           'name' : {
               'type' : 'string',
               'required': True
               },
           'country' : {
               'type' : "string",
               'required': True
               },
           'province' : {
               'type' :  "string",
               'required': True
               },
           'population' : {
               'type' :  ["int", "double", "string"]
               },
           'elevation' : {
               'type' :  ["int", "double", "string"]
               },
           'latitude' : {
               'type' :  ["int", "double", "string"],
                "minimum":  -90.0,
                "maximum" : 90.0
               },
           'longitude' : {
               'type' :  ["int", "double", "string"],
                "minimum":  -180.0,
                "maximum" : 180.0
           } 
       }
    elif col == 'provincelocalname':         
       collection_schema = {
           'province' : {
               'type' : 'string',
               'required': True
               },
           'localname' : {
               'type' : "string"
               },
           'country' : {
               'type' :  "string"
               }
       }
    elif col == 'provinceothername':         
       collection_schema = {
           'province' : {
               'type' : 'string',
               'required': True
               },
           'othername' : {
               'type' : "string",
               'required': True
               },
           'country' : {
               'type' :  "string"
               }
       }
    elif col == 'provincepopulation':         
       collection_schema = {
           'province' : {
               'type' : 'string',
               'required': True
               },
           'population' : {
               'type' : "int",
               'required': True
               },
           'year' : {
               'type' :  "int",
               'required': True
               }
       }
    elif col == 'citylocalname':         
       collection_schema = {
           'country' : {
               'type' : 'string',
               'required': True
               },
           'city' : {
               'type' : "string",
               'required': True
               },
           'province' : {
               'type' :  "string",
               'required': True
               },
           'localname' : {
               'type' :  "string"
               }
       }
    elif col == 'cityothername':         
       collection_schema = {
           'country' : {
               'type' : 'string',
               'required': True
               },
           'city' : {
               'type' : "string",
               'required': True
               },
           'province' : {
               'type' :  "string",
               'required': True
               },
           'othername' : {
               'type' :  "string",
               'required': True
               }
       }       
    elif col == 'citypopulations':         
       collection_schema = {
           'country' : {
               'type' : 'string',
               'required': True
               },
           'city' : {
               'type' : "string",
               'required': True
               },
           'province' : {
               'type' :  "string",
               'required': True
               },
           'population' : {
               'type' :  "int",
               'required': True
               },
           'year' : {
               'type' :  "int",
               'required': True
               }
       }   
    elif col == 'island':         
       collection_schema = {
           'city' : {
               'type' : 'string',
               'required': True
               },
           'island' : {
               'type' : "string",
               'required': True
               },
           'country' : {
               'type' :  "string"
               },
           'province' : {
               'type' :  "string",
               'required': True
               }
           }  
    elif col == 'organization':         
       collection_schema = {
           'country' : {
               'type' : 'string'
               },
           'abbreviation' : {
               'type' : "string",
               'required': True
               },
           'name' : {
               'type' :  "string"
               },
           'city' : {
               'type' :  "string"
               },
           'province' : {
               'type' :  "string"
               },
           'established' : {
               'type' :  ["date", "string"]
               }
           }  
    elif col == 'ismember':         
       collection_schema = {
           'organization' : {
               'type' : 'string',
               'required': True
               },
           'country' : {
               'type' : "string",
               'required': True
               },
           'type' : {
               'type' :  "string"
               }
           }  
    elif col == 'continent':         
       collection_schema = {
           'country_code' : {
               'type' : 'string',
               'required': True
               },
           'encompasses_continent' : {
               'type' : "string",
               'required': True
               },
           'encompass_percentage' : {
               'type' : ["double", "int", "string"],
                "minimum":  0.0,
                "maximum" : 100.0
               },
           'continent_area' : {
               'type' :  ["double", "int", "string"]
               }
           }  
    elif col == 'airport':         
       collection_schema = {
           'iatacode' : {
               'type' : 'string',
               'required': True
               },
           'name' : {
               'type' : "string"
               },
           'city' : {
               'type' : "string"
               },
           'airport_province' : {
               'type' :  "string"
               },
           'country_code' : {
               'type' :  "string"
               },
           'island' : {
               'type' :  "string"
               },
           'latitude' : {
               'type' :  ["double", "int", "string"],
                "minimum":  -90.0,
                "maximum" : 90.0
               },
           'longitude' : {
               'type' :  ["double", "int", "string"],
                "minimum":  -180.0,
                "maximum" : 180.0
               },
           'elevation' : {
               'type' :  ["double", "int", "string"]
               },
           'gmtOffset' : {
               'type' :  ["double", "int", "string"]
               }
           }  
                   
    return collection_schema

if __name__ == '__main__':
    
    mydb = connectDB()

    collections = ['country', 'country_other_localname', 'countrypopulations', 'economy', 'ethnicgroup', 
                   'language', 'politics', 'population', 'religion', 'borders', 'province', 'city',
                   'provincelocalname', 'provinceothername', 'provincepopulation', 'citylocalname',
                   'cityothername', 'citypopulations', 'island', 'organization', 'ismember', 'continent',
                   'airport']

    print(len(collections))

    for col in collections:
        
        schema = collection_schema(col)
        collection = col


        validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
        required = []
        
        for field_key in schema:
            field = schema[field_key]
            properties = {'bsonType': field['type']}
            
            minimum = field.get('minimum')
            maximum = field.get('maximum')
        
            if type(minimum) == int or type(minimum) == float:
                properties['minimum'] = minimum
            if type(maximum) == int or type(maximum) == float:
                properties['maximum'] = maximum
        
            if field.get('required') is True: required.append(field_key)
            
            validator['$jsonSchema']['properties'][field_key] = properties
        
        if len(required) > 0:
            validator['$jsonSchema']['required'] = required
        
        query = [('collMod', collection),
                 ('validator', validator)]
        
        try:
            mydb.create_collection(collection)
        except CollectionInvalid:
            pass
        
        command_result = mydb.command(OrderedDict(query))
