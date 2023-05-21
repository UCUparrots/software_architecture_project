CREATE TABLE users (
    user_id UUID,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    firstname VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    birthdate DATE,
    is_doctor BOOLEAN DEFAULT FALSE,
    notification BOOLEAN DEFAULT FALSE,
    doctor_phd INT DEFAULT NULL,
    doctor_specialization VARCHAR(100) DEFAULT NULL
);
