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

## GitHub Pages

GitHub Pages cannot run Django, Python, authentication, or SQLite. This project
also includes a standalone browser-only edition in
[docs/index.html](docs/index.html). To publish it, push the repository to
GitHub, open **Settings → Pages**, select **Deploy from a branch**, choose the
default branch and the `/docs` folder, then save. GitHub will provide the Pages
URL after the deployment completes.

The Pages edition stores tasks in the visitor's browser with `localStorage`;
it does not share data with the Django edition. Use a Python-capable host
(such as Render, Railway, Fly.io, or Azure) for the full account/database app.