# app/services/seat_service.py
from ..models import Seat

def create_seat(data):
    seat = Seat(
        Location=data['location'],
        Type=data['type'],
        Status=data['status']
    )
    return seat

def delete_seat(seat_id):
    seat = Seat.query.get_or_404(seat_id)
    return seat