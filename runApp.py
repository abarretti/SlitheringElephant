import os, json, sqlite3
from slitheringElephantApp import DataModel, DataDAO, DataController, KeyModel
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    keyModel = KeyModel.KeyModel(request.form.get('key'))
    dao = DataDAO.DataDAO('pythonDB.db')
    dataModel = DataModel.DataModel(dao)
    dataController = DataController.DataController(dataModel, keyModel)
    return dataController.getData()

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)

## http://127.0.0.1:8080/
## curl --data "key=testKey" http://127.0.0.1:8080/
