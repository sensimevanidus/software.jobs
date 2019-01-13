A sample web application for [web.py](http://webpy.org). In brief, the application fetches a list of open job positions from the github jobs API, groups them by the company and lists them in a fashion way (actually in Pinterest style).

To run the application, do the following:

1. Setup the virtual environment:
`virtualenv --distribute venv && source venv/bin/activate`

2. Install requirements:
`pip install -r requirements.txt`

3. Run the server:
`python index.py`

The server will listen to port 8080 by default.
