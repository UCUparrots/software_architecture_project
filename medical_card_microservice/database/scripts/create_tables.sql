DROP TABLE DiagnosisHistory;

CREATE TABLE DiagnosisHistory (
  patient_id UUID,
  doctor_id UUID,
  diagnosis VARCHAR,
  start_date TIMESTAMP(0),
  notes VARCHAR,
  medicine VARCHAR,
  is_relevant INTEGER,
  resolved_date TIMESTAMP(0)
);


INSERT INTO DiagnosisHistory (patient_id, doctor_id, diagnosis, start_date, notes, medicine, is_relevant, resolved_date)
VALUES
    ('a44b56a7-7aa5-4b02-8b02-9a3f2f03a5d3', 'bce52e17-943f-4cfe-9630-f7c2f2a31047', 'diagnosis_1', '2023-05-20 10:00:00', 'notes_1', NULL, 1, '2023-05-21 12:00:00'),
    ('f8ef50d2-79fd-4cc4-9bb6-9408ce4dc7f2', 'd8e2d68e-20c1-4e0d-b52e-8209ab07b5c8', 'diagnosis_2', '2023-05-22 14:30:00', 'notes_2', 'strepsils',  0, NULL),
    ('e9a3f4b0-46b7-4429-8f79-014a373a8cc3', '1d0d1f8b-68b6-4c89-9761-950db9a4a6a2', 'diagnosis_3', '2023-05-24 09:15:00', 'notes_3', NULL, 1, '2023-05-25 10:30:00');



CREATE TABLE UserTable (
  user_id UUID,
  email VARCHAR,
  password_hash VARCHAR,
  name VARCHAR,
  surname VARCHAR,
  phone VARCHAR,
  birthdate TIMESTAMP(0),
  doctorPhD VARCHAR,
  doctor_specialization VARCHAR
);


INSERT INTO UserTable (user_id, email, password_hash, name, surname, phone, birthdate, doctorPhD, doctor_specialization)
VALUES
  ('bce52e17-943f-4cfe-9630-f7c2f2a31047', 'john@example.com', '5f4dcc3b5aa765d61d8327deb882cf99', 'John', 'Doe', '1234567890', '1990-01-01', 'PhD', 'Cardiology'),
  ('d8e2d68e-20c1-4e0d-b52e-8209ab07b5c8', 'jane@example.com', '5f4dcc3b5aa765d61d8327deb882cf99', 'Jane', 'Smith', '9876543210', '1985-05-10', '', 'Pediatrics'),
  ('1d0d1f8b-68b6-4c89-9761-950db9a4a6a2', 'sam@example.com', '5f4dcc3b5aa765d61d8327deb882cf99', 'Sam', 'Johnson', '5555555555', '1995-12-25', 'PhD', 'Dermatology'),
  ('a44b56a7-7aa5-4b02-8b02-9a3f2f03a5d3', 'john77@example.com', '5f4dcc3b5aa765d61d8327deb882cf99', 'John', 'Doe', '1234567890', '1990-01-01', 'PhD', 'Cardiology'),
  ('f8ef50d2-79fd-4cc4-9bb6-9408ce4dc7f2', 'j7ane@example.com', '5f4dcc3b5aa765d61d8327deb882cf99', 'Jane', 'Smith', '9876543210', '1985-05-10', '', 'Pediatrics'),
  ('e9a3f4b0-46b7-4429-8f79-014a373a8cc3', 'sam67@example.com', '5f4dcc3b5aa765d61d8327deb882cf99', 'Sam', 'Johnson', '5555555555', '1995-12-25', 'PhD', 'Dermatology');
