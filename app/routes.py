# app/routes.py
# from flask import jsonify, request, render_template
# from . import db
# from .models import Employee, Seat
# from flask import send_file
# import pandas as pd
# from io import BytesIO
# from app.models import Employee
# from app import db
# from sqlalchemy.orm import load_only

# def init_routes(app):




    # app/routes.py
from flask import jsonify, request, render_template, redirect, url_for, session, flash
from . import db
from .models import Employee, Seat, SeatAllocation
from flask import send_file
import pandas as pd
from io import BytesIO
from app.models import Employee
from app import db
from sqlalchemy.orm import load_only
from flask import Flask
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session handling

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def init_routes(app):
    # Dummy users for testing (Replace with DB authentication)
    users = {
        "admin@example.com": "password123",
        "user@example.com": "userpass"
    } 

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login', methods=['POST'])
    def login():
        email = request.form.get('email')
        password = request.form.get('password')
        logging.debug(f"Login attempt with email: {email}") 

        if email in users and users[email] == password:
            session['user'] = email  # Store user session
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password", "error")
            return redirect(url_for('index')) 
    
    @app.route('/home')
    def home():
        if 'user' not in session:
            flash("Please log in first", "error")
            return redirect(url_for('index'))  # Redirect if not logged in
        return render_template('Home.html')  # Serve home page only if logged in
    
    @app.route('/logout')
    def logout():
        session.pop('user', None)  # Clear user session
        flash("Logged out successfully", "success")
        return redirect(url_for('index'))

    @app.route('/allocate_seat')  # Route for managing seats
    def allocate_seat():  # Unique function name
        return render_template('/allocate_seat.html')
   
    
    @app.route('/apiallocate_seat_add')
    def allocate_seat_list():
        employees = Employee.query.all()  # Fetch all employees
        return render_template('/allocate_seat_add.html', employees=employees)
    
    @app.route('/api/seat_allocations', methods=['GET'])
    def get_seat_allocations():
        seat_allocations = SeatAllocation.query.all()
        seat_allocations_list = [
            {
                'AllocationID': allocation.AllocationID,
                'SeatID': allocation.SeatID,
                'EmployeeID': allocation.EmployeeID,
                'AllocationDate': allocation.AllocationDate.strftime('%Y-%m-%d %H:%M:%S'),
                'Status': allocation.Status
            }
            for allocation in seat_allocations
        ]
        return jsonify(seat_allocations_list)

    
    @app.route('/employee_list')
    def employee_list():
        employees = Employee.query.all()  # Fetch all employees
        return render_template('employee_list.html', employees=employees)
    
    @app.route('/manage_employees')  # Add this route
    def dashboard():
        return render_template('manage_employees.html')
    
    @app.route('/manage_seats')  # Route for managing seats
    def manage_seats():  # Unique function name
        return render_template('manage_seats.html')
    
    @app.route('/assests')  # Route for managing seats
    def assests():  # Unique function name
        return render_template('assests.html')
    
    

    @app.route('/api/dashboard/metrics', methods=['GET'])
    def get_dashboard_metrics():
        total_employees = Employee.query.count()
        total_seats = Seat.query.count()
        occupied_seats = Seat.query.filter_by(SeatStatus='Occupied').count()
        vacant_seats = total_seats - occupied_seats

        return jsonify({
            'totalEmployees': total_employees,
            'totalSeats': total_seats,
            'occupiedSeats': occupied_seats,
            'vacantSeats': vacant_seats
        })

    @app.route('/api/employees', methods=['GET'])
    def get_employees():
        employees = Employee.query.all()
        return jsonify([employee.to_dict() for employee in employees])
    
    


    @app.route('/api/employees', methods=['POST'])
    def allocate_seat_add():
        data = request.get_json()

        # Validate required fields
        required_fields = ['AllocationID', 'SeatID', 'EmployeeID', 'AllocationDate', 'Status']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400

        # Create a new employee
        new_allocate_seat = SeatAllocation(
            AllocationID=data['AllocationID'],
            SeatID=data['SeatID'],
            EmployeeID=data['EmployeeID'],
            AllocationDate=data['AllocationDate'],
            Status=data.get('Status')
           
        )

        db.session.add(new_allocate_seat)
        db.session.commit()

        return jsonify(new_allocate_seat.to_dict()), 201


    @app.route('/api/employees', methods=['POST'])
    def add_employee():
        data = request.get_json()

        # Validate required fields
        required_fields = ['Name', 'Email', 'Department', 'JobGrade', 'Site', 'StaffCategory']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'{field} is required'}), 400

        # Create a new employee
        new_employee = Employee(
            EmployeeID=data['EmployeeID'],
            Name=data['Name'],
            Email=data['Email'],
            Department=data['Department'],
            SubDepartment=data.get('SubDepartment'),
            DeptManager=data.get('DeptManager'),
            SubDeptManager=data.get('SubDeptManager'),
            DeptAdministrators=data.get('DeptAdministrators'),
            StaffCategory=data['StaffCategory'],
            JobGrade=data['JobGrade'],
            Site=data['Site'],
            LaptopAssetNumber=data.get('LaptopAssetNumber'),
            LaptopSerialNumber=data.get('LaptopSerialNumber'),
            MonitorAssetNumber=data.get('MonitorAssetNumber'),
            MonitorSerialNumber=data.get('MonitorSerialNumber'),
            DesktopAssetNumber=data.get('DesktopAssetNumber'),
            DesktopSerialNumber=data.get('DesktopSerialNumber')
        )

        db.session.add(new_employee)
        db.session.commit()

        return jsonify(new_employee.to_dict()), 201

    @app.route('/api/employees/<int:employee_id>', methods=['DELETE'])
    def delete_employee(employee_id):
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully'}), 200

    @app.route('/api/seats', methods=['GET'])
    def get_seats():
        seats = Seat.query.all()
        seats_list = [
            {
                'SeatID': seat.SeatID,
                'Location': seat.Location,
                'SeatType': seat.SeatType,
                'AreaType': seat.AreaType,
                'SeatStatus': seat.SeatStatus,
                'LastUpdated': seat.LastUpdated
            }
            for seat in seats
        ]
        return jsonify(seats_list)

    @app.route('/api/seats', methods=['POST'])
    def add_seat():
        data = request.get_json()
        new_seat = Seat(
            SeatID=data['SeatID'],  # Ensure SeatID is included
            Location=data['Location'],
            SeatType=data['SeatType'],
            AreaType=data['AreaType'],
            SeatStatus=data['SeatStatus']
        )
        db.session.add(new_seat)
        db.session.commit()
        return jsonify({'message': 'Seat added successfully'}), 201

    @app.route('/api/seats/<int:seat_id>', methods=['DELETE'])
    def delete_seat(seat_id):
        seat = Seat.query.get_or_404(seat_id)
        db.session.delete(seat)
        db.session.commit()
        return jsonify({'message': 'Seat deleted successfully'}), 200
    

    @app.route('/api/employees/<int:employee_id>', methods=['PUT'])
    def update_employee(employee_id):
        employee = Employee.query.get_or_404(employee_id)
        data = request.get_json()

        # Update employee fields
        employee.Name = data.get('Name', employee.Name)
        employee.Email = data.get('Email', employee.Email)
        employee.Department = data.get('Department', employee.Department)
        employee.SubDepartment = data.get('SubDepartment', employee.SubDepartment)
        employee.DeptManager = data.get('DeptManager', employee.DeptManager)
        employee.SubDeptManager = data.get('SubDeptManager', employee.SubDeptManager)
        employee.DeptAdministrators = data.get('DeptAdministrators', employee.DeptAdministrators)
        employee.StaffCategory = data.get('StaffCategory', employee.StaffCategory)
        employee.JobGrade = data.get('JobGrade', employee.JobGrade)
        employee.Site = data.get('Site', employee.Site)
        employee.LaptopAssetNumber = data.get('LaptopAssetNumber', employee.LaptopAssetNumber)
        employee.LaptopSerialNumber = data.get('LaptopSerialNumber', employee.LaptopSerialNumber)
        employee.MonitorAssetNumber = data.get('MonitorAssetNumber', employee.MonitorAssetNumber)
        employee.MonitorSerialNumber = data.get('MonitorSerialNumber', employee.MonitorSerialNumber)
        employee.DesktopAssetNumber = data.get('DesktopAssetNumber', employee.DesktopAssetNumber)
        employee.DesktopSerialNumber = data.get('DesktopSerialNumber', employee.DesktopSerialNumber)

        db.session.commit()
        return jsonify(employee.to_dict()), 200
    
    
   


    @app.route("/generate_report")
    def generate_report():
        # Fetch employees from the database
        employees = db.session.query(Employee).options(
           load_only(Employee.Name, Employee.Email, Employee.Department, Employee.SubDepartment, Employee.JobGrade, Employee.Site)
        ).all()

        # Convert to list of dictionaries
        employee_data = [
            {
                "Name": emp.Name,
                "Email": emp.Email,
                "Department": emp.Department,
                "Sub-Department": emp.SubDepartment,
                "Job Grade": emp.JobGrade,
                "Site": emp.Site
            }
            for emp in employees
        ]

        # Create a Pandas DataFrame
        df = pd.DataFrame(employee_data)

        # Save the Excel file to memory
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        
        output.seek(0)

        # Send file as a response
        return send_file(output, as_attachment=True, download_name="employee_list.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
