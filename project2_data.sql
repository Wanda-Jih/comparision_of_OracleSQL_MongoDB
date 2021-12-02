ALTER TABLE airport DISABLE CONSTRAINT fk_country_airport;
ALTER TABLE airport DISABLE CONSTRAINT fk_city_airport;
ALTER TABLE airport DISABLE CONSTRAINT CHK_latitude_airport;
ALTER TABLE airport DISABLE CONSTRAINT CHK_longitude_airport;
ALTER TABLE borders DISABLE CONSTRAINT fk_country1_borders;
ALTER TABLE borders DISABLE CONSTRAINT fk_country2_borders;
ALTER TABLE city DISABLE CONSTRAINT fk_country_city;
ALTER TABLE city DISABLE CONSTRAINT fk_province_city;
ALTER TABLE city DISABLE CONSTRAINT CHK_latitude_city;
ALTER TABLE city DISABLE CONSTRAINT CHK_longitude_city;
ALTER TABLE citylocalname DISABLE CONSTRAINT fk_city_citylocalname;
ALTER TABLE cityothername DISABLE CONSTRAINT fk_city_cityothername;
ALTER TABLE citypopulations DISABLE CONSTRAINT fk_city_citypopulations;
ALTER TABLE country_other_localname DISABLE CONSTRAINT fk_country_countryotherlocalname;
ALTER TABLE countrypopulations DISABLE CONSTRAINT fk_country_countrypopulations;
ALTER TABLE economy DISABLE CONSTRAINT fk_country_economy;
ALTER TABLE economy DISABLE CONSTRAINT CHK_agriculture;
ALTER TABLE economy DISABLE CONSTRAINT CHK_service;
ALTER TABLE economy DISABLE CONSTRAINT CHK_industry;
ALTER TABLE economy DISABLE CONSTRAINT CHK_unemployment;
ALTER TABLE ethnicgroup DISABLE CONSTRAINT fk_country_ethnicgroup;
ALTER TABLE ethnicgroup DISABLE CONSTRAINT CHK_ethnic_group_percentage;
ALTER TABLE ismember DISABLE CONSTRAINT fk_organization_ismember;
ALTER TABLE ismember DISABLE CONSTRAINT fk_country_ismember;
ALTER TABLE language DISABLE CONSTRAINT fk_country_language;
ALTER TABLE language DISABLE CONSTRAINT CHK_percentage;
ALTER TABLE island DISABLE CONSTRAINT fk_city_island;
ALTER TABLE organization DISABLE CONSTRAINT fk_city_organization;
ALTER TABLE politics DISABLE CONSTRAINT fk_country_politics;
ALTER TABLE politics DISABLE CONSTRAINT fk_dependent_politics;
ALTER TABLE population DISABLE CONSTRAINT fk_country_population;
ALTER TABLE province DISABLE CONSTRAINT fk_province_province;
ALTER TABLE province DISABLE CONSTRAINT fk_country_province;
ALTER TABLE provincelocalname DISABLE CONSTRAINT fk_province_provincelocalname;
ALTER TABLE provinceothername DISABLE CONSTRAINT fk_province_provinceothername;
ALTER TABLE provincepopulation DISABLE CONSTRAINT fk_province_provincepopulation;
ALTER TABLE religion DISABLE CONSTRAINT fk_country_religion;
ALTER TABLE religion DISABLE CONSTRAINT CHK_percentage_religion;
ALTER TABLE continent DISABLE CONSTRAINT fk_countrycode_continent;
ALTER TABLE continent DISABLE CONSTRAINT CHK_encompass_percentage;
