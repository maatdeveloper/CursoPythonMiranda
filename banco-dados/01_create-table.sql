CREATE TABLE world.users (
	id int UNSIGNED AUTO_INCREMENT NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email varchar(255) NOT NULL,
    password_hash varchar(255) NOT NULL,
    CONSTRAINT users_pk PRIMARY KEY (id),
    CONSTRAINT users_un_email UNIQUE KEY (email),
    CONSTRAINT users_un_password_hash UNIQUE KEY (password_hash)
)
DEFAULT CHARSET=utf8mb4;