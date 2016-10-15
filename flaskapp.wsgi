import sys
import os
sys.path.insert(0, '/var/www/html/flaskapp')

# Activate your virtual env
activate_env="/home/miketwo/buzzword-bingo/.buzzvenv/bin/activate_this.py"
execfile(activate_env, dict(__file__=activate_env))

from hello import app as application
