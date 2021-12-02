import pandas as pd

def readData(path):

    # Load the json into a DataFrame
    df = pd.read_json(SourceFile)
    df = pd.json_normalize(df['results'])
    DataDict = df['items'][0]
    return DataDict

def create_commands(file, DataDict, list_string, tableName):
    for i in range(len(DataDict)):
        if tableName == 'country' and i < len(DataDict)-1 and list(DataDict[i+1].values())[0] == list(DataDict[i].values())[0]:
            print(list(DataDict[i+1].values())[0])
            continue
   
            
        value_list = []
        for j in range(len(DataDict[i])):
            value_list.append(list(DataDict[i].values())[j])
        
        value_string = ""
        for e in value_list:
            asp = "\'"

            if e == "":
                value_string += "NULL"
            elif type(e) == str:
                if asp in e:
                    e = e.replace("'", "''")
                value_string += "'" + e + "'" 
            else:
                value_string += str(e)
            value_string += ", "
        value_string = value_string[:-2]
        
        command = "INSERT INTO  " + tableName + " ( " + list_string + " ) VALUES ( " + value_string + " );\n"
        file.write(command)  
    file.write("\n")
   
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

def constrinat_action_fk(file, selectAction):
    if selectAction == 0:
        action = "DISABLE"
    else:
        action = "ENABLE"
        
    file.write("ALTER TABLE airport " + action + " CONSTRAINT fk_country_airport;\n")    
    file.write("ALTER TABLE airport " + action + " CONSTRAINT fk_city_airport;\n")      
    file.write("ALTER TABLE airport " + action + " CONSTRAINT CHK_latitude_airport;\n")     
    file.write("ALTER TABLE airport " + action + " CONSTRAINT CHK_longitude_airport;\n")   
    # file.write("ALTER TABLE airport " + action + " CONSTRAINT fk_island_airport;\n")     
    file.write("ALTER TABLE borders " + action + " CONSTRAINT fk_country1_borders;\n")   
    file.write("ALTER TABLE borders " + action + " CONSTRAINT fk_country2_borders;\n")  
    file.write("ALTER TABLE city " + action + " CONSTRAINT fk_country_city;\n")  
    file.write("ALTER TABLE city " + action + " CONSTRAINT fk_province_city;\n")  
    file.write("ALTER TABLE city " + action + " CONSTRAINT CHK_latitude_city;\n")  
    file.write("ALTER TABLE city " + action + " CONSTRAINT CHK_longitude_city;\n")   
    file.write("ALTER TABLE citylocalname " + action + " CONSTRAINT fk_city_citylocalname;\n") 
    file.write("ALTER TABLE cityothername " + action + " CONSTRAINT fk_city_cityothername;\n") 
    file.write("ALTER TABLE citypopulations " + action + " CONSTRAINT fk_city_citypopulations;\n")
    file.write("ALTER TABLE country_other_localname " + action + " CONSTRAINT fk_country_countryotherlocalname;\n")
    file.write("ALTER TABLE countrypopulations " + action + " CONSTRAINT fk_country_countrypopulations;\n")
    file.write("ALTER TABLE economy " + action + " CONSTRAINT fk_country_economy;\n")       
    file.write("ALTER TABLE economy " + action + " CONSTRAINT CHK_agriculture;\n") 
    file.write("ALTER TABLE economy " + action + " CONSTRAINT CHK_service;\n") 
    file.write("ALTER TABLE economy " + action + " CONSTRAINT CHK_industry;\n") 
    file.write("ALTER TABLE economy " + action + " CONSTRAINT CHK_unemployment;\n")      
    file.write("ALTER TABLE ethnicgroup " + action + " CONSTRAINT fk_country_ethnicgroup;\n")      
    file.write("ALTER TABLE ethnicgroup " + action + " CONSTRAINT CHK_ethnic_group_percentage;\n")      
    file.write("ALTER TABLE ismember " + action + " CONSTRAINT fk_organization_ismember;\n")    
    file.write("ALTER TABLE ismember " + action + " CONSTRAINT fk_country_ismember;\n")       
    file.write("ALTER TABLE language " + action + " CONSTRAINT fk_country_language;\n")   
    file.write("ALTER TABLE language " + action + " CONSTRAINT CHK_percentage;\n")   
    file.write("ALTER TABLE island " + action + " CONSTRAINT fk_city_island;\n")    
    file.write("ALTER TABLE organization " + action + " CONSTRAINT fk_city_organization;\n")  
    file.write("ALTER TABLE politics " + action + " CONSTRAINT fk_country_politics;\n")  
    file.write("ALTER TABLE politics " + action + " CONSTRAINT fk_dependent_politics;\n")  
    # file.write("ALTER TABLE politics " + action + " CONSTRAINT fk_wasdependent_politics;\n")  
    file.write("ALTER TABLE population " + action + " CONSTRAINT fk_country_population;\n")     
    file.write("ALTER TABLE province " + action + " CONSTRAINT fk_province_province;\n")   
    file.write("ALTER TABLE province " + action + " CONSTRAINT fk_country_province;\n") 
    file.write("ALTER TABLE provincelocalname " + action + " CONSTRAINT fk_province_provincelocalname;\n")   
    file.write("ALTER TABLE provinceothername " + action + " CONSTRAINT fk_province_provinceothername;\n")   
    file.write("ALTER TABLE provincepopulation " + action + " CONSTRAINT fk_province_provincepopulation;\n")   
    file.write("ALTER TABLE religion " + action + " CONSTRAINT fk_country_religion;\n")   
    file.write("ALTER TABLE religion " + action + " CONSTRAINT CHK_percentage_religion;\n")   
    file.write("ALTER TABLE continent " + action + " CONSTRAINT fk_countrycode_continent;\n")   
    file.write("ALTER TABLE continent " + action + " CONSTRAINT CHK_encompass_percentage;\n") 
       
    file.write("\n")   

    
if __name__ == "__main__":
             
    sqlFile = "./project2_data.sql"
    file = open( sqlFile, "w", encoding="utf-8")
  
    constrinat_action_fk(file, 0)
    
    tableNames = ['airport', 'borders', 'city', 'citylocalname', 'cityothername', 'citypopulations', 
                  'country', 'country-other-localname', 'countrypopulations', 'economy', 'ethnicgroup',
                  'ismember', 'language', 'located-on', 'organization', 'politics', 'population', 'province',
                  'provincelocalname', 'provinceothername', 'provincepopulation', 'religion', 'continent']
    

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
            
        file.write("REM INSERTING into " + tableName.upper() +" \nSET DEFINE OFF;\n")
        
        redundant_list = redundant_col(tableName)
        list_column = list(DataDict[0].keys())
        print(redundant_list)
        for col in redundant_list:
            list_column.remove(col)
        list_string = ", ".join(list_column)
        if tableName == 'continent':
            list_string = list_string.replace("code", "country_code")
        
        
        for i in range(len(DataDict)):
            for col in redundant_list:
                DataDict[i].pop(str(col))         
                
        create_commands(file, DataDict, list_string, tableName)

    constrinat_action_fk(file, 1)
    file.close()

                                                                                




