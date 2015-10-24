install_soft:
	sudo apt-get install mongodb python-virtualenv

env_create:
	virtualenv --python=python3 --no-site-packages .venv;

install_eggs:
	pip install -r requirements.txt


pep8:
	pep8 --exclude='.*/' .
