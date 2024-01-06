SELECT
    CONCAT_WS(' ', mountain_range, peak_name) AS "Mountain Information",
    LENGTH(CONCAT_WS(' ', mountain_range, peak_name)) AS "Characters Length",
    BIT_LENGTH(CONCAT_WS(' ', mountain_range, peak_name)) AS "Bits of a String"
FROM
    mountains AS m,
    peaks AS p
WHERE
    m.id = p.mountain_id;