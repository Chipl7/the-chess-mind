.PHONY install freeze

install:
		.\venv\Scripts\activate
		pip install -r requirements.txt

freeze:
		pip freeze > requirements.txt
