import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def save_booking(date, time):
    # Save the booking to the database
    app_tables.bookings.add_row(
        booking_date=date,
        booking_time=time,
        created=datetime.now()
    )
    return "Booking successfully saved!"

@anvil.server.callable
def add_feedback(name, email, feedback):
    app_tables.feedback.add_row(
        name=name, 
        email=email, 
        feedback=feedback, 
        created=datetime.now()
    )
    # Send yourself an email each time feedback is submitted
    anvil.email.send(
        to="rishika.k1697@gmail.com",  # Change this to your email address
        subject="Request {}".format(name),
        text=f"""
    A new request has been sent!

    Date: {datetime.now().strftime('%Y-%m-%d')}
    Time: {{}}
    """
    )

@anvil.server.callable
def mark_slot_unavailable(day, block):
    # Update slot availability in the database
    app_tables.slots.get(day=day, block=block)['available'] = False
    
    # Fetch all users with bookings for this slot
    affected_bookings = app_tables.bookings.search(day=day, block=block)
    affected_users = {booking['user'] for booking in affected_bookings}
    
    # Notify affected users
    for user in affected_users:
        send_notification(user['email'], day, block)

def send_notification(email, day, block):
    # Email notification example
    anvil.email.send(
        to=email,
        subject="Slot Unavailable Notification",
        text=f"The slot on {day}, Block {block} is no longer available. Please choose another time."
    )
@anvil.server.callable
def check_slot_availability(day, block):
    slot = app_tables.slots.get(day=day, block=block)
    return slot['available'] if slot else False
  import anvil.tables as tables
from anvil.tables import app_tables

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def update_chemical(chemical, chemical_data):
    """
    Update an existing chemical record.
    """
    if chemical_data['chemical_name'] and chemical_data['quantity'] is not None and chemical_data['units'] and chemical_data['critical_stock_level'] is not None:
        chemical.update(**chemical_data)

@anvil.server.callable
def add_chemical(chemical_data):
    """
    Add a new chemical to the database.
    """
    if chemical_data['chemical_name'] and chemical_data['quantity'] is not None and chemical_data['units'] and chemical_data['critical_stock_level'] is not None:
        app_tables.chemicals.add_row(**chemical_data)

@anvil.server.callable
def delete_chemical(chemical):
    """
    Delete a chemical from the database.
    """
    chemical.delete()
