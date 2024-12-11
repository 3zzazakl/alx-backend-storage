-- fans
SELECT 
    TRIM(origin) AS origin, 
    SUM(fans) AS fans
FROM metal_bands
GROUP BY TRIM(origin)
ORDER BY fans DESC;
