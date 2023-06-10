CREATE TABLE users (
    user_id UUID,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    firstname VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    birthdate DATE,
    is_doctor BOOLEAN DEFAULT FALSE,
    notification BOOLEAN DEFAULT TRUE,
    doctor_phd INT DEFAULT NULL,
    doctor_specialization VARCHAR(100) DEFAULT NULL
);

INSERT INTO users (user_id, email, password_hash, firstname, surname, phone, birthdate, is_doctor, notification)
VALUES
    ('4aebdbe2-8a82-4e96-9760-7e8e0d3f79e0', 'vlprotsenko333@gmail.com', 'superhash', 'Max', 'Verstappen', '12345', '1984-05-10', True, True),
    ('b0869c06-6a85-482e-b93a-6be9a5f16c7a', 'vlpsenko333@gmail.com', 'superhash', 'Max', 'Verstappen', '12345', '1954-05-10', True, False);
