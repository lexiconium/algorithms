SELECT
    HOUR (DATETIME) HOUR,
    COUNT(*) COUNT
FROM
    ANIMAL_OUTS
WHERE
    HOUR (DATETIME) BETWEEN 9 AND 19
GROUP BY
    HOUR
ORDER BY
    HOUR;