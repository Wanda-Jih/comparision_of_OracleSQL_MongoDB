SELECT country.name, count(country.name)
FROM country, airport
WHERE country.capital = airport.city
GROUP BY country.name
HAVING COUNT(country.name) > 1

