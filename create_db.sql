DROP DATABASE IF EXISTS OpenFoodFacts;

CREATE DATABASE OpenFoodFacts CHARACTER SET 'utf8';

USE OpenFoodFacts;

CREATE TABLE product (
  product_id int UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_name varchar(150) NOT NULL,
  nutrition_grade char(1) NOT NULL,
  product_url varchar(150) NOT NULL,
  product_category varchar(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE category (
  category_name varchar(100) NOT NULL PRIMARY KEY
) ENGINE=InnoDB;

CREATE TABLE product_category(
  product_id int UNSIGNED NOT NULL,
  category_name varchar(100) NOT NULL,
  CONSTRAINT fk_product
    FOREIGN KEY (product_id)
    REFERENCES product(product_id),
  CONSTRAINT fk_category
    FOREIGN KEY (category_name)
    REFERENCES category(category_name)
) ENGINE=InnoDB;

CREATE TABLE user_history(
  search_id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_searched INT UNSIGNED NOT NULL,
  product_found INT UNSIGNED NOT NULL,
  search_date DATETIME NOT NULL,
  CONSTRAINT fk_product_searched
    FOREIGN KEY (product_searched)
    REFERENCES product(product_id),
  CONSTRAINT fk_product_found
    FOREIGN KEY (product_found)
    REFERENCES product(product_id)
) ENGINE=InnoDB;
