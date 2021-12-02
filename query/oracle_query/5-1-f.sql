SELECT c.name, gdp, inflation
FROM economy, country c
WHERE gdp > 0
    AND c.code = economy.country
ORDER BY gdp DESC
FETCH FIRST 10 ROWS ONLY