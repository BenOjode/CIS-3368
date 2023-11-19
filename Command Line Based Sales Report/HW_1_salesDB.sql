show databases

create database sales

use sales

create table sales (
id int primary key auto_increment,
seller varchar(255) not null,
product varchar(255) not null,
quantity int,
price int
)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Homer","Donuts",12,2.00)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Bart","Skateboard",15,35.00)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Ben","Watch",10,650.00)

INSERT INTO sales (seller, product, quantity, price) VALUES
("LeBron","Shoes",200,220.00)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Kobe","Snakes",50,300.00)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Drake","CD",250,25)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Mike","Synthesizer",12,700)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Steve","Phone",1000,850)

INSERT INTO sales (seller, product, quantity, price) VALUES
("Bill","Computer",2000,1500)



