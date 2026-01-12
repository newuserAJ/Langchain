from pydantic import BaseModel, Field,EmailStr
from typing import Optional

class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email: EmailStr
    cgpa: float = Field(ge=0.0, le=10.0)  #cgpa between 0.0 to 10.0
    

#data validation, if set as str only str will be accepted
new_Student={"name":"Adith","age":22,"email":'adithjose@gmail.com',"cgpa":9.5}
student=Student(**new_Student)
print(student)