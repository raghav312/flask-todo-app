#importing required dependencies

from flask import Flask,request, render_template, Response ,url_for ,jsonify , json
from flask_sqlalchemy import SQLAlchemy
import helper , uuid

app = Flask(__name__)

# base endpoint
@app.route('/')
def index():
    #establish database and table
    helper.start()
    return render_template('index.html')   

# Note : id -> UUID as a unique key
#        complete -> True/False shows whether task is completed or not
#        item -> Title for the task


# base endpoint/addNote : A POST method that stores a task in the database and also provides the UUID the note.
#  request -> { "item" : "task_name"}
# ID is given automatically and complete by default is False.
@app.route('/addNote' , methods=['POST', 'GET'])
def postNote():
    try:
        # Get item from the POST body
        req_data = request.get_json()
        item = req_data['item']
        id = uuid.uuid4()
        # Add item to the list
        res_data = helper.add_to_list(str(id),item)

        # Return error if item not added
        if res_data is None:
            response = Response("{'error': 'Item not added - " + item + "'}", status=400 , mimetype='application/json')
            return response

        # Return response
        response = Response(json.dumps(res_data), mimetype='application/json')

        return response
    except Exception as e:
        return Response(e.__getattribute__, status=400 , mimetype='application/json')
    

# base endpoint/showNote : A GET method that fetches all the task in the database along with complete and id.
@app.route('/showNote')
def getNote():
    # get the list
    res_data = helper.get_list()
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

#base endpoint/clearList : A GET method that deletes all the tasks in the database along. 
@app.route('/clearList')
def clearList():
    #command to clear list
    res_data = helper.del_list()
    # Return response
    response = Response(json.dumps(res_data), mimetype='application/json')
    return response

#base endpoint/updateStatus : A POST method that updates the status of a the task in the database, have to provide task id and complete status.
# request -> { "id" : "23123123sadfasf" , "complete" : "True" } 
@app.route('/updateStatus', methods = ['POST','GET'])
def updateStatus():
    try:
        # Get id,status from the POST body
        req_data = request.get_json()
        id = req_data['id']
        status = req_data['status']
        # make update command
        res_data = helper.update_note(status,id)

        # Return error if item not updated
        if res_data is None:
            response = Response("{'error': 'Item not updated - " + id + "'}", status=400 , mimetype='application/json')
            return response

        # Return response
        response = Response(json.dumps(res_data), mimetype='application/json')

        return response
    except Exception as e:
        return Response(e.__getattribute__, status=400 , mimetype='application/json')
    
#base endpoint/deleteNote : A POST method that deletes the task in the database, have to provide task id.
# request -> { "id" : "23123123sadfasf" }
@app.route('/deleteNote' , methods=['POST', 'GET'])
def del_note():
    try:
        req_data = request.get_json()
        id = req_data['id']
        res_data = helper.del_note(id)
        # Return response
        response = Response(json.dumps(res_data), mimetype='application/json')
        return response
    except Exception as e:
        return Response(e.__getattribute__, status=400 , mimetype='application/json')


if __name__ == "__main__" :
     with app.app_context():
        app.run(debug = True)
     