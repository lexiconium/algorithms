WITH
    USER_JOINED_2021 AS (
        SELECT
            USER_ID
        FROM
            USER_INFO
        WHERE
            JOINED LIKE '2021-%'
    )
SELECT
    YEAR (s.SALES_DATE) YEAR,
    MONTH (s.SALES_DATE) MONTH,
    COUNT(DISTINCT u.USER_ID) PURCHASED_USERS,
    ROUND(
        COUNT(DISTINCT u.USER_ID) / (
            SELECT
                COUNT(*)
            FROM
                USER_JOINED_2021
        ),
        1
    ) PURCHASED_RATIO
FROM
    ONLINE_SALE s
    JOIN USER_JOINED_2021 u ON s.USER_ID = u.USER_ID
GROUP BY
    YEAR,
    MONTH
ORDER BY
    YEAR,
    MONTH;