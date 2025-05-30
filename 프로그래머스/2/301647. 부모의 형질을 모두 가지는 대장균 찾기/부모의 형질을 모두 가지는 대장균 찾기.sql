SELECT C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA C
INNER JOIN ECOLI_DATA P ON P.ID=C.PARENT_ID 
WHERE P.GENOTYPE & C.GENOTYPE = P.GENOTYPE
ORDER BY C.ID