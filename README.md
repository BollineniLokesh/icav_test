# icav_test

Build And Deploy A BOOKS_INFO PROJECT

This is a flask_restful api's code for signin the book system and get the list of books info like author,title,dimensions based your input given in no of rows and along with unittest cases

How to run the project
Clone the project Repository
<...............project_repository................>
git clone {project_folder}
Enter the project folder and create a virtual environment create a virtual environment

$change directory to git repository icav_test

$python -m venv env 

Activate the virtual environment

$ source env/bin/actvate #On linux Or Unix

$ source env/scripts/activate #On Windows 

Install all requirements

$ pip install -r requirements.txt

Run the project in development

$python icav_tech_challenge/app.py

TO TEST THE SINGIN API
http://0.0.0.0:5000/api/signin ---> POST METHOD

IN Body we need to pass json request
#Default_user
user ={'user_name':'book_management@admin.com','password':'Welcome@123'}

TO  GET THE BOOKS INFO ---> GET METHOD
http://127.0.0.1:5000/api/booksinfo
IN HEADERS NEED TO PARAMETER WITH VALUE LIKE rows  = '3' OR rows='' we need to pass number or empty string

### WE CAN TEST THE API IN POSTMAN


FOR TO TEST THE CODE COVERAGE OR RUN TESTS

$pytest --cov 

$coverage html
