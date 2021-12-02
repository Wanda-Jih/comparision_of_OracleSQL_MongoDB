import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["project2"]

tableNames = ['airport', 'borders', 'city', 'citylocalname', 'cityothername', 'citypopulations', 
              'country', 'country_other_localname', 'countrypopulations', 'economy', 'ethnicgroup',
              'ismember', 'language', 'island', 'organization', 'politics', 'population', 'province',
              'provincelocalname', 'provinceothername', 'provincepopulation', 'religion', 'continent']
# tableNames = ['country']
# mydb.mycol.remove()
for tlist in tableNames:
    
    mycol = mydb[tlist]
    # for i in mycol:
    #     print(i)
    # print(mycol)
    mycol.drop()