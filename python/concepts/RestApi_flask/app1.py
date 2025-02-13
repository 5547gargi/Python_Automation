from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)

employee_info={
     "emp1": {
          "name": "Radha",
          "salary": "100k"
     },
     "emp2": {
        "name":"Krishna",
        "salary":"8k"
     }
}

class Employee(Resource):
     def get(self):
         return employee_info
     
api.add_resource(Employee, "/info")
app.run(port=5000,host="localhost")