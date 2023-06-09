# software_architecture_project
to start:  
`docker-compose up --build`  
in the project root.  
Example:  
 - curl -X GET -H 'Content-Type: application/json' -d '{"type": 1}' http://localhost:8081/get_timeslots -- returns all timeslots because there is no column "type" -- should be able to do more elegantly but whatever
 - curl -X GET -H 'Content-Type: application/json' -d '{"timeslot_id": "a0869c06-6a85-482e-b93a-6be9a5f16c7a"}' http://localhost:8081/get_timeslots
 - curl -X GET -H 'Content-Type: application/json' -d '{"doctor": "7aebdbe2-8a82-4e96-9760-7e8e0d3f79e0", "date": "2023-05-19 19:45:00"}' http://localhost:8081/get_timeslots
 - curl -X POST -H 'Content-Type: application/json' -d '{"doctor": "fe150f8b-3866-4544-8921-d70dde8596e0", "start_date": "2023-07-02 12:15:00" , "end_date": "2023-07-02 12:45:00"}' http://localhost:8081/new_timeslots -- adds as many timeslots as possible knowing that timeslot is 15 minutes and starts at 00, 15, 30 or 45 minutes of any hour (2 in this example)
 - curl -X POST -H 'Content-Type: application/json' -d '{"timeslot_id": "a0869c06-6a85-482e-b93a-6be9a5f16c7a"}' http://localhost:8081/delete_timeslot
