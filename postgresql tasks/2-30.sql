CREATE VIEW view_addresses
AS SELECT
       CONCAT_WS(' ', first_name, last_name) AS "full name",
       department_id,
       CONCAT_WS(' ', number, street) AS "addresses"
FROM
    employees,
    addresses;