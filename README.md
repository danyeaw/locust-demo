## Load Testing with Locust

### Prerequisites

Python 3 and pipenv (https://github.com/pypa/pipenv) are required.

### Installation

1. Clone the repository:

        cd /path/to/your/projects
        git clone https://github.com/empug/locust-demo.git

2. Make the repository directory the current directory:

        cd locust-demo

3. Install packages using pipenv:

        pipenv install
        
    This command installs the packages specified in *Pipfile*. These include
    Flask (http://flask.pocoo.org), Locust (https://locust.io),
    Gunicorn (http://gunicorn.org) and Eventlet (http://eventlet.net).

### Running a single-threaded Flask app

1. Launch the Flask web application (hello.py)

        pipenv run flask run
        
    *Note that the app is served on port 5000.*

2. Visit the application endpoints in your browser (at localhost:5000):

        /
        /health
        /shorter
        /longer

3. In a new terminal, run Locust and test with different numbers of users:

        pipenv run locust --host=http://localhost:5000

### Running the Flask app behind Gunicorn (single synchronous worker)

1. Launch Gunicorn

        pipenv run gunicorn hello:app
        
    *Note that the app is now served on port 8000.*

3. In a new terminal, run Locust and test with different numbers of users:

        pipenv run locust --host=http://localhost:8000

### Running the Flask app behind Gunicorn (single asynchronous worker)

1. Launch Gunicorn

        pipenv run gunicorn -k eventlet hello:app
        
    *Note that the app is now served on port 8000. It is using the evenlet package
    to handle web requests using coroutines.*

3. In a new terminal, run Locust and test with different numbers of users:

        pipenv run locust --host=http://localhost:8000
