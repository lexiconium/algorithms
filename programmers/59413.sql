WITH RECURSIVE
    TIME_TABLE AS (
        SELECT
            0 HOUR
        UNION
        SELECT
            HOUR + 1
        FROM
            TIME_TABLE
        WHERE
            HOUR < 23
    )
SELECT
    tt.HOUR,
    COUNT(ao.ANIMAL_ID) COUNT
FROM
    TIME_TABLE tt
    LEFT JOIN ANIMAL_OUTS ao ON HOUR(ao.DATETIME) = tt.HOUR
GROUP BY
    tt.HOUR
ORDER BY
    tt.HOUR;