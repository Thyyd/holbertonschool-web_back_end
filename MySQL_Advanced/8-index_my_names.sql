-- Creates an index on the first letter of the name field of the table names

-- Create the index that will store only the first letter of name
CREATE INDEX idx_name_first
ON names (name(1));