from queryApi import querygithub
from flask import request, Flask, render_template
from jinja2 import FileSystemLoader   
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('.')
tpl = env.get_template('template.html')

app = Flask('GitHubNavigator')
app.config.from_object(__name__)


def runquery(st):
    print ("-- querying GitHub API --")
    out = querygithub(st)
    return out


@app.route('/navigator')
def navigator():
    t = request.args.get('search_term')
    print ("-- search term ", t, " received --")
    f = runquery(t)
    return render_template(tpl, fiveNewest=f, search_term=t)
