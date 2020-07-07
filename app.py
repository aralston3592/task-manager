import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "task-manager"

app = Flask(__name__)

# app.config["MONGO_DBNAME"] = 'task-manager'
# app.config["MONGO_URI"] = 'mongodb+srv://andyralston35:Tmnt3592@myfirstcluster-2yvra.mongodb.net/task-manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", '0.0.0.0'),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)
