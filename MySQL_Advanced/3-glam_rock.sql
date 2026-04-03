-- Orders a table of Glam Rock style by their lifespan, in descend order

-- Orders the table of Glam Rock style by their lifespan, in descend order
SELECT band_name, COALESCE(split, 2024) - formed AS lifespan  -- COALESCE renvoie le premier argument qui n'est pas NULL
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC