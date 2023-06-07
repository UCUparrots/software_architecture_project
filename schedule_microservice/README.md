# software_architecture_project
to start:  
`docker-compose up --build`  
in the project root.  
Example:  
 - curl -X GET -H 'Content-Type: application/json' -d '{"type": 1}' http://localhost:8080/get_timeslots -- returns all timeslots because there is no column "type" -- should be able to do more elegantly but whatever
 - curl -X GET -H 'Content-Type: application/json' -d '{"timeslot_id": "a0869c06-6a85-482e-b93a-6be9a5f16c7a"}' http://localhost:8080/get_timeslots -- should be able to do with other attributes, not juxt timeslot_id (similar to what is in appointments microservice)
 - curl -X POST -H 'Content-Type: application/json' -d '{"doctor": "fe150f8b-3866-4544-8921-d70dde8596e0", "start_date": "2023-07-02 12:15:00" , "end_date": "2023-07-02 12:45:00"}' http://localhost:8080/new_timeslots
 - curl -X POST -H 'Content-Type: application/json' -d '{"timeslot_id": "a0869c06-6a85-482e-b93a-6be9a5f16c7a"}' http://localhost:8080/delete_timeslot
