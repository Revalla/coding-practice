import pandas as pd
employee = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"]
})
salary = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Salary": [50000, 60000, 55000, 65000]
})
print(employee)
print(salary) 
res=pd.merge(employee,salary,on="EmpID")
print(res)
