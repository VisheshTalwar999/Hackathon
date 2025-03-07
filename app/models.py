# app/models.py
from . import db

# class Employee(db.Model):
#     __tablename__ = 'employees'
#     EmployeeID = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String(255), nullable=False)
#     Email = db.Column(db.String(255), nullable=False)
#     Department = db.Column(db.String(255), nullable=False)

#     def to_dict(self):
#         return {
#             'EmployeeID': self.EmployeeID,
#             'Name': self.Name,
#             'Email': self.Email,
#             'Department': self.Department
        # }

# class Seat(db.Model):
#     # __tablename__ = 'seats'
#     # SeatID = db.Column(db.Integer, primary_key=True)
#     # Location = db.Column(db.String(255), nullable=False)
#     # Type = db.Column(db.String(50), nullable=False)
#     # Status = db.Column(db.String(50), nullable=False)
#     SeatID = db.Column(db.Integer, primary_key=True)
#     Location = db.Column(db.String(255), nullable=False)
#     SeatType = db.Column(db.String(50), nullable=False)
#     AreaType = db.Column(db.String(50), nullable=False)
#     SeatStatus = db.Column(db.String(50), nullable=False)
#     LastUpdated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

#     def __init__(self,SeatID, Location, SeatType, AreaType, SeatStatus):
#         self.SeatID = SeatID
#         self.Location = Location
#         self.SeatType = SeatType
#         self.AreaType = AreaType
#         self.SeatStatus = SeatStatus

#     # def to_dict(self):
#     #     return {
#     #         'SeatID': self.SeatID,
#     #         'Location': self.Location,
#     #         'Type': self.Type,
#     #         'Status': self.Status
#     #     } 



class Seat(db.Model):
    __tablename__ = 'seats'
    SeatID = db.Column(db.Integer, primary_key=True)
    Location = db.Column(db.String(255), nullable=False)
    SeatType = db.Column(db.String(50), nullable=False)
    AreaType = db.Column(db.String(50), nullable=False)
    SeatStatus = db.Column(db.String(50), nullable=False)
    LastUpdated = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, SeatID, Location, SeatType, AreaType, SeatStatus):
        self.SeatID = SeatID
        self.Location = Location
        self.SeatType = SeatType
        self.AreaType = AreaType
        self.SeatStatus = SeatStatus

    def to_dict(self):
        return {
            'SeatID': self.SeatID,
            'Location': self.Location,
            'SeatType': self.SeatType,
            'AreaType': self.AreaType,
            'SeatStatus': self.SeatStatus,
            'LastUpdated': self.LastUpdated
        }
    

class Employee(db.Model):
    __tablename__ = 'employees'

    EmployeeID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False, unique=True)
    Department = db.Column(db.String(255), nullable=False)
    SubDepartment = db.Column(db.String(255), nullable=True)
    DeptManager = db.Column(db.String(255), nullable=True)
    SubDeptManager = db.Column(db.String(255), nullable=True)
    DeptAdministrators = db.Column(db.String(255), nullable=True)
    StaffCategory = db.Column(db.Enum('Employee', 'Intern', 'SubCon'), nullable=False)
    JobGrade = db.Column(db.String(50), nullable=False)
    Site = db.Column(db.String(255), nullable=False)
    LaptopAssetNumber = db.Column(db.String(255), nullable=True)
    LaptopSerialNumber = db.Column(db.String(255), nullable=True)
    MonitorAssetNumber = db.Column(db.String(255), nullable=True)
    MonitorSerialNumber = db.Column(db.String(255), nullable=True)
    DesktopAssetNumber = db.Column(db.String(255), nullable=True)
    DesktopSerialNumber = db.Column(db.String(255), nullable=True)

    def __init__(self, EmployeeID,Name, Email, Department, JobGrade, Site, SubDepartment=None, DeptManager=None, SubDeptManager=None,
                 DeptAdministrators=None, StaffCategory='Employee', LaptopAssetNumber=None,
                 LaptopSerialNumber=None, MonitorAssetNumber=None, MonitorSerialNumber=None,
                 DesktopAssetNumber=None, DesktopSerialNumber=None):
        self.EmployeeID=EmployeeID
        self.Name = Name
        self.Email = Email
        self.Department = Department
        self.SubDepartment = SubDepartment
        self.DeptManager = DeptManager
        self.SubDeptManager = SubDeptManager
        self.DeptAdministrators = DeptAdministrators
        self.StaffCategory = StaffCategory
        self.JobGrade = JobGrade
        self.Site = Site
        self.LaptopAssetNumber = LaptopAssetNumber
        self.LaptopSerialNumber = LaptopSerialNumber
        self.MonitorAssetNumber = MonitorAssetNumber
        self.MonitorSerialNumber = MonitorSerialNumber
        self.DesktopAssetNumber = DesktopAssetNumber
        self.DesktopSerialNumber = DesktopSerialNumber

    def to_dict(self):
        return {
            'EmployeeID': self.EmployeeID,
            'Name': self.Name,
            'Email': self.Email,
            'Department': self.Department,
            'SubDepartment': self.SubDepartment,
            'DeptManager': self.DeptManager,
            'SubDeptManager': self.SubDeptManager,
            'DeptAdministrators': self.DeptAdministrators,
            'StaffCategory': self.StaffCategory,
            'JobGrade': self.JobGrade,
            'Site': self.Site,
            'LaptopAssetNumber': self.LaptopAssetNumber,
            'LaptopSerialNumber': self.LaptopSerialNumber,
            'MonitorAssetNumber': self.MonitorAssetNumber,
            'MonitorSerialNumber': self.MonitorSerialNumber,
            'DesktopAssetNumber': self.DesktopAssetNumber,
            'DesktopSerialNumber': self.DesktopSerialNumber
        }


class SeatAllocation(db.Model):
    __tablename__ = 'seat_allocations'
    AllocationID = db.Column(db.Integer, primary_key=True)
    SeatID = db.Column(db.Integer, nullable=False)
    EmployeeID = db.Column(db.Integer, nullable=False)
    AllocationDate = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    Status = db.Column(db.Enum('Active', 'Expired', 'Pending'), nullable=False)

    def __init__(self, AllocationID,SeatID, EmployeeID, AllocationDate, Status):
        self.AllocationID = AllocationID
        self.SeatID = SeatID
        self.EmployeeID = EmployeeID
        self.AllocationDate = AllocationDate
        self.Status = Status


    def to_dict(self):
        return {
            'AllocationID': self.EmployeeID,
            'SeatID': self.SeatID,
            'EmployeeID': self.EmployeeID,
            'AllocationDate': self.AllocationDate,
            'Status': self.Status         
        }