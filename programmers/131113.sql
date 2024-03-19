SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT (OUT_DATE, '%Y-%m-%d') OUT_DATE,
    CASE
        WHEN OUT_DATE IS NULL THEN '출고미정'
        WHEN OUT_DATE < '2022-05-02' THEN '출고완료'
        ELSE '출고대기'
    END "출고여부"
FROM
    FOOD_ORDER
ORDER BY
    ORDER_ID;