from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

class Info(Resource):
      def __init__(self):
             #  print(request) # <Request 'http://127.0.0.1:5000/info' [GET]> #<Request 'http://127.0.0.1:5000/info' [POST]>
             #  print(dir(request))
             #  print(request)
             print(request.authorization)
             print(request.args)
      def get(self):
            print("get method is executed")
      def post(self):
            pass

api.add_resource(Info,"/info")
app.run(debug=True)

# curl -i -u any_user:pass_user  -X GET http://127.0.0.1:5000/info?id=5