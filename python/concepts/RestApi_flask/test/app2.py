from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app) 

'''
> creating endpoints : > / :- for help
                       > /ping :- for status of REST API
                       > /info :- for employee-info
'''
class Help(Resource):
    def get(self):
         help={
            "Available REST APIs are" : ["/ping","/info"]
            }
         return help

class Ping(Resource):
         def get(self):
             status = {
                "status" : "Alive"  
              }
             return status
    
class Employee(Resource):
      def get(self):
             employee_info ={
              "emp1": {
              "name": "Radha",
              "salary": "100k"
              },
              "emp2": {
              "name":"Krishna",
              "salary":"8k"
              }
             }
             return employee_info

# Inhereting Resource class to our classes; automatically endpoint will map to our perticular class.
# But we need to add endponits information to api(object).
api.add_resource(Help,"/")
api.add_resource(Ping,"/ping")
api.add_resource(Employee,"/info")

app.run(port=5000,host="localhost") 