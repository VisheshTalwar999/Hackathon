document.getElementById('addEmployeeForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const employee = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        department: document.getElementById('department').value
    };

    // Send data to the backend
    fetch('/api/employees', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(employee)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Employee Added:', data);
        alert('Employee added successfully!');
        // Clear form
        e.target.reset();
        // Refresh the employee list
        fetchEmployees();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to add employee. Please try again.');
    });
});

// Function to fetch and display employees
function fetchEmployees() {
    fetch('/api/employees')
        .then(response => response.json())
        .then(data => {
            const employeeList = document.getElementById('employeeList');
            employeeList.innerHTML = ''; // Clear existing rows
            data.forEach(employee => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${employee.EmployeeID}</td>
                    <td>${employee.Name}</td>
                    <td>${employee.Email}</td>
                    <td>${employee.Department}</td>
                    <td>
                        <button class="btn btn-sm btn-warning">Edit</button>
                        <button class="btn btn-sm btn-danger">Delete</button>
                    </td>
                `;
                employeeList.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Fetch employees on page load
document.addEventListener('DOMContentLoaded', fetchEmployees);

document.getElementById('addSeatForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const seat = {
        location: document.getElementById('location').value,
        type: document.getElementById('type').value,
        status: document.getElementById('status').value
    };

    // Send data to the backend
    fetch('/api/seats', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(seat)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Seat Added:', data);
        alert('Seat added successfully!');
        // Clear form
        e.target.reset();
        // Refresh the seat list
        fetchSeats();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to add seat. Please try again.');
    });
});

// Function to fetch and display seats
function fetchSeats() {
    fetch('/api/seats')
        .then(response => response.json())
        .then(data => {
            const seatList = document.getElementById('seatList');
            seatList.innerHTML = ''; // Clear existing rows
            data.forEach(seat => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${seat.SeatID}</td>
                    <td>${seat.Location}</td>
                    <td>${seat.Type}</td>
                    <td>${seat.Status}</td>
                    <td>
                        <button class="btn btn-sm btn-warning">Edit</button>
                        <button class="btn btn-sm btn-danger">Delete</button>
                    </td>
                `;
                seatList.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Fetch seats on page load
document.addEventListener('DOMContentLoaded', fetchSeats);

// Delete Employee
document.getElementById('employeeList').addEventListener('click', function (e) {
    if (e.target.classList.contains('btn-danger')) {
        const employeeId = e.target.closest('tr').querySelector('td').innerText;
        fetch(`/api/employees/${employeeId}`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    alert('Employee deleted successfully!');
                    fetchEmployees(); // Refresh the list
                } else {
                    alert('Failed to delete employee.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});

// Delete Seat
document.getElementById('seatList').addEventListener('click', function (e) {
    if (e.target.classList.contains('btn-danger')) {
        const seatId = e.target.closest('tr').querySelector('td').innerText;
        fetch(`/api/seats/${seatId}`, { method: 'DELETE' })
            .then(response => {
                if (response.ok) {
                    alert('Seat deleted successfully!');
                    fetchSeats(); // Refresh the list
                } else {
                    alert('Failed to delete seat.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
});