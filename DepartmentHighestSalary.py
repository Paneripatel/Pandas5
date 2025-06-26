'''
Pandas5

1 Problem 1 : Department Highest Salary (https://leetcode.com/problems/department-highest-salary/ )
'''

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rnk'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending = False)
    employee = employee[employee['rnk']==1]
    employee = employee.merge(department, left_on='departmentId', right_on='id')
    return employee[['name_y', 'name_x', 'salary']].rename(columns={'name_y':'Department', 'name_x':'Employee', 'salary':'Salary'})