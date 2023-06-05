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

INSERT INTO users (user_id, email, password_hash, firstname, surname, phone, birthdate, is_doctor, notification)
VALUES
    ('fe150f8b-3866-4544-8921-d70dde8596e0', 'vlprotsenko333@gmail.com', 'superhash', 'Max', 'Verstappen', '12345', '1984-05-10', True, True);
    ('c3083920-af10-4f27-8814-7486ab1ad590', 'vlpsenko333@gmail.com', 'superhash', 'Max', 'Verstappen', '12345', '1954-05-10', True, False);
