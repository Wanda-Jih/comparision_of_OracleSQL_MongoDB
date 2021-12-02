SELECT country.name, religion.name
FROM 
    (
        SELECT country, COUNT(name) AS num_religion
        FROM religion
        GROUP BY country
        HAVING COUNT(name) = (
            SELECT COUNT(name) AS num_religion
            FROM religion
            GROUP BY country
            ORDER BY num_religion DESC
            FETCH FIRST 1 ROWS ONLY    
            )  
    ) r, religion, country
WHERE r.country = religion.country
    AND country.code = religion.country
