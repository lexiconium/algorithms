SELECT
    CONCAT (
        '/home/grep/src/',
        f.BOARD_ID,
        '/',
        f.FILE_ID,
        f.FILE_NAME,
        f.FILE_EXT
    ) FILE_PATH
FROM
    USED_GOODS_FILE f
WHERE
    f.BOARD_ID = (
        SELECT
            BOARD_ID
        FROM
            USED_GOODS_BOARD
        ORDER BY
            VIEWS DESC
        LIMIT
            1
    )
ORDER BY
    f.FILE_ID DESC;