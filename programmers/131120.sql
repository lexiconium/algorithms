SELECT
    MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT (DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
FROM
    MEMBER_PROFILE
WHERE
    DATE_OF_BIRTH LIKE '____-03-__'
    AND GENDER = 'W'
    AND TLNO IS NOT NULL
ORDER BY
    MEMBER_ID;