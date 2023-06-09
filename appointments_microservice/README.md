# software_architecture_project
to start:  
`docker-compose up --build`  
in the project root.  
Example:  
 - curl -X GET -H 'Content-Type: application/json' -d '{"id": "35c2e0ff-30d3-4e0a-88f4-79f68c377d86", "doctor": "a34e21f9-93fd-4e4c-9c3f-fb6c64f28b25", "patient": "e7d9c0b8-71c5-4e3e-9f81-9f038011d4b0", "type": 2, "date": "2023-05-20 11:45:00"}' http://localhost:8085/get_appointments
 - curl -X GET -H 'Content-Type: application/json' -d '{"type": 1}' http://localhost:8085/get_past_appointments
 - curl -X GET -H 'Content-Type: application/json' -d '{"type": 1}' http://localhost:8085/get_future_appointments
 - curl -X POST -H 'Content-Type: application/json' -d '{"doctor": "fe150f8b-3866-4544-8921-d70dde8596e0", "patient": "c3083920-af10-4f27-8814-7486ab1ad590", "date": "2023-07-02 12:15:00", "type": 1}' http://localhost:8085/new_appointment
 - curl -X POST -H 'Content-Type: application/json' -d '{"appointment_id": "35c2e0ff-30d3-4e0a-88f4-79f68c377d86"}' http://localhost:8085/delete_appointment
 - curl -X POST -H 'Content-Type: application/json' -d '{"appointment_id": "35c2e0ff-30d3-4e0a-88f4-79f68c377d86"}' http://localhost:8085/confirm_appointment