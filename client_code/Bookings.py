from ._anvil_designer import BookingsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date, timedelta

class Bookings(BookingsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Initialize the DatePicker
        self.datepicker.max_date = date.today() + timedelta(days=30)

    def populate_block_dropdown(self):
        """Populate the slot_for_teachers dropdown with available blocks."""
        available_blocks = app_tables.slots.search(Booked=False)
        self.slot_for_teachers.items = [(block['Block'], block) for block in available_blocks]
        if not available_blocks:
            self.slot_for_teachers.placeholder = "No blocks available"

    def pick_slot_change(self, **event_args):
        """Handle changes in the slot_for_teachers dropdown."""
        self.confirm_slot_button.enabled = bool(self.start_drop_down.selected_value)

    def submit_button_click(self, **event_args):
        """Handle the Submit button click."""
        self.item['start'] = self.start_drop_down.selected_value
        print(self.item['start'])
        self.content_panel.clear()

    def datepicker_change(self, **event_args):
        """This method is called when the selected date changes"""
        selected_date = self.datepicker.date  # Ensure this matches the component name
        if selected_date:
            day = selected_date.isoformat()
            start_times = self.item['slots_dict_by_day'].get(day, [])
            self.start_drop_down.items = start_times
            self.start_drop_down.enabled = bool(start_times)
            self.start_drop_down.placeholder = 'Pick a slot' if start_times else 'No slots - choose another day'

            # Save the selected date to the bookings table
            app_tables.bookings.add_row(
                date=selected_date,
                user=anvil.users.get_user(),
                created_on=date.today()
            )
        else:
            self.start_drop_down.enabled = False
            self.start_drop_down.placeholder = 'Select a valid date'

    def Special_request_pressed_enter(self, **event_args):
        """Handle the pressed enter event for the Special_request field."""
        pass

class BookingForm(BookingFormTemplate):

    def check_slot_availability(self, day, block):
        # Call server function to check availability
        is_available = anvil.server.call('check_slot_availability', day, block)
        if not is_available:
            alert("This slot is unavailable. Please select another slot.")
        return is_available

    def submit_click(self, **event_args):
        # Validate before submitting
        day = self.day_dropdown.selected_value
        block = self.block_dropdown.selected_value
        
        if self.check_slot_availability(day, block):
            # Proceed with the booking
            anvil.server.call('book_slot', day, block)
            alert("Your booking has been confirmed!")
        else:
            alert("Please select an available slot.")
          
          