-- This script is used to temporay delete the latest records entered into the database


SET @latestkplc = (SELECT max(id) FROM kplcreading);
SET @latestkiwasco = (SELECT max(id) FROM kiwascoreading);

SELECT * FROM kplcreading
WHERE id  = @latestkplc AND DATE(entry_date) = CURDATE();

SELECT * FROM kiwascoreading
WHERE id  = @latestkiwasco AND DATE(entry_date) = CURDATE();

-- Uncomment this block of code the run

/*
DELETE FROM kplcreading
WHERE id  = @latestkplc AND DATE(entry_date) = CURDATE();

DELETE FROM kiwascoreading
WHERE id  = @latestkiwasco AND DATE(entry_date) = CURDATE();


*/