-- a script that prepares a MySQL server
-- Database: hbnb_dev_db
-- User: hbnb_dev
-- Password: hbnb_dev_pwd

-- Creating the Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating the User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting the privilages
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Granting select privilages
GRANT SELECT ON performance_schema.* 'hbnb_dev'@'localhost';

-- Applying changes
FLUSH PRIVILEGES;
