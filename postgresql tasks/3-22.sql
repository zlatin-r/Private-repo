SELECT
    population,
    LENGTH(population::VARCHAR) -- LENGTH(CAST(population AS VARCHAR)) AS "length"
FROM
    countries
