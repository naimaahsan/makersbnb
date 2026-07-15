DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    address TEXT NOT NULL,
    price_per_night DECIMAL,
    user_id INT,
    constraint fk_user foreign key(user_id) references users(id) on delete cascade -- Deletes user-associated-spaces when a user is deleted
);

CREATE TABLE bookings (
    space_id INT,
    user_id INT, -- this is the id of the user who booked it
    date DATE,
    constraint fk_spaceid foreign key(space_id) references spaces(id) on delete cascade,
    constraint fk_userid foreign key(user_id) references users(id) on delete cascade
);

INSERT INTO users (email, password) VALUES('user1@email.com', '$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu'); -- password1
INSERT INTO users (email, password) VALUES('user2@email.com', '$2b$10$Pzf69bH7oZk3yBbeFea1HuGUcrDb9A0Q2oN1PRQicmNsFjyIDrRMS'); -- p4ssword123
INSERT INTO users (email, password) VALUES('user3@email.com', '$2b$10$P0whtrX05RAam425JcGoxeAccsV1uAZGhquwiWDlXTlXpkUHmtnZy'); -- p00

INSERT INTO spaces (name, description, address, price_per_night, user_id) VALUES 
    ('Cool House', 'Small flat', '8 Fake Street, Faketown', 100.00, 1),
    ('My House', 'Large flat', '9 Fake Street, Faketown', 125.00, 1),
    ('Top House', 'Bungalow', '15 Fake Road, Faketown', 99.00, 2),
    ('Party House', 'Penthouse', '85 Fake Road, Faketown', 200.00, 3);

INSERT INTO bookings (space_id, user_id, date) VALUES
    (1, 2, '2026-01-01'),
    (1, 3, '2026-01-03'),
    (3, 2, '2026-01-07'),
    (3, 1, '2026-05-25'),
    (2, 1, '2026-05-25');
