SELECT
    r.FOOD_TYPE,
    r.REST_ID,
    r.REST_NAME,
    r.FAVORITES
FROM
    REST_INFO r
    JOIN (
        SELECT
            FOOD_TYPE,
            MAX(FAVORITES) FAVORITES
        FROM
            REST_INFO
        GROUP BY
            FOOD_TYPE
    ) t ON r.FOOD_TYPE = t.FOOD_TYPE
    AND r.FAVORITES = t.FAVORITES
ORDER BY
    r.FOOD_TYPE DESC;