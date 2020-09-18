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

Finally, you'll need to add the following into the `src/config/.env`:
```
DB_NAME=gardenbuilder
DB_USER=`databaseUsernameHere`
DB_PASSWORD=`databasePasswordHere`
DB_HOST=localhost
DB_PORT=5432
DJANGO_SECRET_KEY='secretKeyHere'
```

### To Run

```bash
python gardenbuilder/manage.py migrate
python gardenbuilder/manage.py runserver
```

Then navigate to [localhost:8000/graphql](http://localhost:8000/graphql).
You should see the graphiQL editor and be able to write queries like
```graphql
query {
  gardens{
    gardenName
  }
}
```

## Contributing

We would love some help, especially for [Hacktoberfest](https://hacktoberfest.digitalocean.com/)!

### General Code Contributions

There are a number of [issues](https://github.com/capndave/gardenbuilder-api/issues) that we would love your help with. Many of them are fairly easy and are tagged as ` good first issue`. Most are things that I (capndave), just haven't gotten around to yet. Feel free to fork, work on, and submit a pull request for anything you see an issue for.

If the issue you want to work on is a spelling or grammar mistake, or a documentation issue, feel free to make a pull request with your changes (without submitting an issue first)

For all other changes, please submit an issue before submitting a pull request! Please reference a given issue in cases where a related pull request is made.

### Further Involvement

If you are interested in ok-ing pull requests, co-managing this repo or anything else beyond occasional contributions, please email me at capndavet@gmail.com. I'd love your help!

## Contact

Questions? Feel free to contact Dave at `capndavet@gmail.com`.