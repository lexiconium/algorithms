select
    f.FACTORY_ID,
    f.FACTORY_NAME,
    f.ADDRESS
from
    FOOD_FACTORY f
where
    f.ADDRESS like '강원%'
order by
    f.FACTORY_ID