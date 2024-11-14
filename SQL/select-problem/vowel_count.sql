-- # write your SQL statement here: you are given a table 'getcount' with column 'str', return a table with column 'str' and your result in a column named 'res'.

-- 1
SELECT str, LENGTH(str) - LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(str, 'a', ''), 'e', ''), 'i', ''), 'o', ''), 'u', '')) AS res
FROM getcount;

-- 2
SELECT str, LENGTH(REGEXP_REPLACE(str, '[^aeiou]', '', 'g')) AS res
FROM getcount
