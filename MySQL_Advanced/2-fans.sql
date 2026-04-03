-- Orders a table by the number of fans, in descend order

-- Orders the table by the number of fans, in descend order
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC