SELECT COUNT(l.country)
FROM 
    (
        SELECT country_code, COUNT(ethnic_group_name) as num_ethnic
        FROM ethnicgroup
        GROUP BY country_code
    ) e,
    (
        SELECT country, COUNT(language) as num_language
        FROM language
        GROUP BY country
    ) l
WHERE l.country = e.country_code
    AND l.num_language = e.num_ethnic


