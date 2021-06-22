# test_django

[REPO Link](https://github.com/python-hillel/test_django)



CREATE TABLE "students_student" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "last_name" varchar(80) NOT NULL, 
    "first_name" varchar(50) NOT NULL, 
    "age" integer NOT NULL, 
    "email" varchar(120) NULL, 
    "birthdate" date NOT NULL, 
    "enroll_date" date NOT NULL, 
    "graduate_date" date NOT NULL, 
    "graduate_date2" date NOT NULL, 
    "group_id" bigint NULL REFERENCES "groups_group" ("id") DEFERRABLE INITIALLY DEFERRED)
