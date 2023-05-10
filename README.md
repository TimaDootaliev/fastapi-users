# Users API

## How to setup

Create .env file and fill it with the data below

```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

Create database as in DB_NAME

## How to run project

```
uvicorn app.main:app --reload
```

### File Structure
```
├── app
│   ├── auth
│   │   ├── models.py
│   │   ├── queries.py
│   │   └── routers.py
│   ├── database.py
│   ├── main.py
│   └── settings.py
└── requirements.txt
```