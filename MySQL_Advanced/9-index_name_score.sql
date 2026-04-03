-- Creates an index on the first letter of the name field and the score of the table names

-- Create the index that will store only the first letter of name and the score
CREATE INDEX idx_name_first_score
ON names (name(1), score);