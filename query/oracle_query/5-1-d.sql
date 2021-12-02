SELECT country.name, num_ethnic_group, max_ethnic_group_percentage
FROM 
    (
        SELECT DISTINCT ethnicgroup.country_code, ep.num_ethnic_group, eg.max_ethnic_group_percentage
        FROM 
            (
            SELECT country_code, COUNT(ethnic_group_name) as num_ethnic_group
            FROM ethnicgroup
            GROUP BY country_code    
            ) ep,
            (
            SELECT country_code, MAX(ethnic_group_percentage) as max_ethnic_group_percentage
            FROM ethnicgroup
            GROUP BY country_code  
            ) eg, ethnicgroup
        WHERE ethnicgroup.country_code = ep.country_code
            AND ethnicgroup.country_code = eg.country_code
        ORDER BY num_ethnic_group DESC    
    ) e, country
WHERE e.country_code = country.code
ORDER BY num_ethnic_group DESC   

    