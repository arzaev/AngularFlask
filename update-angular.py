import subprocess

subprocess.call(('cd angular-flask && ng build'), shell=True)
subprocess.call(('mv angular-flask/dist/angular-flask/*.js /static/'), shell=True)
subprocess.call(('mv angular-flask/dist/angular-flask/*.css /static/'), shell=True)
subprocess.call(('mv angular-flask/dist/angular-flask/*.html /templates/'), shell=True)
