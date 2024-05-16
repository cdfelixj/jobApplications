UPDATE Product
SET tags = REPLACE(tags, 'open', 'close')
WHERE tags LIKE '%open%';
