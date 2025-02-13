from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

employee_info ={
              "Radha": {
              "salary": "100k",
              "Technology": "Linux Admin"
                },
              "Krishnan": {
              "salary":"8k",
              "Technology": "Web Developer",
               }
             }

class Help(Resource):
     def get(self):
         help={
            "All Endpoints" : ["/esinfo","/einfo/:ename"]
              }
         return help

class Employess(Resource):
     def get(self):
         return employee_info

class Emloyee(Resource):
      def get(self,ename):
           return employee_info.get(ename)

api.add_resource(Help,"/")
api.add_resource(Employess,"/esinfo")
api.add_resource(Emloyee,"/einfo/<string:ename>")

app.run(port=5000,host="localhost")