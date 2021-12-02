CREATE INMEMORY JOIN GROUP country_city_jg(
    country(code),
    city(country)
);

ALTER TABLE country INMEMORY;
ALTER TABLE city INMEMORY;

