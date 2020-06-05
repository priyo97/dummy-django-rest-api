# dummy-django-rest-api
A mini-project that was given by a company.

Objective: The pdf present in the folder explains the requirements.
Dependencies: Django, Faker

Procedure to initilize and run the project:

1. Run python3 manage.py makemigrations
2. Run python3 manage.py migrate
3. Run python3 manage.py add_activity
3. Run python3 manage.py runserver

The api can be referenced by the following url: http://localhost:8000/activity

query parameters: firstname, lastname, tz

/activity - will give activity data for all users

/activity?firstname=[value] - will give activity of users whose firstname is equal to [value]

/activity?lastname=[value] - will give activity of users whose lastname is equal to [value]

/activity?tz=[value] - will give activity of users whose timezone is equal to [value]

The above parameters can also be combined together.

add_activity is management command for manege.py which will randomly add 3 users and their corresponding activity period info in the database every time it is run. 

