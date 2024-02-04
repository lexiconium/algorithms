WITH
    MAX_PRICE_PER_CATEGORY AS (
        SELECT
            CATEGORY,
            MAX(PRICE) MAX_PRICE
        FROM
            FOOD_PRODUCT
        WHERE
            CATEGORY IN ('과자', '국', '김치', '식용유')
        GROUP BY
            CATEGORY
    )
SELECT
    f.CATEGORY,
    f.PRICE MAX_PRICE,
    f.PRODUCT_NAME
FROM
    FOOD_PRODUCT f
    JOIN MAX_PRICE_PER_CATEGORY c ON f.CATEGORY = c.CATEGORY
    AND f.PRICE = c.MAX_PRICE
ORDER BY
    f.PRICE DESC;