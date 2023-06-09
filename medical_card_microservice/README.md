# Medical Card Service

Examples of GET/POST requests are in the `requests.http` file. I will attach them also here:


Add user information to the service table:
```
POST http://0.0.0.0:8080/add_user_to_medcard
Content-Type: application/json

{
  "user_id": "10311f8b-68b6-4c89-9761-950db9a4a6a2",
  "email": "custom@email.com",
  "name": "Name",
  "surname": "Surname",
  "phone": "1234567890",
  "birthdate": "2003-07-10",
  "doctorPhD": "",
  "doctor_specialization": ""
}
###
```

Get MedCard info by user id:
```
GET http://0.0.0.0:8080/form_medcard?uuid=10311f8b-68b6-4c89-9761-950db9a4a6a2
###
```

Add information about patient (some diagnosis) to user's medcard:
```
POST http://0.0.0.0:8080/update_medcard
Content-Type: application/json

{
  "patient_id": "10211f8b-68b6-4c89-9761-950db9a4a6a2",
  "doctor_id": "d8e2d68e-20c1-4e0d-b52e-8209ab07b5c8",
  "diagnosis_id": "2e4c874e-9361-4a76-bbaf-49f4ae5e7c09",
  "diagnosis": "diagnosis",
  "start_date": "2023-10-10 10:00:00",
  "notes": "note from me",
  "medicine": "som meds",
  "is_relevant": 1,
  "resolved_date": ""
}
###
```

Update relevantness of the diagnosis:
```
POST http://0.0.0.0:8080/update_diagnosis_status
Content-Type: application/json

{
  "diagnosis_id": "2e4c874e-9361-4a76-bbaf-49f4ae5e7c09",
  "resolved_date": "2023-07-10 10:00:00"
}
###
```

