# Execution Guide for ATK-System 
## 6430613024 / 6430613026


Step 1 : Copy this link “https://github.com/Yasu46/atk_project.git” and use the command below to clone a repository.
```bash
git clone https://github.com/Yasu46/atk_project.git
```

Step 2 : Create .env file in  ATK_PROJECT directory and copy the texts below.

```bash
SECRET_KEY=django-insecure-fqfhhjiy+$-d9b*kn+uc5f%3(2dh75v0ngx=$6^+(z6ah8jzv7
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=db
DB_USER=user
DB_PASSWORD=pass
DB_HOST=db
DB_PORT=5432
```

Step 3 : Open Docker Desktop and go to the text editor you used to clone the repository, then use the command below to build the image.

```bash
docker-compose up –build -d
```

Step 4 : In your terminal, go to root directory on the project folder, then use the command below to enter the docker container shell

```bash
docker exec -it web bash
```

Step 5 : After you enter the docker container shell you can use the Django command, then use the command below to make the model into a database schema. 

```bash
python manage.py makemigrations
```

Step 6 : Use the command below to apply the schema. 

```bash
python manage.py migrate
```

Step 7 : To access to the admin page, you need to create an admin account and use the command below to create it. 

```bash
python manage.py createsuperuser
```

Step 8 : After you enter the command above, you will be asked to put your username and password to create an admin account, type any username and password and keep it somewhere (any text editor or memos to not forget).


# Guide for How to use ATK-System for Student

Step 1 : When a user access localhost:8000, the system will ask the user to login or register to the system. 
To register or login, users must enter the username and password.

Step 2 : After login to the system, users are able to submit their ATK test result to the system. 
To submit the result, users must choose the right answer if the result is negative or positive, and attach the picture of the ATK test result. 

Step 2 : After submitting the ATK result successfully, the screen displays the appreciated message and the user can go back to the home page. 


# Guide for How to use ATK-System for Admin

Step 1 : Access localhost:8000/admin and enter the username and password that was set in the execution guide step 8 to login to the admin page. 

Step 2 : Admin can see the user information and submit ATK result information.

