SELECT city.country, city.name
FROM (
    SELECT country, MAX(population) AS maxP
    FROM city
    GROUP BY country
) cp, city
WHERE city.country = cp.country
    AND city.population = cp.maxP;

