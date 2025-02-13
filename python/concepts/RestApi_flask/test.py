import requests

response=requests.get("http://localhost:5000/info")
print(response)               # <Response [200]>
print(response.status_code)   # 200
print(response.text)          # {"emp1": {"name": "Radha", "salary": "100k"}, "emp2": {"name": "Krishna", "salary": "8k"}}