from flask import Flask, make_response,jsonify
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
            "All Endpoints" : ["/api/v1/esinfo","/api/v1/esinfo/:ename"]
              }
         return help

class Employess(Resource):
     def get(self,ename=None):
         if ename:
              if ename in employee_info.keys():
                 return make_response(jsonify(employee_info.get(ename)),200)
              else:
                     message={
                      "message" : "Employee_Name not found"
                       }
                     return make_response(jsonify(message),404)
         return make_response(jsonify(employee_info),200)
     
api.add_resource(Help,"/")
api.add_resource(Employess,"/api/v1/esinfo","/api/v1/esinfo/<string:ename>")

app.run(debug=True,port=5000,host="localhost")