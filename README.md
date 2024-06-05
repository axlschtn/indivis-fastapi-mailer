#### Lead 

[Heroku Application link](https://indivis-mailer-1899ecdcdbf4.herokuapp.com/)

Once the clone is success, you nedd to Install poetry dependency first if you don't have it on your local machine
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

- poetry install project
```bash
poetry install
```

- launch the project
```bash
poetry run uvicorn src.main:app --port 3006 --reload
```
