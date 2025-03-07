import pandas as pd
from app import db
from app.models import Employee
from sqlalchemy.orm import load_only

def export_to_excel():
    # Fetch employees from the database
    employees = db.session.query(Employee).options(
        load_only(Employee.Name, Employee.Email, Employee.Department, Employee.Sub_Department, Employee.Job_Grade, Employee.Site)
    ).all()

    # Convert to list of dictionaries
    employee_data = [
        {
            "Name": emp.Name,
            "Email": emp.Email,
            "Department": emp.Department,
            "Sub-Department": emp.Sub_Department,
            "Job Grade": emp.Job_Grade,
            "Site": emp.Site
        }
        for emp in employees
    ]

    # Create DataFrame and export to Excel
    df = pd.DataFrame(employee_data)
    excel_path = "employee_list.xlsx"
    df.to_excel(excel_path, index=False)

    print(f"Excel file saved: {excel_path}")

if __name__ == "__main__":
    export_to_excel()
