# **Smathchat**

![YAP](https://giphy.com/embed/atpu7tQWSWOE6GeeEy)

## Description

Smathchat is a game-like web application where users can solve different math problems and chat together. The app also records the time users need to complete a math challenge and shows 3 fastest students in the championship chart. In order to do this, I use the fetch() method to get this.state value of the time in the React app and send data via a POST request to an API route then save data in the database. The chat app allows them to chat in real time and to learn from each other and make study more fun. I got this idea for my final project from my own study experience when my classmates needed help to solve math problems. It's fair to say that students often learn from peers more than from teachers.


The project was built using Django as a backend framework (with Django Channels) and JavaScript and React as a frontend programming language. All the users information are saved in database (SQLite)

All webpages of the project are mobile-responsive.

## Specifications:
- User registration:
	- Users are required to log in in order to use the math app and keep track of their records. Users can either register or log in.
- Real live chat:
	- Users can use the chat log while solving a math problem to communicate with other students. When users click send the message will show up with their name in the chat log.
- Addition 1 digit app:
	- Using React to render addition problems with 1 digit numbers. Each time the users get the correct answer, increase their scores. Once the users get 10 for the score, render the winner screen and stop the timer. Show the users restart button to restart the game.
- Addition 2 digit app:
	- Using React to render addition math exercises with 1 to 2 digit numbers. Each time the users get the correct answer, increase their scores. Once the users get 10 for the score, render the winner screen and stop the timer. Show the users restart button to restart the game.
- Multiplication app
	- Using React to render multiplication problems with numbers up to 13. Each time the users get the correct answer, increase their scores. Once the users get 10 for the score, render the winner screen and stop the timer. Show the users restart button to restart the game.
- Time recorder:
	- Show the time recorder while users are solving math problems. Once the users win, stop the timer and save the record by make a POST request to API route /record
- Championship
	- Show the 3 fastest students’ records for each math problem in the top chart: Championship while users are solving math problems. Each record includes the user name, the record and the timestamp.
- User progress
	- In the profile page, show the users progress by the math problem categories.
- Mobile responsive design for all pages.


## Files and directories
- chat - main application directory.
    - migrations - a directory stores all database migrations for the application
    - static/chat - a directory contains all static content.
        - styles.css - contains style for the templates
        - giphy.gif - gif file used in the webpage
        - Harvard.jpg - backgroud picture for the chat app
    - templates - a directory contains all application templates.
        - addition1.html - shows addition math exercises (for 1 digit number) and chat room.
        - addtion2.html - shows addition math exercises (for 1-2 digit numbers) and chat room.
        - index.html - main template for homepage when user go to the website.
        - layout.html - the website base templates. All other tempalates extend it.
        - login.html - a template for users to login.
        - multiplication.html - shows multiplication math exercises and chat room.
        - profile.html - a template to show user's progress.
        - register.html - main template for unregistered users. It shows registration forms.
     - _init_.py -  required file to start the directories as containing packages
     - admin.py - stores all ModelAdmin classes in the Django admin.
     - apps.py - the AppConfig of the application.
     - consumers.py - stores WebSocket consumer that accepts all connections, receives messages from its client, and echos those messages back to the same client.
     - models.py - contains User model I used in the project.
     - routing.py - a routing configuration for the chat app that has a route to the consumer.
     - tests.py - a file for automated tests
     - urls.py - lists all application URLs.
     - views.py - contains all application views.
- finalproject - project directory
- venv - virtual machine directory
- db.sqlite3 - a SQLite file to store database for the app
- manage.py - Django's command-line utility for administrative tasks

## Installation
- `cd` into the project directory.
- Start a virtual machine `py -m venv venv`
                            `venv\Scripts\activate`.
                            Install Django `pip install django` and Channels `python -m pip install -U     channels` in the virtual machine.
- Install Docker to install and run Redis. Start a Redis server (if not available):
    ` docker run -p 6379:6379 -d redis:5`
    ` python -m pip install channels_redis`
- Open a Django shell
    ` python manage.py shell`
    >>> import channels.layers

    >>> channel_layer = channels.layers.get_channel_layer()

    >>> from asgiref.sync import async_to_sync

    >>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})

    >>> async_to_sync(channel_layer.receive)('test_channel')

- Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`
- Run the web  ` python manage.py runserver`
- Go to the website address and register an account.

Deploy on heroku
- heroku login
- git clone
- cd
- heroku create
- Disable the collectstatic during a deploy `heroku config:set DISABLE_COLLECTSTATIC=1`
- deploy `git push heroku main`
- `heroku run python manage.py migrate`
- `heroku ps:scale web=1:free worker=1:free`
- `heroku addons:create heroku-postgresql`
- `heroku addons:create heroku-redis`
- `heroku config:set DEBUG_VALUE="False"` # yes, "False" as a string!
- `heroku config:set SECRET_KEY="your_secret_key_in_strings"`



Youtube link: https://youtu.be/Z5xwn1h-rE8
