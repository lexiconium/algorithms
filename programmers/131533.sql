SELECT
    p.PRODUCT_CODE,
    SUM(p.PRICE * s.SALES_AMOUNT) AS SALES
FROM
    PRODUCT AS p
    JOIN OFFLINE_SALE AS s ON p.PRODUCT_ID = s.PRODUCT_ID
GROUP BY
    p.PRODUCT_CODE
ORDER BY
    SALES DESC,
    p.PRODUCT_CODE