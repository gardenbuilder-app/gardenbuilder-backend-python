# Gardenbuilder

GraphQL API and database interface for Gardenbuilder

## About

Made with Django, Postgres and GraphQL

## Getting Started

### Setup

Follow these steps to set up and initialize a virtual environment. From inside the project root:

```bash
python3 -m venv env                 # Set up virtual env
source env/bin/activate             # Activate virtual env
pip install -r requirements.txt     # Install requirements
```

You'll need to also set up a postgresql database named gardenbuilder. I would follow the directions [here](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/).

Alternatively, you could run postgresql locally using docker: `docker run -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=gardenbuilder -p 127.0.0.1:5432:5432/tcp library/postgres`

Finally, you'll need to add the following into the `config/.env`:

```
DB_NAME=gardenbuilder
DB_USER=root
DB_PASSWORD=secret
DB_HOST_LOCAL=localhost
DB_PORT=5432
DJANGO_SECRET_KEY=secretKeyHere
```

### To Run

```bash
python manage.py migrate
python manage.py runserver
```

Then navigate to [localhost:8000/graphql](http://localhost:8000/graphql).
You should see the graphiQL editor and be able to write queries like

```graphql
query {
  gardens {
    name
  }
}
```

### To Run Tests

`python manage.py test`


## Contributing

For Contributing, Read our [Contribution Guidelines](https://github.com/saurabhhere/gardenbuilder-backend/blob/master/CONTRIBUTING.md#contributing)


## Contact

Questions? Feel free to contact Dave at `capndavet@gmail.com`.
