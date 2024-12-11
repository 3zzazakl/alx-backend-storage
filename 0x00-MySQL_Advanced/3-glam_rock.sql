-- glam rock
SELECT band_name, (IFNULL(split, 2022) - formed ) AS lifespan
FROM metal_bands
WHERE style like "%Glam rock%"
ORDER BY lifespan DESC;
