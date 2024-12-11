-- fans
SELECT 
    TRIM(origin) AS origin, 
    SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY TRIM(origin)
ORDER BY nb_fans DESC;
