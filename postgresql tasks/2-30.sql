AS SELECT
       CONCAT_WS(' ', first_name, last_name) AS "full name",
       department_id,
       CONCAT_WS(' ', number, street) AS "address"
FROM
    employees AS e,
    addresses AS a
WHERE
    e.address_id = a.id
ORDER BY
    address;