from flask import Flask, request, jsonify

app = Flask(__name__)
# just created a Flask server, used to run our API, with basic initialization


# creating out root (our endpoint) - is a location in our API to get some kind of data
# diff kinds of roots (below is a simple one)

@app.route("/") # to make this root/func accessible, we add the decorator @app, which is the name of Flask app above (same var name)
# path we want to access is the str - "/" is the default root; root is really what comes after the slash in URL addr bar
def home():
    return "Home" # returning some data to user when they reach this root

# other roots we can create with diff HTTP methods
# whenever writing an API, we work with HTTP - protocol used to communicate data over the internet

# when creating diff API routes, we mark them with diff methods: GET; POST; PUT; DELETE (most common ones - there exists others)
"""
GET - used to get some values from server (req data from some specified resource)
POST - used to create something new (creating a resource)
PUT - used to alter/modifiy some existing data (updating a resource)
DELETE - deleting data from some database or resource we accessing from (deleting a resource)

"""

# creating a GET route
@app.route("/get-user/<user_id>") # <user_id> syntax : Path_Param -> dynamic val that can be passed in the path of a URL, that can be accessed inside our root
def get_user(user_id): # the param passed in is the same as the Path_Param passed in decorator
    # defining this func does the following
    # "/get-user/1234" for eg -> GETting the user with the ID of 1234
    # and so we access the Path_Param thru passing it in the func get_user

    # following is exemplar data that can be returned to user
    user_data = {
        "user_id" : user_id,
        "name" : "First Trial",
        "email" : "first.trial@example.com"
    }

    # whenever accessing a root, we can also access a Query_Param, after a '?' symbol
    # Query_Param - extra val  included after main path
    # eg: path - "/get-user/395", then after including the '?' symbol with Query_Param (eg: extra) - "/get-user/123?extra=hello world"
    # "?extra=hello world" is an additional var that can be passed along in the route

    # to be accessed from Flask, do:
    extra = request.args.get("extra") # request is var from import line above; .args stores all Query_Param in a dictionary; .get is use d to access a val like "extra"
    if extra: # checking is "extra" exists
        user_data["extra"] = extra # fetching the "extra" key within user_data defined dictionary, and assigning it the var extra

    what = request.args.get("what")
    if what:
        user_data["what"] = what


    return jsonify(user_data), 200 # we are returning our user_data defined dictionary as a JSON; THEN, returning the response code of 200
# whenever returning data from an API -> we use JSON (JavaScript Object Notation); essentially a collection of key-val pairs (similar to a python dictionary)
# this allows Flask to parse this val and return as JSON data - the JSONify then being returned to user
# other returned val is StatusCode; 200 is default for success (other HTTP status codes can be passed here instead)


# POST req
@app.route("/create-user", methods=["POST"]) # because we are not using the default GET req, we have to specify the accepted method for this route
# means that this endpoint accepts both a POST req
# if wanted to accept more than 1 method, then methods arr would look like so: methods=["POST", "GET"] (to accept the GET req as well
def create_user():
    """
    # to check what method is being used in this func, we can do following

    if request.method == "POST":
        ...
    elif request.method == "GET":
        ...
    etc

    mainly used when the "methods" arr for this decorator has more than 1 method within it
    """

    # want to receive data from the request that is in JSON format
    data = request.get_json()
    # gets all JSON data passed that is in the body of the req


    return jsonify(data), 201

# demonstrates that we have successfully received some JSON data from the user
# more can be done by adding this to a Database

# can't demo in browser, but can demo with other tools: Postman, OpenAPI, etc





if __name__ == "__main__":
    app.run(debug=True) # runs Flask server
# after running this, we get a test server URL, containing the word "Home" as the default root

# the python server has URL: http://127.0.0.1:5000 - localhost (127.0.0.1) , port=5000