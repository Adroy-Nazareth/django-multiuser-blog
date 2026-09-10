# Django Multiuser Blog

A small, reviewer-ready multi-user blog built with Django and PostgreSQL. Features include Django authentication, posts, tags, search, pagination, comments with admin moderation, RSS, tests, seed data, and Render deployment configuration.

## Features
- Register, login and logout with Django's built-in authentication
- Create and edit your own posts
- Tags and tag filtering
- Search across titles, excerpts, content and tags
- Pagination (5 posts per page)
- Comments require admin approval before appearing publicly
- Django admin for posts, tags and comment moderation
- RSS feed at `/feed/`
- SQLite locally and PostgreSQL in production
- 10 seeded sample posts
- Render + PostgreSQL deployment configuration

## Local setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_blog
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Reviewer admin credentials
Username: `reviewer`

Password: `BlogReview2026!`

Admin: `/admin/`

This is a demo/reviewer account only. Change the password for any real deployment.

## Tests

```bash
python manage.py test
```

## Deployment

`render.yaml` defines a Django web service and PostgreSQL database. Set the repository as a Render Blueprint. The build step installs dependencies, migrates the database, collects static files, and seeds 10 demo posts.

Required production environment values include `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`, and `ALLOWED_HOSTS`.

## Screenshots / results

After deployment, add screenshots of the home/search page, post page, registration/login, admin comment moderation, and the live deployed application here.

## Reflection

Keeping the first version intentionally small made the core user flow easy to understand and test. The project demonstrates practical backend fundamentals: relational persistence, authentication, validation through Django forms, moderation workflows, automated tests, environment-based configuration, static-file handling, deployment, and documentation.

## Tech stack
Django · PostgreSQL · Django Auth · Django Admin · RSS · Gunicorn · WhiteNoise · Render
