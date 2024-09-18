-- Rename an existing table from 'old_table_name' to 'new_table_name'
RENAME TABLE `old_table_name` TO `new_table_name`;

-- Rename a column in 'table_name' from 'old_column_name' to 'new_column_name'
ALTER TABLE table_name 
RENAME COLUMN `old_column_name` TO `new_column_name`;

-- Modify the data type of 'column_name' in 'table_name' to 'new_data_type'
ALTER TABLE table_name 
MODIFY column_name new_data_type;

-- Convert a date string in 'column_name' from the format '%d %m %y' to a DATE type
UPDATE table_name
SET column_name = STR_TO_DATE(column_name, '%d %m %y');

--remove suffixes using REGEXP_REPLACE to match 'st', 'nd','rd' or 'th' at the end of 'column_name'
UPDATE table_name
SET column_name = REGEXP_REPLACE(column_name, '(st|nd|rd|th)$', '');
