select
    i.REST_ID,
    i.REST_NAME,
    i.FOOD_TYPE,
    i.FAVORITES,
    i.ADDRESS,
    pr.SCORE
from
    REST_INFO as i
    join (
        select
            r.REST_ID,
            round(avg(r.REVIEW_SCORE), 2) as SCORE
        from
            REST_REVIEW as r
        group by
            r.REST_ID
    ) as pr on i.REST_ID = pr.REST_ID
where
    i.ADDRESS like '서울%'
order by
    pr.SCORE desc,
    i.FAVORITES desc;