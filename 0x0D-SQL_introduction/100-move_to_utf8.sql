-- Convert database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- This is to support More NON_ASCII set of characters
-- Change context to hbtn_0c_0 database
USE hbtn_0c_0;
-- Modify database hbtn_0c_0 to utf8
ALTER DATABASE hbtn_0c_0 CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Modify table first_table to utf8
ALTER TABLE first_table CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Modify Field name in first_table ot utf8
ALTER TABLE first_table
	MODIFY COLUMN name VARCHAR(256);
