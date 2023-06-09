CREATE TABLE PastAppointments (
  appointment_id UUID,
  doctor_id UUID,
  patient_id UUID,
  type INT,
  date TIMESTAMP(0)
);

CREATE TABLE FutureAppointments (
  appointment_id UUID,
  doctor_id UUID,
  patient_id UUID,
  type INT,
  date TIMESTAMP(0)
);

INSERT INTO PastAppointments (appointment_id, doctor_id, patient_id, type, date)
VALUES
    ('4b3c9d5e-1b9e-4c24-af6d-6f9bdc8dbcc6', '4aebdbe2-8a82-4e96-9760-7e8e0d3f79e0', 'c3d6c8a4-68d5-4eab-963c-257df866a0d4', 1, '2023-05-10 10:30:00'),
    ('e57d5e96-7124-4a7f-89c1-1660f2d3c26e', 'a34e21f9-93fd-4e4c-9c3f-fb6c64f28b25', 'e7d9c0b8-71c5-4e3e-9f81-9f038011d4b0', 2, '2023-05-12 14:45:00'),
    ('f34e4faa-8f77-44d5-a344-82a2fd4c32f7', '68e4bcf5-82fb-47d2-9c28-58d751f1085d', 'fd4db558-1e10-4a9e-912f-7e4b9db14de7', 3, '2023-04-20 08:15:00'),
    ('b641ba0f-46c4-4d9a-b67a-eeb28d5452d9', '4aebdbe2-8a82-4e96-9760-7e8e0d3f79e0', 'e7d9c0b8-71c5-4e3e-9f81-9f038011d4b0', 3, '2023-05-12 13:45:00');

INSERT INTO FutureAppointments (appointment_id, doctor_id, patient_id, type, date)
VALUES
    ('a0869c06-6a85-482e-b93a-6be9a5f16c7a', '4aebdbe2-8a82-4e96-9760-7e8e0d3f79e0', 'c3d6c8a4-68d5-4eab-963c-257df866a0d4', 1, '2023-05-19 19:00:00'),
    ('35c2e0ff-30d3-4e0a-88f4-79f68c377d86', 'a34e21f9-93fd-4e4c-9c3f-fb6c64f28b25', 'e7d9c0b8-71c5-4e3e-9f81-9f038011d4b0', 2, '2023-05-20 11:45:00'),
    ('4afdd1f9-ced1-4a8a-b614-6a8edfc21b32', '68e4bcf5-82fb-47d2-9c28-58d751f1085d', 'fd4db558-1e10-4a9e-912f-7e4b9db14de7', 3, '2023-06-22 14:00:00'),
    ('8a3d1c9e-6d32-4d21-b3c2-9f3b774a8b03', 'a34e21f9-93fd-4e4c-9c3f-fb6c64f28b25', 'fd4db558-1e10-4a9e-912f-7e4b9db14de7', 1, '2023-06-20 16:30:00')