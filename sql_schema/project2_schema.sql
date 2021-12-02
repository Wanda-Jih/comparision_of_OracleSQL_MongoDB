
-- country
CREATE TABLE country
  (
    name VARCHAR2( 255 ),
    code VARCHAR2( 255 ) PRIMARY KEY,
    capital VARCHAR2( 255 ),
    area NUMBER NOT NULL,
    population NUMBER
  );

-- country_other_localname
CREATE TABLE country_other_localname
  (
    country VARCHAR2( 255 ) PRIMARY KEY,
    localname VARCHAR2( 255 ) NOT NULL,
    othername VARCHAR2( 255 ),
    CONSTRAINT fk_country_countryotherlocalname
        FOREIGN KEY( country )
        REFERENCES country( code )
        ON DELETE CASCADE
  );

-- countrypopulations
CREATE TABLE countrypopulations
  (
    country VARCHAR2( 255 ),
    population NUMBER,
    year NUMBER NOT NULL,
    CONSTRAINT pk_countrypopulations
      PRIMARY KEY( country, population),
    CONSTRAINT fk_country_countrypopulations
        FOREIGN KEY( country )
        REFERENCES country( code )
        ON DELETE CASCADE
  );

-- economy
CREATE TABLE economy
  (
    country VARCHAR2( 255 ) PRIMARY KEY,
    GDP NUMBER,
    agriculture NUMBER,
    service NUMBER,
    industry NUMBER,
    inflation NUMBER,
    unemployment NUMBER,
    CONSTRAINT fk_country_economy
        FOREIGN KEY( country)
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT CHK_agriculture
        CHECK (agriculture >= 0 AND agriculture <= 100),
    CONSTRAINT CHK_service
        CHECK (service >= 0 AND service <= 100),
    CONSTRAINT CHK_industry
        CHECK (industry >= 0 AND industry <= 100),
    CONSTRAINT CHK_unemployment
        CHECK (unemployment >= 0 AND unemployment <= 100)
      );

-- ethnicgroup
CREATE TABLE ethnicgroup
  (
    country_code VARCHAR2( 255 ),
    ethnic_group_name VARCHAR2( 255),
    ethnic_group_percentage NUMBER,
    CONSTRAINT pk_ethnicgroup
      PRIMARY KEY( country_code, ethnic_group_name),
    CONSTRAINT fk_country_ethnicgroup
        FOREIGN KEY( country_code)
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT CHK_ethnic_group_percentage
        CHECK (ethnic_group_percentage >= 0 AND ethnic_group_percentage <= 100)
      );

-- language
CREATE TABLE language
  (
    country VARCHAR2( 255 ),
    language VARCHAR2( 255),
    percentage NUMBER,
    CONSTRAINT pk_language
      PRIMARY KEY( country, language),
    CONSTRAINT fk_country_language
        FOREIGN KEY( country)
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT CHK_percentage
        CHECK (percentage >= 0 AND percentage <= 100)
      );

-- politics
CREATE TABLE politics
  (
    country VARCHAR2( 255 ) PRIMARY KEY,
    independence DATE,
    wasdependent VARCHAR2( 255 ),
    dependent VARCHAR2( 255 ),
    government VARCHAR2( 255 ),
    CONSTRAINT fk_country_politics
        FOREIGN KEY( country)
        REFERENCES country( code )
        ON DELETE CASCADE,
--    CONSTRAINT fk_wasdependent_politics
--        FOREIGN KEY( wasdependent)
--        REFERENCES country( code )
--        ON DELETE CASCADE,
    CONSTRAINT fk_dependent_politics
        FOREIGN KEY( dependent)
        REFERENCES country( code )
        ON DELETE CASCADE
      );

-- population
CREATE TABLE population
  (
    country_code VARCHAR2( 255) PRIMARY KEY,
    population_growth NUMBER,
    infant_mortality NUMBER,
    CONSTRAINT fk_country_population
        FOREIGN KEY( country_code)
        REFERENCES country( code )
        ON DELETE CASCADE
      );

-- religion
CREATE TABLE religion
  (
    country VARCHAR2( 255 ),
    name VARCHAR2( 255 ),
    percentage NUMBER NOT NULL,
    CONSTRAINT pk_religion
      PRIMARY KEY( country , name ),
    CONSTRAINT fk_country_religion
        FOREIGN KEY( country)
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT CHK_percentage_religion
        CHECK (percentage >= 0 AND percentage <= 100)
      );

