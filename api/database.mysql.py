CREATE DATABASE school_api CHARACTER SET utf8mb4;
USE school_api;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age >= 0),
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO students (prenom, age) VALUES
('Arthur', 22),
('Lyes', 23),
('Hassan', 21),
('Jacques', 23)