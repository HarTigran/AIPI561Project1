install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

format:
		black *.py

lint:
		pylint --disable=R,C,broad-except, q_and_a.py

test:
		python -m pytest -vv --cov=q_and_a test_q_and_a.py

all: install lint test
