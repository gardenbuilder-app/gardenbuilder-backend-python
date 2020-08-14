# Gardenbuilder

Main project for Gardenbuilder

## About

Made with Django, React, Postgres and GraphQL

## Before running

Follow these steps to set up and initialize a virtual environment. From inside the project root:

```bash
python3 -m venv env                 # Set up virtual env
source env/bin/activate             # Activate virtual env
pip install -r requirements.txt     # Install requirements
```

## To Run

```bash
python gardenbuilder/manage.py runserver
```

Then navigate to [localhost:8000/graphql](http://localhost:8000/graphql).
You should see the graphiQL editor and be able to write queries like
```graphql
query {
  allGardens{
    gardenName
  }
}
```
