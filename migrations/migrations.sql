CREATE DATABASE bntu_checkout;

USE bntu_checkout;

CREATE TABLE checkout(
    customer_account VARCHAR(255),
    date_ VARCHAR(255),
    customer_number VARCHAR(255),
    university_account VARCHAR(255),
    student_name VARCHAR(255),
    operation_number VARCHAR(255),
    sum_ VARCHAR(255)
) DEFAULT CHARSET=utf8;