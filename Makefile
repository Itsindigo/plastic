env:
	pipenv install --dev
	ln -fs $(abspath ./src/manage.py) "$$(pipenv --venv)/bin/manage.py"

requirements:
	pipenv install
