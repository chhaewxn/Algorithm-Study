-- 만원 단위 가격대별 상품 개수 조회
SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS 
FROM PRODUCT 
GROUP BY FLOOR(PRICE / 10000) * 10000 
ORDER BY PRICE_GROUP 