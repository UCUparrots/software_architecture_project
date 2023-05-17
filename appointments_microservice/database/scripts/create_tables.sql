CREATE TABLE PastAppointments (
  appointment_id SERIAL PRIMARY KEY,
  doctor_id UUID,
  patient_id UUID,
  type VARCHAR(255),
  date DATE
);

CREATE TABLE FutureAppointments (
  appointment_id SERIAL PRIMARY KEY,
  doctor_id UUID,
  patient_id UUID,
  type VARCHAR(255),
  date DATE
);