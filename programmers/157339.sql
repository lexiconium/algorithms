WITH
    SEDAN_OR_SUV AS (
        SELECT
            CAR_ID,
            CAR_TYPE,
            DAILY_FEE
        FROM
            CAR_RENTAL_COMPANY_CAR
        WHERE
            CAR_TYPE IN ('세단', 'SUV')
    ),
    AVAILABLE_CARS AS (
        SELECT
            c.CAR_ID
        FROM
            SEDAN_OR_SUV c
        WHERE
            NOT EXISTS (
                SELECT
                    1
                FROM
                    CAR_RENTAL_COMPANY_RENTAL_HISTORY h
                WHERE
                    h.CAR_ID = c.CAR_ID
                    AND NOT (
                        h.END_DATE < '2022-11-01'
                        OR h.START_DATE > '2022-11-30'
                    )
            )
    ),
    DISCOUNTED_FEES AS (
        SELECT
            c.CAR_ID,
            c.CAR_TYPE,
            ROUND(30 * c.DAILY_FEE * (1 - p.DISCOUNT_RATE / 100)) FEE
        FROM
            SEDAN_OR_SUV c
            JOIN AVAILABLE_CARS a ON c.CAR_ID = a.CAR_ID
            LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON c.CAR_TYPE = p.CAR_TYPE
            AND p.DURATION_TYPE = '30일 이상'
    )
SELECT
    CAR_ID,
    CAR_TYPE,
    FEE
FROM
    DISCOUNTED_FEES
WHERE
    FEE >= 500000
    AND FEE < 2000000
ORDER BY
    FEE DESC,
    CAR_TYPE,
    CAR_ID DESC;