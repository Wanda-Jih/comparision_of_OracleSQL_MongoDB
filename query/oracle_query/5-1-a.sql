SELECT name
FROM
    (
        SELECT
            name,
            SUM(length) AS total_length
        FROM
            (
                SELECT
                    name,
                    length
                FROM country
                    JOIN borders ON code = country1
                UNION ALL
                SELECT
                    name,
                    length
                FROM country
                    JOIN borders ON code = country2
            )
        GROUP BY name
        ORDER BY total_length DESC
    )
FETCH NEXT 1 ROWS ONLY;
