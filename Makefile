
setup:
	@python3 -m venv ~/.jiraclient

install:
	@. ~/.jiraclient/bin/activate &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	@. ~/.jiraclient/bin/activate &&\
		find . -name "*.py" -exec pylint --disable=R,C {} \;

test:
	@. ~/.jiraclient/bin/activate &&\
		python -m pytest -vv --cov=parser parser/*_test.py
fmt:
	@. ~/.jiraclient/bin/activate &&\
		find . -name "*.py" -exec black {} \;

all: setup install lint test
