# django-graphql

## How run in local
1. Create postgresql database name graphql
2. Export DATABASE_PASSWORD
```shell
$ export DATABASE_PASSWORD=PASSWORD
```
3. Create new python environment
```shell
$ python -m venv env
$ source env/bin/activate
```
4. Install libraries
```shell
$ pip install -r requirements.txt
```
5. Migrate database
```shell
$ python manage.py migrate
```

6. Run django server
```shell
$ python manage.py runserver
```


7. Try graphql
[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