-- borders
CREATE TABLE borders
  (
    country1 VARCHAR2( 255 ),
    country2 VARCHAR2( 255 ),
    length NUMBER NOT NULL,
    CONSTRAINT pk_borders 
      PRIMARY KEY( country1, country2 ),
    CONSTRAINT fk_country1_borders
        FOREIGN KEY( country1 )
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT fk_country2_borders
        FOREIGN KEY( country2 )
        REFERENCES country( code )
        ON DELETE CASCADE
  );

-- province
CREATE TABLE province
  (
    name VARCHAR2( 255 ),
    country VARCHAR2( 255 ) NOT NULL,
    area NUMBER  NOT NULL,
    population NUMBER,
    capprov VARCHAR2( 255 ),
    CONSTRAINT pk_province
        PRIMARY KEY(name, country),
    CONSTRAINT fk_province_province
        FOREIGN KEY( capprov, country )
        REFERENCES province( name, country )
        ON DELETE CASCADE,
    CONSTRAINT fk_country_province
        FOREIGN KEY( country )
        REFERENCES country( code )
        ON DELETE CASCADE
      );

-- city
CREATE TABLE city
  (
    name VARCHAR2( 255 ),
    country VARCHAR2( 255 ),
    province VARCHAR2( 255 ),
    population NUMBER,
    elevation NUMBER,
    latitude NUMBER NOT NULL,
    longitude NUMBER NOT NULL,
    CONSTRAINT pk_city
      PRIMARY KEY( name, country, province ),    
    CONSTRAINT fk_country_city
        FOREIGN KEY( country )
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT fk_province_city
        FOREIGN KEY( province, country )
        REFERENCES province( name, country )
        ON DELETE CASCADE,
    CONSTRAINT CHK_latitude_city
        CHECK (latitude >= -90 AND latitude <= 90),
    CONSTRAINT CHK_longitude_city
        CHECK (longitude >= -180 AND longitude <= 180)
  );
  
-- provincelocalname
CREATE TABLE provincelocalname
  (
    province VARCHAR2( 255 ) PRIMARY KEY,
    localname VARCHAR2( 255 ) NOT NULL,
    country VARCHAR2( 255 ) NOT NULL,
    CONSTRAINT fk_province_provincelocalname
        FOREIGN KEY( province, country)
        REFERENCES province( name, country)
        ON DELETE CASCADE
      );

-- provinceothername
CREATE TABLE provinceothername
  (
    province VARCHAR2( 255 ),
    othername VARCHAR2( 255 ),
    country VARCHAR2( 255 ) NOT NULL,
    CONSTRAINT pk_provinceothername
      PRIMARY KEY( province, othername ), 
    CONSTRAINT fk_province_provinceothername
        FOREIGN KEY( province, country )
        REFERENCES province( name, country )
        ON DELETE CASCADE
      );

-- provincepopulation
CREATE TABLE provincepopulation
  (
    province VARCHAR2( 255 ),
    population NUMBER,
    year NUMBER(4) NOT NULL,
    country VARCHAR2( 255 ) NOT NULL,
    CONSTRAINT pk_provincepopulation
      PRIMARY KEY( province, population, year ), 
    CONSTRAINT fk_province_provincepopulation
        FOREIGN KEY( province, country )
        REFERENCES province( name, country )
        ON DELETE CASCADE
      );

-- citylocalname
CREATE TABLE citylocalname
  (
    country VARCHAR2( 255 ),
    city VARCHAR2( 255 ),
    province VARCHAR2( 255 ),
    localname VARCHAR2( 255 ) NOT NULL,
    CONSTRAINT pk_citylocalname
      PRIMARY KEY( city, country, province ), 
    CONSTRAINT fk_city_citylocalname
        FOREIGN KEY( city, country, province )
        REFERENCES city( name, country, province )
        ON DELETE CASCADE
  );

