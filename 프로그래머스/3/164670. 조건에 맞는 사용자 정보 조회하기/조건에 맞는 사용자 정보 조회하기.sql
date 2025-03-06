-- 코드를 입력하세요
SELECT 
    u.USER_ID, 
    u.NICKNAME, 
    CONCAT(u.CITY, ' ', u.STREET_ADDRESS1, ' ', IFNULL(u.STREET_ADDRESS2, '')) AS 전체주소,
    CONCAT(
        SUBSTRING(u.TLNO, 1, 3), '-',
        SUBSTRING(u.TLNO, 4, 4), '-',
        SUBSTRING(u.TLNO, 8, 4)
    ) AS 전화번호
FROM 
    USED_GOODS_USER u
JOIN (
    SELECT 
        WRITER_ID
    FROM 
        USED_GOODS_BOARD
    GROUP BY 
        WRITER_ID
    HAVING 
        COUNT(*) >= 3
) b ON u.USER_ID = b.WRITER_ID
ORDER BY 
    u.USER_ID DESC;