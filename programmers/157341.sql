WITH
    SEDAN AS (
        SELECT DISTINCT
            CAR_ID
        FROM
            CAR_RENTAL_COMPANY_CAR
        WHERE
            CAR_TYPE = '세단'
    ),
    OCT_RENTED AS (
        SELECT DISTINCT
            CAR_ID
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            START_DATE LIKE '%-10-%'
    )
SELECT
    s.CAR_ID
FROM
    SEDAN s
    JOIN OCT_RENTED o ON s.CAR_ID = o.CAR_ID
ORDER BY
    s.CAR_ID DESC;