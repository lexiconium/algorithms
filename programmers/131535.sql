select
    count(USER_ID) as USERS
from
    USER_INFO
where
    JOINED like '2021-%'
    and AGE between 20 and 29