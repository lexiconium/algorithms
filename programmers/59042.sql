SELECT
    o.ANIMAL_ID,
    o.NAME
FROM
    ANIMAL_OUTS o
    LEFT JOIN ANIMAL_INS i ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE
    i.ANIMAL_ID IS NULL
    -- 
SELECT
    o.ANIMAL_ID,
    o.NAME
FROM
    ANIMAL_OUTS o
WHERE
    NOT EXISTS (
        SELECT
            1
        FROM
            ANIMAL_INS i
        WHERE
            o.ANIMAL_ID = i.ANIMAL_ID
    )
ORDER BY
    o.ANIMAL_ID;