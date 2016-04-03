The deployed heroku app is currently available at [https://shorturl-rakib.herokuapp.com/](https://shorturl-rakib.herokuapp.com/)

# Local setup instructions

**Clone this repo into your file system**

	git clone git@github.com:syedrakib/shorturl-django.git ./shorturl-rakib
	cd ./shorturl-rakib

**Setup Python Virtual Environment**

Python Virtual Environment helps you to maintain your local python package dependencies in an isolated environment so that they do not interfere with the other python packages installed globally. One project should have one virtual environment of its own.

	wget https://pypi.python.org/packages/source/v/virtualenv/virtualenv-15.0.1.tar.gz
	tar zxvf ./virtualenv-15.0.1.tar.gz
	python ./virtualenv-15.0.1/virtualenv.py ./venv-shorturl-rakib
	rm ./virtualenv-15.0.1.tar.gz
	rm -rf ./virtualenv-15.0.1
	
**Activate the Python Virtual Environment**

	source ./venv-shorturl-rakib/bin/activate

We will deactivate this Python Virtual Environment later

**Install python package dependencies**

All necessary python package dependencies of the project will be installed in the Virtual Environment. They won't interefere with any other python packages that maybe installed globally. The project will only utilize the packages installed in the virtual environment and not those that are available globally.
	
	pip install -r ./requirements.txt
	
**Test the project with django-nose tests**

	python ./manage.py test

**Run a lightweight python mini server**

This will allow you to try out the project locally running in a local Python Virtual Environment

	python ./manage.py runserver 0.0.0.0:8000

You can now visit [localhost:8000](http://localhost:8000) to try out the project. Press ***Ctrl+C*** when done to close the server.

**Deactivate the Python Virtual Environment**

	deactivate
	
# Deployment instructions

**Tryout the project in a local Heroku environment.**

You will need to have [Heroku-Toolbelt](https://toolbelt.heroku.com/) installed in your system and a Heroku account for this step to work. The local heroku environment will utilize python dependencies from the Python Virtual Environment.

	heroku login
	source ./venv-shorturl-rakib/bin/activate
	heroku local # press Ctrl+C when done
	deactivate

**Deploy on Heroku**

	heroku create shorturl-rakib
	heroku config:set DISABLE_COLLECTSTATIC=1
	git push heroku master

**Visit the deployed Heroku app**

	heroku open
	
# About this project

- uses `python` on `django` framework
- uses `django-nose` for running tests
- uses small `SQLite3` for protoyping the database layer - it's all abstracted away by the Django ORM. Real production should (and must) use more robust DB solutions like MySQL, PostgreSQL etc as a drop-in replacement of the Sqlite3 - the django ORM will take care of all logical abstraction between python and database.
- tried and tested on Mac OS X 10.11.3 and on Ubuntu 14.04.3 LTS

**There are 3 URL routes in this project.**
- `/` takes the user to the home page which presents a simple form to shorten a URL
- `/<shorturl>` takes the user to the short URL and redirects to the original reference of the short URL
- `/<shorturl>/inflate` allows the user to inflate the short URL and see detailed information of the shortened URL

# Thoughtwork behind the decisions taken

**Why did i use heroku**
- sufficient for protoyping concepts
- does not require mundane infrastructure setup for small prototyping 
- git push heroku master is all it takes
- lightweight heroku runtime is available for mac, windows, linux

**Why did i use sqlite**
- light-weight and sufficient for prototyping
- replacing the DB settings to use mysql/postgres will automatically take care of all table creation with respect to the models we have defined

**Deploying to production with SQLite**
- added db.sqlite3 file into Git tracker with only 1 db entry in it
- then untracked further changes to db.sqlite3 with `git update-index --assume-unchanged [<file> ...]`
- learned this technique from http://stackoverflow.com/q/3319479/636762
- this allows us to:
	- port the db.sqlite3 file wherever we want to deploy our app
	- the db.sqlite3 file (with only one prepopulated entry) stays in file system along with the source code
	- DB is always accessible regardless of MySQL / Postgres is provisioned or not

**What testing philosophy did i use**
- small helpers are small testable units

**Short URL generation (choice of algorithm)**
- mathematical algorithm to cryptographically determine a unique short URL
- generated a random 6 digit alphanumeric string from built-in randomizer APIs which allows 
(26+26+10)p6 = 40+ Billion short URLs
- chose the second approach

**URL generation flow**

	take long_URL
	if (this_long_URL_already_exists){
		return shortURL_for_this_long_URL
		# reutilizes existing short URL for this long URL that was already recorded previously
		# prevents database exhaustion by the same long URL being recorded in our DB over and over again
	}
	else{
		generate_a_random_short_URL(6)
	}

**Ensured collision proof short URL generation**

	generate_a_random_short_URL(int_URLlength){
		if (generated_short_URL_already_exists_in_DB)
			generate_a_random_short_URL(int_URLlength)
		else
			insert_new_entry_into_DB()
	}

**Furhter improvement possible for collision proof short URL generation**

	integer generated_short_URL_collides = 0
	generate_a_random_short_URL(int_URLlength){
		if (generated_short_URL_already_exists){
			generated_short_URL_collides++
			if (generated_short_URL_collides >= 2){
				notify_Website_Admin()
				int_URLlength++
			}
			generate_a_random_short_URL(int_URLlength)
		}
		else
			insert_new_entry_into_DB()
	}	


