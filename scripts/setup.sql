CREATE DATABASE iot;
USE iot;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20),
    passhash VARCHAR(20),
    registered TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    primary key (id, username)
);

INSERT INTO `users` (`username`, `passhash`) VALUES ("admin", "1234");
