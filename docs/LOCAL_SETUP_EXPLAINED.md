# Sites Values

## How to hack locally (Explained)

Disclaimer:

This setup instructions are focused on Linux users, if you are using MacOs or Windows, you might need to adapt.

### A. Set Up your Python Virtualenv

1. Choose and download

    First, setup your favorite virtualenv. I recommend [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

2. Create and activate your virtualenv.

    If you are using virtualenvwrapper. You might need to source it on your terminal first.

    `source /usr/local/bin/virtualenvwrapper.sh`

    To create you virtual environment just prompt:

    ``mkvirtualenv {your_venv_name} --python=`which python3\` ``

    It will activate automatically. But, for future reference, when you already have an environment set up, to activate it you prompt:

    `workon {your_venv_name}`

    And to deactivate it, just prompt:

    `deactivate`

### B. Python requirements

With your virtualenv set up and activated, to download all project requirements, on your project root folder:

`pip install -r requirements.txt`

### C. Frontend requirements

You will need [npm](https://www.npmjs.com/) and [Node](https://nodejs.org).

You might get those by

`sudo apt install npm nodejs`

Then change directory into frontend folder:

`cd frontend`

And install project requirements locally:

`npm i`

### D. Watch your frontend files while developing

You will need this to serve webpack automagically bundled assets after each change on frontend files

`npm run watch`

### E. Create the database

First, you will need postgres

`sudo apt-get update`
`sudo apt-get install postgresql postgresql-contrib`

Now, set your postgres user and database:

`sudo su postgres`

`createuser -d -SRP sites` (you will be prompted a password, please, insert CHECKPASS)

`createdb -O sites sites`

Now, your database and user are created.

All set, to disconnect from database:

`sites=# \q`

Then switch back to your user:

`su`

### F. Migrate database schema

Back at root folder

`cd ..`

`python manage.py migrate`


### G. Raise your Django local server

You will need some environment variables now, create a `.env` file:

```
export DEBUG=1
export DATABASE_URL=postgres://sites:CHECKPASS@localhost:5432/sites
export LANG=en_US.UTF-8
```

and source it.

`source .env`

Then, run your local server

`python manage.py runserver`

All done, it should be acessible on `localhost:8000`
