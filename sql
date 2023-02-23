CREATE DATABASE myusers;

USE myusers;

CREATE USER 'python'@'%' IDENTIFIED BY 'password';

#Grand all privileges to a user account on all databases:
GRANT ALL PRIVILEGES ON *.* TO 'python'@'%';


SHOW GRANTS FOR 'python'@'%';

CREATE TABLE users (
  id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  mobile_num VARCHAR(20) NOT NULL,
  email VARCHAR(100) NOT NULL
);



INSERT INTO users (first_name, last_name, mobile_num, email) VALUES ('John', 'Doe', '1234567890', 'johndoe@example.com');

SELECT * FROM users;
