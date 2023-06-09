# software_architecture_project

to start:  
`docker-compose up --build`  
in the project root.  
Example:  
 - curl -X POST -H "Content-Type: application/json" -d '{"email": "shevdan007@gmail.com", "password_hash": "1", "firstname": "s", "lastname": "b", "phone": "+380931428816", "birthdate": "2023-07-02", "is_doctor": "False", "notification": "True"}' http://localhost:8080/signup
 - curl -X POST -H "Content-Type: application/json" -d '{"user_id": "YOUR_USER_ID", "email": "newshevdan007@gmail.com", "phone": "+38000000000", "birthdate": "2023-07-02", "is_doctor": "True", "doctor_phd": "123", "doctor_specialization": "Doc"}' http://localhost:8080/update_info
 - curl -X POST -H "Content-Type: application/json" -d '{"email": "newshevdan007@gmail.com", "password_hash": "1", "login_as_doctor": "False"}' http://localhost:8080/login
 - curl -X GET -H "Content-Type: application/json" -d '{"user_id": "8901ceee-7b4f-4ae1-9b91-0f20d33b2efa"}' http://localhost:8080/get_info
