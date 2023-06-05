CREATE TABLE DiagnosisHistory (
  patient_id UUID,
  doctor_id UUID,
  diagnosis_id UUID,
  diagnosis VARCHAR,
  start_date TIMESTAMP(0),
  notes VARCHAR,
  medicine VARCHAR,
  is_relevant INTEGER,
  resolved_date TIMESTAMP(0)
);


INSERT INTO DiagnosisHistory (patient_id, doctor_id, diagnosis_id, diagnosis, start_date, notes, medicine, is_relevant, resolved_date)
VALUES
    ('a44b56a7-7aa5-4b02-8b02-9a3f2f03a5d3', 'bce52e17-943f-4cfe-9630-f7c2f2a31047', '426e5d22-f2c6-4b92-8d27-1a8be2882407', 'diagnosis_1', '2023-05-20 10:00:00', 'notes_1', NULL, 1, '2023-05-21 12:00:00'),
    ('f8ef50d2-79fd-4cc4-9bb6-9408ce4dc7f2', 'd8e2d68e-20c1-4e0d-b52e-8209ab07b5c8', '9e4c2373-1dfb-4924-8fbf-6c52f7d38e68', 'diagnosis_2', '2023-05-22 14:30:00', 'notes_2', 'strepsils',  0, NULL),
    ('e9a3f4b0-46b7-4429-8f79-014a373a8cc3', '1d0d1f8b-68b6-4c89-9761-950db9a4a6a2', '60853c4b-9a37-4a95-b80e-7d6dbb4178a3', 'diagnosis_3', '2023-05-24 09:15:00', 'notes_3', NULL, 1, '2023-05-25 10:30:00');



CREATE TABLE UserTable (
  user_id UUID,
  email VARCHAR,
  name VARCHAR,
  surname VARCHAR,
  phone VARCHAR,
  birthdate TIMESTAMP(0),
  doctorPhD VARCHAR,
  doctor_specialization VARCHAR
);


INSERT INTO UserTable (user_id, email, name, surname, phone, birthdate, doctorPhD, doctor_specialization)
VALUES
  ('bce52e17-943f-4cfe-9630-f7c2f2a31047', 'john@example.com', 'John', 'Doe', '1234567890', '1990-01-01', 'PhD', 'Cardiology'),
  ('d8e2d68e-20c1-4e0d-b52e-8209ab07b5c8', 'jane@example.com', 'Jane', 'Smith', '9876543210', '1985-05-10', '', 'Pediatrics'),
  ('1d0d1f8b-68b6-4c89-9761-950db9a4a6a2', 'sam@example.com', 'Sam', 'Johnson', '5555555555', '1995-12-25', 'PhD', 'Dermatology'),
  ('a44b56a7-7aa5-4b02-8b02-9a3f2f03a5d3', 'john77@example.com', 'John', 'Doe', '1234567890', '1990-01-01', 'PhD', 'Cardiology'),
  ('f8ef50d2-79fd-4cc4-9bb6-9408ce4dc7f2', 'j7ane@example.com', 'Jane', 'Smith', '9876543210', '1985-05-10', '', 'Pediatrics'),
  ('e9a3f4b0-46b7-4429-8f79-014a373a8cc3', 'sam67@example.com', 'Sam', 'Johnson', '5555555555', '1995-12-25', 'PhD', 'Dermatology');
