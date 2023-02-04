dev:
	python3 manage.py makemigrations csfd
	python3 manage.py migrate  
	python3 manage.py runserver

remove:
	python manage.py flush --no-input