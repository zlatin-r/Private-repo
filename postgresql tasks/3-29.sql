SELECT
    latitude,
    ROUND(latitude, 2) AS round,
    trunc(latitude, 2) AS trunc
FROM
    apartments