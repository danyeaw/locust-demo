## Load Testing with Locust

### Prerequisites

Python 3 and pipenv (https://github.com/pypa/pipenv) are required.

### Installation

1. Clone the repository

2. Make the repository directory the current directory:

        cd locust-demo

3. Install packages using pipenv:

        pipenv install
        
    This command installs the packages specified in *Pipfile*. These include
    Quart (https://gitlab.com/pgjones/quart), Locust (https://locust.io),

### Running a AsyncIO enabled Quart app

1. Launch the Quart web application (hello.py)

        pipenv run quart run
        
    *Note that the app is served on port 5000.*

2. Visit the application endpoints in your browser (at localhost:5000):

        /
        /health
        /shorter
        /longer

3. In a new terminal, run Locust and test with different numbers of users:

        pipenv run locust --host=http://localhost:5000

