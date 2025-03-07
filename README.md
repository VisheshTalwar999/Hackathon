README FILE
eWMS (Enterprise Workspace Management System) is a real-time seat allocation system that helps manage employee seating across multiple departments. It ensures optimal seat assignments based on job grades and department constraints, using Flask, MySQL, and OR-Tools Customization Algorithm for optimization.

Features :-
-Automated Seat Allocation using OR-Tools optimization(added many constrains - 1 seat to 1 employee, employees of a department in same floor occupying minimum area, seat allocated based on job-grades, minimum area used by a department)
-Real-time Workspace Map visualization with seat status(showing vacant, occupied, reserved seats of 1 seater, 2 seater, 4 seater, enclosed room, labs using one to one mapping)
-Employee Management (Add, View, Delete)
-Addition of employees results in automatic allocation of seat and that seat is shown occupied in Workspace Map visualization
-Employee Assets Tracking (assets owned by a particular employee)
-Filtering by Site, Department, Sub-department, Floor
-Dynamic Dashboard for Seat Usage Analytics to save time 
-Excel Report Generation for Employees 

Installation & Setup :-
 Prerequisites
- Python 3.8
- MySQL Server
- Flask (framework)

Clone the Repository:-
sh
git clone https://github.com/your-repo/eWMS.git
cd eWMS

•	The server will run on ‘http://127.0.0.1:5000/’


Input & Output Details
Input Data :-
1. Adding an Employee
   - Name, Email, Department, Sub-Department, Job Grade, Site.
   - Example:
   json
   {
       "name": "Alice",
       "email": "alice@example.com",
       "department": "DTIT",
       "sub_department": "DTIT-PLM",
       "job_grade": "JG-9",
       "site": "Greater Noida"
   }
   
2. Seating Information
   - Seat ID, Type (Enclosed Room, Open Cubical), Floor, Department, Sub-Department.

Output :-
1. Workspace Map Updates
   - Occupied Seats → Red
   - Vacant Seats → White
   - Reserved Seats → Grey

2. Database Updates
   - ‘employees’ table stores new employees.
   - ‘seat allocations’ table links employees to their assigned seats.

How to Use the Application :-
1. Add Employees
   - Navigate to ‘Manage Employees’ → Fill the form to add employee.
   - Click "Submit" → Seat automatically allocated (as mapping is done of employee id with seat number).

2. Add Assets
-

2️. View Workspace Map
   - Navigate to ‘Home’ → See real-time seat occupancy of the department you wish to see

3. Download Reports
   - Click ‘Generate Report’ to get an Excel file of employees and their respective seats.

Future Enhancements:-
1.Asset tracking and demand (requirements, available, used assets)
2. On hovering the Workspace Map visualization seat; if vacant, asks if to allocate that to employee; if occupied asks if to vacant the seat and accordingly updates the employee
3. Excel report generated mailed to HR after 15 days so that he can keep track of seats.

