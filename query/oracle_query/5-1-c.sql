SELECT country.name, gdp, agriculture, inflation
FROM 
    (
        SELECT country, gdp, agriculture, inflation
        FROM economy
        WHERE agriculture > service
            AND agriculture > industry
            OR agriculture > 50
    ) e, country
WHERE country.code = e.country

