#How to pass URL Parameters(variables) to the destination URL?
#http://yourapi.com/esinfo?ename=1 
#Passing multiple query parameter:-
#"http://yourapi.com/esinfo?ename=abc&id=4"

from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

employee_info ={
              "Radha": {
              "salary": "100k",
              "Technology": "Linux Admin"
                },
              "Krishnan": {
              "salary":"10k",
              "Technology": "Web Developer",
               }
             }

class Help(Resource):
     def get(self):
         help={
            "All Endpoints" : ["/api/v1/esinfo"]
              }
         return help

class Employess(Resource):
     def get(self):
         #  print(request.args.get("ename"))
         if request.args:
              if "ename" not in request.args.keys():
                    message={
                         "message": "Use only ename as query parameter",
                         "help" : "/esinfo?ename=<your_emp_name>"
                    }
                    return message
              if (request.args.get("ename")) in employee_info.keys():
                   return make_response(jsonify(employee_info.get(request.args.get("ename"))),200)
              return make_response(jsonify(f"Didn't found {request.args.get("ename")} info in our Database"),404)
         return make_response(jsonify(employee_info),200)
     
api.add_resource(Help,"/")
api.add_resource(Employess,"/api/v1/esinfo")

app.run(debug=True,port=5000,host="localhost")