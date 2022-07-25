release: python manage.py makemigrations personal_budget && python manage.py migrate
web: gunicorn personal_budget.wsgi