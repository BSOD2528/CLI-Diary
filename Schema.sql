-- Database: Diary
-- DROP DATABASE IF EXISTS "Diary";

CREATE DATABASE "Diary"
    WITH 
    OWNER = "AV"
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_India.1252'
    LC_CTYPE = 'English_India.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "Diary"
    IS 'CLI Diary Database';