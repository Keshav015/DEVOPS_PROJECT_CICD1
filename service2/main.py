from fastapi import FastAPI
from database import SessionLocal
from model import Employee
app = FastAPI()

@app.post("/add")
def add_item(name:str, age: int, department:str, salary:int):    
     db = SessionLocal()
     try:
          employee = Employee( name = name, age = age, department = department, salary = salary)    
          db.add(employee)
          db.commit()
          db.refresh(employee)
          return {"message":"Employee added successfully", "Employee_ID":employee.id}
     finally:
         db.close()


@app.get("/data")
def get_data():
     db = SessionLocal()
     try:
          employee =db.query(Employee).all()
          return {
               "employee":[{"id":i.id,"name":i.name,"age":i.age,"department":i.department,"salary":i.salary} for i in employee]
          }
     finally:
          db.close()