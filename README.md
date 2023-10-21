# Backend Integrador

## Creating a virtual environment in Windows
1. Open a command prompt and navigate to the directory where you want to create the virtual environment.
2. Type `python -m venv .venv` and press Enter.
3. To activate the virtual environment, type `.venv\Scripts\activate` and press Enter.
4. You can now install packages and run your Python code within the virtual environment.
5. To install requirements, type `python -m pip install -r requirements.txt`
6. To deactivate the virtual enviroment, type `deactivate`
7. To remove all packages, type: `pip freeze | xargs pip uninstall -y`

## Create image users
1. Create image users: `docker build -t inte_app .`


## Run Unittest
1. To run all test: `python -m unittest discover -s test -v`
2. To run a specify test: `python -m unittest test/test_signup.py`
3. To test coverage: `python -m coverage run -m unittest` or `coverage run -m unittest tests/test_signup.py -v`
4. To test coverage report in console: `python -m coverage report`
5. To a test coverage report more detail in html format: `python -m coverage html`