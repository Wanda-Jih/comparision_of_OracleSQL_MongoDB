# Comaprision of Oracle SQL and MongoDB

### Part 1 – Understanding the data 
### 1-1	
Is each column present in every data entry? List which columns do not appear in every data entry.


![](https://i.imgur.com/jhUnmGX.png)


### 1-2 
Given the file descriptions and the knowledge graph, are there any redundant columns in the files?\
List which files have redundant columns. Name the columns and provide reasons why, in your opinion, those columns are redundant?

![](https://i.imgur.com/9z4etI1.png)

### 1-3	
What logical constraints would you set for which columns in the files? For example, latitude should always be in the range of [-90, 90], and the longitude should be in [-180, 180]. Here you don't have to set constraints for every column of every file.

![](https://i.imgur.com/aAJrVWs.png)


### Part 2 – Relational database schema

### 2-1
Write an SQL script that contains the schema for the storage and manipulation of the data  provided in the JSON files. 
See [```./sql_schema/project2_schema.sql```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/sql_schema/project2_schema.sql) for the Oracle SQL schema script.
(Use Oracle SQL Developer to run sql file)

### 2-2
Compile the entity-relationship diagram of your database.
![](https://i.imgur.com/rQttqph.png)


### Part 3 – Inserting the data to Oracle DBMS

### Environment
This part will use python3 and Oracle SQL Developer.

### Execution Steps
1. Execute python file to create insert values for Oracle database. The output will be in [```./sql_schema/project2_data.sql```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/sql_schema/project2_data.sql) 
See [```./sql_schema/createInsertValue_sql.py```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/sql_schema/createInsertValue_sql.py) 

    Executive Command:
```python sql_schema/createInsertValue_sql.py```

2. Execute sql file to insert values into Oracle SQL database.
See [```./sql_schema/project2_data.sql```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/sql_schema/project2_data.sql) 
(Use Oracle SQL Developer to run sql file)
(It is possible to take a long to insert values into database)

### Part 4 - Using MongoDB

### Environment
This part will use python3 and [MongoDB(3.6)](https://www.mongodb.com/try/download/community).
The reason for using MongoDB (3.6) is that we need to use a tool - [mongoimport](https://docs.mongodb.com/database-tools/mongoimport/).

After downloading MongoDB(3.6), put ```~/MongoDB/Server/3.6/bin``` into environment variables.

### Execution Steps
1. Create MongoDB schema
Execute python file to create MongoDB schema. It will generate 23 collections in MongoDB.
See [```./mongodb_schema/mongodb_schema.py```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/mongodb_schema/mongodb_schema.py) 

    Executive Command:
```python mongodb_schema/mongodb_schema.py```

2. Create json files for the data for MongoDB
Execute python file to create json files for inserting values in MongoDB. The output json files will be in [```./mongodb_data```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/tree/main/mongodb_schema/mongodb_data) directory.
See [```./mongodb_schema/insertValue_mongodb.py```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/mongodb_schema/insertValue_mongodb.py)

    Executive Command:
```python mongodb_schema/insertValue_mongodb.py```

3. Insert data into MongoDB
Click bat file to insert data into MongoDB. 
See [```./mongodb_schema/import_data_mongodb.bat```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/mongodb_schema/import_data_mongodb.bat)

    Executive command in bat file (Samples)
```
mongoimport --db project2 --collection language .\mongodb_data\language.json --jsonArray
mongoimport --db project2 --collection politics .\mongodb_data\politics.json --jsonArray
```

### Part 5 – Queries

### Environment
This part will use python3 and Oracle SQL Developer.

### 5-1

Implement the following queries in both Oracle and MongoDB. For each of the following queries, capture the execution time for both DBMS environments (question 5-2).

#### a
Select the name of the country that shares the longest border with one or more other countries.

•	Oracle: [query/oracle_query/ 5-1-a.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-a.sql)
	
•   MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 1```


#### b	
For each country, list the city that has the maximum average population.

•	Oracle: [query/oracle_query/ 5-1-b.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-b.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 2```

#### c
List the following information of the countries where agriculture contributes the most to their economy. Name of the country, its GDP, percentage contribution from agriculture, and inflation.

•	Oracle: [query/oracle_query/ 5-1-c.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-c.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 3```

#### d	
List the following information of the countries in the descending order of their ethnic diversity. Name of the country, number of ethnic groups, and the percentage of the major ethnicity. Ethnic diversity of a country increases as the number of ethnic groups that live in the country increases.

•	Oracle: [query/oracle_query/ 5-1-d.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-d.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 4```

#### e	
Find the number of countries with the number of ethnic groups equal to the number of languages used.

•	Oracle: [query/oracle_query/ 5-1-e.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-e.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 5```

#### f
The GDP and IMR (infant mortality rate) together define the development of a country. Find the top 10 countries with the highest GDP (in decreasing order) and their corresponding IMR value.

•	Oracle: [query/oracle_query/ 5-1-f.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-f.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 6```

#### g
Find the following information of the country with the highest religious freedom. Name of the country, the religions that are practiced in the country. Note that the larger the number of religions practiced in a country, the higher its religious freedom is.

•	Oracle: [query/oracle_query/ 5-1-g.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-g.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 7```

#### h	
What is the proportion of commonwealth countries in the top 100 countries in terms of GDP.

•	Oracle: [query/oracle_query/ 5-1-h.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-h.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 8```

#### i
Find the country with the largest population density in each continent. List the name of the country and its population density against the name of the continent. The population density of a country is the ratio between its total population and area.

•	Oracle: [query/oracle_query/ 5-1-i.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-i.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 9```

#### j
Find the names of countries and their capitals where the capital has more than one airport.

•	Oracle: [query/oracle_query/ 5-1-j.sql](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/5-1-j.sql)

•	MongoDB: [query/mongodb_query/mongodb_query.py](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

Executive Command:
```python query/mongodb_query/ mongodb_query.py 10```

### 5-2

Create a table to summarize the execution time in the two DBMS for each of the queries.
![](https://i.imgur.com/sAu50Zi.png)

### 5-3

Comment on the execution times you have obtained. Give educated reasons why one DBMS has performed better than the other?

In the above form, most of MongoDB’s execution times are better than Oracle because MongoDB has less constraints. Thus, compare to Oracle SQL, we need less checks when we execute the query in MongoDB.

For the few cases, MongoDB’s execution times are worse than Oracle. From my observation, MongoDB performs worse than Oracle SQL if we need to use multiple collections/tables. It is possible that the Oracle SQL Database will cache and create automatically indexing internally.

### 5-4 
Suggest one performance improvement technique that you can use on each DBMS to improve the performance. Implement your technique on each DBMS and report your results in a table similar to questions 5-2.

* Oracle

Use the “[CREATE INMEMORY JOIN GROUP](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/sqlrf/CREATE-INMEMORY-JOIN-GROUP.html#GUID-87CA7034-4F80-4D46-8EE1-5CC865C2D676)” statement to create a join group, which is an object that specifies frequently joined columns from the same table or different tables. When you create a join group, Oracle Database stores special metadata for the columns in the global dictionary, which enables the database to optimize join queries for the columns.

Because code in country table and country in city table are frequently used by the queries, so I use the above method to create a join group.

See [```query/oracle_query/optimized.sql```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/oracle_query/optimized.sql)


* MongoDB

[Create Indexes to Support Queries](https://docs.mongodb.com/manual/tutorial/optimize-query-performance-with-indexes-and-projections/). If a query searches multiple fields, create a compound index. Scanning an index is much faster than scanning a collection. 

See the function - optimizedDB(db) in [```query/mongodb_query/mongodb_query.py```](https://github.com/Wanda-Jih/comparision_of_OracleSQL_MongoDB/blob/main/query/mongodb_query/mongodb_query.py)

* Eexecution time

![](https://i.imgur.com/kJx8Bc2.png)

### 5-5 
Comment on the execution times you have obtained after implementing your performance improvement technique. How much improvement do you observe compared to your results in 5-2?

* Oracle

All queries reduce their execution time. Because almost every query uses country table - code or city table - country. The higher the frequency they use, the more the execution time is reduced.

* MongoDB

All queries reduce their execution time. If the query needs to scan different collections, the execution time will be reduced even more. Because I store the fields in the index, scanning the index can reduce the execution time.
