SELECT
    h.HISTORY_ID,
    ROUND(
        CASE
            WHEN DATEDIFF (h.END_DATE, h.START_DATE) + 1 >= 7 THEN c.DAILY_FEE * (DATEDIFF (h.END_DATE, h.START_DATE) + 1) * (1 - p.DISCOUNT_RATE / 100)
            ELSE c.DAILY_FEE * (DATEDIFF (h.END_DATE, h.START_DATE) + 1)
        END
    ) FEE
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY h
    JOIN CAR_RENTAL_COMPANY_CAR c ON h.CAR_ID = c.CAR_ID
    LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON c.CAR_TYPE = p.CAR_TYPE
    AND (
        (
            (
                DATEDIFF (h.END_DATE, h.START_DATE) + 1 BETWEEN 7 AND 29
            )
            AND p.DURATION_TYPE = '7일 이상'
        )
        OR (
            (
                DATEDIFF (h.END_DATE, h.START_DATE) + 1 BETWEEN 30 AND 89
            )
            AND p.DURATION_TYPE = '30일 이상'
        )
        OR (
            DATEDIFF (h.END_DATE, h.START_DATE) + 1 >= 90
            AND p.DURATION_TYPE = '90일 이상'
        )
    )
WHERE
    c.CAR_TYPE = '트럭'
ORDER BY
    FEE DESC,
    h.HISTORY_ID DESC;