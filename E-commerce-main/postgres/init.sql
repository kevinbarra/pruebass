CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    id_role INTEGER,
    name VARCHAR(50),
    lastname VARCHAR(50),
    email VARCHAR(100),
    password VARCHAR(128),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    is_banned BOOLEAN,
    
    FOREIGN KEY (id_role) REFERENCES roles(id)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    id_user VARCHAR(50),
    price FLOAT,
    created_at TIMESTAMP
);

CREATE TABLE orders_products (
    id_order INTEGER,
    id_product VARCHAR(50),
    quantity INTEGER,

    FOREIGN KEY (id_order) REFERENCES orders(id)
);

INSERT INTO roles (name) VALUES
('user'),
('admin');