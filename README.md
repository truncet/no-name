# Steps to setup on development environment

1. Clone the repo `no-name`
2. Create virtual environment `python -m venv <virtual_env_name>`
3. `pip install -r requirements.txt`
4. Create a postgres database on your local(install postgres in your system and use pgAdmin client for easy use)
5. Create a `.env` file inside the root directory of the project `no-name`
6. For Firebase to verify the token, you need the firebase application id. Create one or ask the team. Need to add this to env file with key `GOOGLE_CLOUD_PROJECT`

## Running migrations
- inside the .env file give the values for these keys
    ```DB_USER=<your_db_username>
    DB_PASSWORD=<your_db_password>
    POSTGRES_SERVICE_HOST=<your_db_host>
    POSTGRES_SERVICE_PORT=<your_db_port>
    DB_NAME=<your_db_name>```
- now If you are initializing db for first time, run `flask db init`
- To create migrations for new or changed models, run `flask db migrate`
- now inside the `no-name` directory run `flask db upgrade`


## Running the application in local
- set the environment variable, FLASK_APP to "manage.py"
- inside `no-name` directory run `flask run`
