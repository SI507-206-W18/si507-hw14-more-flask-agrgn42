
from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("admin.html", entries=model.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/")    # redirects to a given page


@app.route("/deleteentry", methods=["POST"])
def deleteentry():
    post_id = request.form["id"]
    model.delete_entry(post_id)
    return redirect("/")


if __name__=="__main__":
    model.init()
    app.run(debug=True)



# with gunicorn:
# gunicorn app:app - looks inside object called app to run app.py file
# heroku communicates with git
# Create a `requirements.txt` file.
# Create a `runtime.txt` file. This will tell Heroku what version of Python to run.
# run `python --version` to find out what version you’re running
# write a single line into your `runtime.txt` file that looks like this (using your python version): python-3.6.4
# Create a `Procfile`. This is a file that will tell Heroku how to run your app. Again, just one line: web: gunicorn app:app --log-file=-
# Create a git repository in your project directory
# First, create a .gitignore and put in it: 
#   venv 
#   __pycache__
# git init 
# git add .
# git commit -m "first commit"

# heroku login
# heroku create

# remote -v
# heroku  https://git.heroku.com/tranquil-ravine-49028.git (fetch)
# heroku  https://git.heroku.com/tranquil-ravine-49028.git (push)
# git push heroku master

# git remote add origin https://github.com/agrgn42/herokutest.git

# now you can either "git push origin master" to update code, and then "git push heroku master" to deploy to the world





