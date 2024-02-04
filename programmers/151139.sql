WITH
    TOTAL_RECORDS AS (
        SELECT
            MONTH (START_DATE) MONTH,
            CAR_ID,
            COUNT(CAR_ID) RECORDS
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY
            MONTH (START_DATE),
            CAR_ID
    ),
    CONDITIONED_CAR_IDS AS (
        SELECT
            CAR_ID
        FROM
            TOTAL_RECORDS
        GROUP BY
            CAR_ID
        HAVING
            SUM(RECORDS) >= 5
    )
SELECT
    tr.MONTH,
    tr.CAR_ID,
    tr.RECORDS
FROM
    TOTAL_RECORDS tr
    JOIN CONDITIONED_CAR_IDS cid ON tr.CAR_ID = cid.CAR_ID
ORDER BY
    tr.MONTH,
    tr.CAR_ID DESC;