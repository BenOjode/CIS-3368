import flask
from flask import jsonify
from flask import request
import creds
from sql import create_connection
from sql import execute_read_query
from sql import execute_query

app = flask.Flask(__name__)
app.config["Debug"] = True


# GET request for seeing all animals within Zoo
@app.route('/api/zoo', methods=['GET'])
def view_animals():
    myCreds = creds.Creds()
    # Creating connection to Zoo_HW2 database
    connect = create_connection(myCreds.connection_string, myCreds.user, myCreds.password, myCreds.database)
    cursor = connect.cursor(dictionary=True)
    # SQL Query to view animals in Zoo table
    sql = "SELECT * FROM Zoo"
    cursor.execute(sql)
    Zoo = cursor.fetchall()
    return jsonify(Zoo)

# POST request for adding new instances to Zoo
@app.route('/api/zoo', methods=["POST"])
def add_animals():
    request_data = request.get_json()
    myCreds = creds.Creds()
    connect = create_connection(myCreds.connection_string, myCreds.user, myCreds.password, myCreds.database)
    cursor = connect.cursor(dictionary=True)
    # SQL query to insert a new entry
    sql = "SELECT * FROM Zoo"
    cursor.execute(sql)
    Zoo = cursor.fetchall()
    last_zoo_id = Zoo[-1]['id']
    request_data['id'] = last_zoo_id + 1

    newkingdom = request_data['kingdom']
    newdomain = request_data['domain']
    newspecies = request_data['species']
    newclass = request_data['class']
    newage = request_data['age']
    newalive = request_data['alive']
    newanimalname = request_data['animalname']
    sql = (
              "INSERT INTO Zoo(domain, kingdom, class, species, age, animalname, alive) VALUES " "('%s', '%s', '%s', '%s', '%s', '%s', '%s')") % (
              newdomain, newkingdom, newclass, newspecies, newage, newanimalname, newalive)
    execute_query(connect, sql)
    return 'Request to add is complete.'

# DELETE request for deleting instances from Zoo
@app.route('/api/zoo', methods=['DELETE'])
def delete_animals():
    request_data = request.get_json()
    id_delete = request_data['id']
    myCreds = creds.Creds()
    connect = create_connection(myCreds.connection_string, myCreds.user, myCreds.password, myCreds.database)
    sql = ("DELETE FROM Zoo WHERE id = %s" %id_delete)
    execute_query(connect,sql)
    return 'Request to delete is complete.'

# PUT request for updating entries in Zoo
@app.route('/api/zoo', methods=['PUT'])
def update_zoo():
    request_data = request.get_json()
    id_update = int(request.args['id'])
    newalive = request_data['alive']
    myCreds = creds.Creds()
    connect = create_connection(myCreds.connection_string, myCreds.user, myCreds.password, myCreds.database)
    sql = """UPDATE Zoo SET alive = %s WHERE id = %s;"""
    vals = (newalive, id_update)
    cursor = connect.cursor()
    cursor.execute(sql, vals)
    connect.commit()
    return 'Update to change alive status successful!'

app.run()



