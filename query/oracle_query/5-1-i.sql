SELECT country.name, temp1.encompasses_continent, temp1.density
FROM
    (
        SELECT code, encompasses_continent, (population/area) AS density
        FROM country, continent
        WHERE country.code = continent.country_code    
    ) temp1,
    (
        SELECT encompasses_continent, MAX(density) AS density
        FROM 
            (
                SELECT code, encompasses_continent, (population/area) AS density
                FROM country, continent
                WHERE country.code = continent.country_code    
            )
        GROUP BY encompasses_continent    
    ) temp2, country
WHERE temp2.density = temp1.density
    AND country.code = temp1.code





