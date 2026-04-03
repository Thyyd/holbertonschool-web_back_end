-- Creates a view that will list all students that have a score under 80 AND either no last_meeting date or a last_meeting older than 1 month

-- Create the view that will list the students with a score below 80 AND either no last_meeting date or a last_meeting older than 1 month
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 AND (last_meeting IS NULL OR last_meeting < NOW() - INTERVAL 1 MONTH)