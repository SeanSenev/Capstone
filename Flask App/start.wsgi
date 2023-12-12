import os, sys

PROJECT_DIR = '/Users/jesusfernandez/Desktop/Berkeley DS Masters/School Work/Capstone/Capstone/Flask App'

activate_this = '/Users/jesusfernandez/Desktop/Berkeley DS Masters/School Work/Capstone/Capstone/Flask App/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.append(PROJECT_DIR)

from w209 import app as application