-- cityothername
CREATE TABLE cityothername
  (
    country VARCHAR2( 255 ),
    city VARCHAR2( 255 ),
    province VARCHAR2( 255 ),
    othername VARCHAR2( 255 ) NOT NULL,
    CONSTRAINT pk_cityothername
        PRIMARY KEY( city, country, province, othername ), 
    CONSTRAINT fk_city_cityothername
        FOREIGN KEY( city, country, province )
        REFERENCES city( name, country, province )
        ON DELETE CASCADE
  );

-- citypopulations
CREATE TABLE citypopulations
  (
    country VARCHAR2( 255 ),
    city VARCHAR2( 255 ),
    province VARCHAR2( 255 ),
    population NUMBER,
    year NUMBER,
    CONSTRAINT pk_citypopulations
        PRIMARY KEY( city, country, province, population, year ), 
    CONSTRAINT fk_city_citypopulations
        FOREIGN KEY( city,  country, province)
        REFERENCES city( name, country, province )
        ON DELETE CASCADE
  );

-- island
CREATE TABLE island
  (
    city VARCHAR2( 255 ),
    island VARCHAR2( 255),
    country VARCHAR2( 255 ),
    province VARCHAR2( 255 ), 
    CONSTRAINT pk_island
      PRIMARY KEY( city , island, province ),
    CONSTRAINT fk_city_island
        FOREIGN KEY( city, country, province )
        REFERENCES city( name, country, province )
        ON DELETE CASCADE
      );

-- organization
CREATE TABLE organization
  (
    country  VARCHAR2( 255),
    abbreviation VARCHAR2( 255) PRIMARY KEY,
    name VARCHAR2( 255 ) NOT NULL,
    city VARCHAR2( 255),
    province VARCHAR2( 255),
    established DATE,
    CONSTRAINT fk_city_organization
        FOREIGN KEY( city, country, province )
        REFERENCES city( name, country, province )
        ON DELETE CASCADE
      );
      
-- ismember
CREATE TABLE ismember
  (
    organization VARCHAR2( 255 ) NOT NULL,
    country VARCHAR2( 255),
    type VARCHAR2( 255 ) NOT NULL,
    CONSTRAINT pk_ismember
      PRIMARY KEY( organization, country),
    CONSTRAINT fk_organization_ismember
        FOREIGN KEY( organization)
        REFERENCES organization( abbreviation )
        ON DELETE CASCADE,
    CONSTRAINT fk_country_ismember
        FOREIGN KEY( country)
        REFERENCES country( code )
        ON DELETE CASCADE
      );

-- continent
CREATE TABLE continent
  (
    country_code VARCHAR2( 255 ),
    encompasses_continent VARCHAR2( 255 ),
    encompass_percentage NUMBER NOT NULL,
    continent_area NUMBER NOT NULL,
    CONSTRAINT pk_continent
        PRIMARY KEY( country_code, encompasses_continent ),
    CONSTRAINT fk_countrycode_continent
        FOREIGN KEY( country_code )
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT CHK_encompass_percentage
        CHECK (encompass_percentage >= 0 AND encompass_percentage <= 100)
  );

     
--------------------------------------------
  

-- airport
CREATE TABLE airport
  (
    iatacode VARCHAR2( 255 ) PRIMARY KEY,
    name VARCHAR2( 255 ) NOT NULL,
    city VARCHAR2( 255 ),
    airport_province VARCHAR2( 255 ),
    country_code VARCHAR2( 255 ) NOT NULL,
    island  VARCHAR2( 255 ),   
    latitude NUMBER NOT NULL,
    longitude NUMBER NOT NULL,
    elevation NUMBER,
    gmtOffset NUMBER NOT NULL,
    CONSTRAINT fk_country_airport
        FOREIGN KEY( country_code )
        REFERENCES country( code )
        ON DELETE CASCADE,
    CONSTRAINT fk_city_airport
        FOREIGN KEY( city, country_code, airport_province )
        REFERENCES city( name, country, province )
        ON DELETE CASCADE,
--    CONSTRAINT fk_island_airport
--        FOREIGN KEY( city, island, airport_province )
--        REFERENCES island( city , island, province )
--        ON DELETE CASCADE,
    CONSTRAINT CHK_latitude_airport
        CHECK (latitude >= -90 AND latitude <= 90),
    CONSTRAINT CHK_longitude_airport
        CHECK (longitude >= -180 AND longitude <= 180)
  );
