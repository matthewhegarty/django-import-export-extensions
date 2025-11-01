My local changes are in mrh-additions branch.

```
# start db and redis
docker compose up --build
cd test_project
python3 manage.py runserver
python3 manage.py createsuperuser
```

test data in `test_files/`

- Add an instrument via the Admin UI
