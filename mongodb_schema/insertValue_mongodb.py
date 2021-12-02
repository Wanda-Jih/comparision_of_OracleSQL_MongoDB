import pandas as pd
import os


def readData(path):

    # Load the json into a DataFrame
    df = pd.read_json(SourceFile)
    df = pd.json_normalize(df['results'])
    DataDict = df['items'][0]
    return DataDict
  
def redundant_col(tableName):
    
    redundant_list = []
    if tableName == 'airport':
        redundant_list.append("country_name")
    elif tableName == 'city':
        redundant_list.append("country_name")
        redundant_list.append("country_capital")
    elif tableName == 'cityothername':
        redundant_list.append("country_area")
        redundant_list.append("country_capital")
    elif tableName == 'country':
        redundant_list.append("province")
        redundant_list.append("encompasses_continent")
        redundant_list.append("encompass_percentage")
        redundant_list.append("continent_area")
    elif tableName == 'countrypopulations':
        redundant_list.append("name")
        redundant_list.append("capital")
    elif tableName == 'ethnicgroup':
        redundant_list.append("country")
        redundant_list.append("country_capital")  
    elif tableName == 'language':
        redundant_list.append("country_area")
        redundant_list.append("country_capital")    
    elif tableName == 'island':
        redundant_list.append("province_area")       
    elif tableName == 'population':
        redundant_list.append("country_name")
        redundant_list.append("country_province")  
    elif tableName == 'province':
        redundant_list.append("capital")      
    elif tableName == 'religion':
        redundant_list.append("country_name") 
        redundant_list.append("country_population")        
    elif tableName == 'continent':
        redundant_list.append("name") 
        redundant_list.append("capital") 
        redundant_list.append("province") 
        redundant_list.append("area") 
        redundant_list.append("population") 

    return redundant_list    

def create_insert_data(file, DataDict, list_column, tableName):
            
    # file.write("db.project2.airport(\n")
    file.write("[\n")
    for i in range (len(DataDict)):
        if tableName == 'country' and i < len(DataDict)-1 and list(DataDict[i+1].values())[0] == list(DataDict[i].values())[0]:
            print(list(DataDict[i+1].values())[0])
            continue
   

        value_list = []
        for j in range(len(DataDict[i])):
            if tableName == 'country' and j == 3:
                value_list.append(float(list(DataDict[i].values())[j]))
                continue
            if tableName == 'economy' and j != 0 and list(DataDict[i].values())[j] != '':
                value_list.append(float(list(DataDict[i].values())[j])) 
                continue
            value_list.append(list(DataDict[i].values())[j])
   
 
        file.write("\t{ ")
        for k in range(len(list_column)):
            if type(value_list[k]) == str:
                value_list[k] = str('"' + value_list[k] + '"')
            file.write('"' + str(list_column[k]) +'": '+ str(value_list[k]))
            
            if k != len(DataDict[i]) - 1:
                file.write(", ")

        if i == len(DataDict) - 1:
            file.write("}\n")
        else:
            file.write("},\n")
    file.write("]\n")        
        

    
if __name__ == "__main__":
             
    directory = "./mongodb_data"
    if not os.path.exists(directory):
        os.makedirs(directory)
  
    
    tableNames = ['airport', 'borders', 'city', 'citylocalname', 'cityothername', 'citypopulations', 
                  'country', 'country-other-localname', 'countrypopulations', 'economy', 'ethnicgroup',
                  'ismember', 'language', 'located-on', 'organization', 'politics', 'population', 'province',
                  'provincelocalname', 'provinceothername', 'provincepopulation', 'religion', 'continent']
    
    # tableNames = ['economy']

    for tableName in tableNames:
       
        print(tableName)
        if tableName == 'continent':
            SourceFile = '../dataset/country.json'
        else:
            SourceFile = '../dataset/' + tableName +'.json'
        DataDict = readData(SourceFile)
    
        if tableName == "country-other-localname":
            tableName = "country_other_localname"
        elif tableName == "located-on":
            tableName = "island"
            
        sqlFile = "./mongodb_data/" + tableName + ".json"
        file = open( sqlFile, "w", encoding="utf-8")
        
        redundant_list = redundant_col(tableName)
        list_column = list(DataDict[0].keys())
        print(redundant_list)
        for col in redundant_list:
            list_column.remove(col)
         
        print(list_column)
        if tableName == 'continent':
            new_list_column = []
            for string in list_column:
                new_string = string.replace("code", "country_code")
                new_list_column.append(new_string)
            list_column = new_list_column
 
        
        for i in range(len(DataDict)):
            for col in redundant_list:
                DataDict[i].pop(str(col))         
         
        create_insert_data(file, DataDict, list_column, tableName)
        
        
        
    file.close()

                                                                                




