WITH
    USER_CONDITION AS (
        SELECT
            WRITER_ID
        FROM
            USED_GOODS_BOARD
        GROUP BY
            WRITER_ID
        HAVING
            COUNT(*) >= 3
    )
SELECT
    USER_ID,
    NICKNAME,
    CONCAT (CITY, " ", STREET_ADDRESS1, " ", STREET_ADDRESS2) "전체주소",
    CONCAT (
        SUBSTRING(TLNO, 1, 3),
        '-',
        SUBSTRING(TLNO, 4, 4),
        '-',
        SUBSTRING(TLNO, 8)
    ) "전화번호"
FROM
    USED_GOODS_USER u
    JOIN USER_CONDITION c ON u.USER_ID = c.WRITER_ID
ORDER BY
    u.USER_ID DESC;