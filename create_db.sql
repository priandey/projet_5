DROP USER IF EXISTS off_admin;
CREATE USER 'off_admin'@'%' IDENTIFIED BY 'goodfood';
ALTER USER 'off_admin'@'%' IDENTIFIED WITH mysql_native_password BY 'goodfood';


DROP DATABASE IF EXISTS OpenFoodFacts;

CREATE DATABASE OpenFoodFacts CHARACTER SET 'utf8';

USE OpenFoodFacts;

GRANT ALL ON OpenFoodFacts.* TO 'off_admin'@'%';

CREATE TABLE product (
  product_name VARCHAR(150) NOT NULL,
  nutrition_grade CHAR(1) NOT NULL,
  product_url VARCHAR(250) NOT NULL PRIMARY KEY,
  store VARCHAR(120) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE category (
  category_name VARCHAR(100) NOT NULL PRIMARY KEY
) ENGINE=InnoDB;

CREATE TABLE product_category(
  product_url VARCHAR(250) NOT NULL,
  category_name VARCHAR(100) NOT NULL,
  CONSTRAINT fk_product
    FOREIGN KEY (product_url)
    REFERENCES product(product_url),
  CONSTRAINT fk_category
    FOREIGN KEY (category_name)
    REFERENCES category(category_name)
) ENGINE=InnoDB;

CREATE TABLE user_history(
  search_id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  selected_product VARCHAR(250) NOT NULL,
  substitute VARCHAR(250) NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_product_searched
    FOREIGN KEY (selected_product)
    REFERENCES product(product_url),
  CONSTRAINT fk_product_found
    FOREIGN KEY (substitute)
    REFERENCES product(product_url)
) ENGINE=InnoDB;
