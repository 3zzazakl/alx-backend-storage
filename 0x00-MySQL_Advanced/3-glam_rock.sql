-- glam rock
SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE style = 'glam rock'
ORDER BY lifespan DESC;
