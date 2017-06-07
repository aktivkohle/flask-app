# Python Flask Web App

This app will feed a search query to the GitHub API which it detects in the browser URL, wait for the response then render the results in a web page

To run it do this on the Linux command line :

`$ export FLASK_APP=application.py` 

`$ flask run`

CTRL-click on link in command terminal and append _navigator?search_term=mySearchTerm_

eg. to find repositories related to the raspberry pi:
http://127.0.0.1:5000/navigator?search_term=raspberry

Aallow it time to query the API and display - usually around 15 seconds.
Ignore any error message in the browser during that time.

Then change the query word in the URL in the browser to another one and repeat.
