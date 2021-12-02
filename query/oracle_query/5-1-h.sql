SELECT COUNT(e.country)/100
FROM
    (
        SELECT country
        FROM economy
        WHERE gdp > 0
        ORDER BY gdp DESC
        FETCH FIRST 100 ROWS ONLY
    ) e,
    (
        SELECT country
        FROM ismember
        WHERE organization = 'C'    
    ) m
WHERE m.country = e.country

