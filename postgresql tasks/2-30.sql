CREATE VIEW view_addresses
AS SELECT
       CONCAT_WS(' ', e.first_name, e.last_name) AS "Full name",
       e.department_id,
       CONCAT_WS(' ', a.number, a.street) AS "Address"
FROM
    employees AS e
JOIN
    addresses AS a
        ON
    e.address_id = a.id
ORDER BY
    "Address";