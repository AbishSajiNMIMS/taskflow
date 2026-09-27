# TaskFlow

A task tracker built end to end: Django backend, Docker deployment.

## Run locally

```powershell
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py createsuperuser
.\venv\Scripts\python.exe manage.py runserver
```

Open <http://127.0.0.1:8000/> and sign in with a Django user. Tasks are private
to their owner and can be created, completed, reopened, or deleted.

## Test

```powershell
.\venv\Scripts\python.exe manage.py test tasks
```

## Docker

```powershell
docker build -t taskflow .
docker run --rm -p 8000:8000 taskflow
```