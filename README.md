![sqlalchemy](https://cdn.discordapp.com/attachments/733391066136313879/1159942451570688041/FLASK_SQLALCHEMY.png?ex=6532db97&is=65206697&hm=e16a1a39930ef714968ac69ea8c422f7f1270ee4a7fe0bf7ae50fda387c52881&)

![Logo](https://img.shields.io/badge/Created%20by-GabryWasTaken-blue)
## DESCRIPTION
In this website you can manage a list of users, you can perform the following actions:  

**Add a User** 
 * Add a new user to the database by fill out a form in the main route.

**Get Users List**
 * Get a list of all the users in the database in the main page of the site. 

**Search a User** 
 * Get the details of a single user by searching for a part/full name or email 

**Update User**
* Update or modify an existing user details in the main page. 

**Delete User**
* Delete a user from the database in the main page. 

This provides a centralized way to add, view, edit or remove users without needing to manage the database directly. \
This app is very similar to my previous API [MemberAPI](https://github.com/GabryWasTaken/MemberAPI) but here you can manage a list of users with a graphic interface.
## PREREQUISITES

![Python3](https://img.shields.io/badge/Install-Python%203%20or%20greater-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads%2F) ![sql](https://img.shields.io/badge/install-SQLclient-orange)

Install the external dependencies, they are located in
```bash
requirements.txt
```
Create a SQL database or connect to another in remote and insert the URI of the database in config.cfg:
```bash
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/db_name' #modify this
```
## HOW TO RUN PROGRAM

* Install all of the prerequisites in your virtual environment or your machine with the following command:
```bash
pip install -r requirements.txt
```
* Write this command to run the API:
```bash
python3 ./app.py
``` 
* Or : 
```bash
flask run
``` 
if you wanna start the program with flask run you need to set the environment variable with the command:
```bash
set FLASK_APP=app.py
``` 




