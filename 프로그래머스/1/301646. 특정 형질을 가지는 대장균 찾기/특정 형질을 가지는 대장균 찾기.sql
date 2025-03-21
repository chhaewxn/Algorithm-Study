-- 2번 형질이 없고 1번이나 3번 형질이 있는 대장균 개체 수 계산
SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0   -- 2번 형질을 보유하지 않음 (2번 비트가 0)
  AND ((GENOTYPE & 1) > 0 OR (GENOTYPE & 4) > 0)  -- 1번 형질(1) 또는 3번 형질(4)을 보유