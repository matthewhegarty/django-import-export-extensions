
## localhost

```
DB_HOST=localhost REDIS_HOST=redis://localhost:6379/1 python3 test_project/manage.py showmigrations
```

## Celery container

```
cd /home/app/server
PYTHONPATH=. python3 test_project/manage.py shell_plus
```
