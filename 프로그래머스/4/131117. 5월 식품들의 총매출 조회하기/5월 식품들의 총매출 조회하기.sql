-- 2022년 5월 생산 식품의 총매출을 계산하는 MySQL/MariaDB 쿼리
-- FOOD_PRODUCT와 FOOD_ORDER 테이블 조인
-- 생산일자는 2022년 5월로 필터링
-- 각 식품별 총매출(가격 * 주문량) 계산 후 집계
-- 총매출 내림차순, 식품 ID 오름차순 정렬
SELECT 
    FP.PRODUCT_ID,
    FP.PRODUCT_NAME,
    SUM(FP.PRICE * FO.AMOUNT) AS TOTAL_SALES
FROM 
    FOOD_PRODUCT FP
JOIN 
    FOOD_ORDER FO ON FP.PRODUCT_ID = FO.PRODUCT_ID
WHERE 
    FO.PRODUCE_DATE BETWEEN '2022-05-01' AND '2022-05-31'
GROUP BY 
    FP.PRODUCT_ID, FP.PRODUCT_NAME
ORDER BY 
    TOTAL_SALES DESC, FP.PRODUCT_ID ASC;