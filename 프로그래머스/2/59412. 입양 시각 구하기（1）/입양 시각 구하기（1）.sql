-- 09:00부터 19:59까지 각 시간대별 입양 건수 조회
SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) BETWEEN 9 AND 19 
GROUP BY HOUR(DATETIME)
ORDER BY HOUR 