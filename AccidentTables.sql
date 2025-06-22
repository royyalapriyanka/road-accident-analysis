CREATE DATABASE AccidentTables;
USE AccidentTables;
CREATE TABLE accidents (
  accident_id INT AUTO_INCREMENT PRIMARY KEY,
  accident_date DATE,
  accident_time TIME,
  location VARCHAR(100),
  cause VARCHAR(100),
  severity ENUM('Minor', 'Major', 'Fatal')
);
