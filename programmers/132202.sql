SELECT
    MCDP_CD `진료과 코드`,
    COUNT(*) `5월예약건수`
FROM
    APPOINTMENT
WHERE
    APNT_YMD LIKE '2022-05%'
GROUP BY
    MCDP_CD
ORDER BY
    `5월예약건수`,
    `진료과 코드`;