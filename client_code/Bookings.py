from ._anvil_designer import BookingsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Bookings(BookingsTemplate):
    def __init__(self, **properties):
    # Set Form properties and Data Bindings.
      self.init_components(**properties)

    def populate_block_dropdown(self):
        """Populate the slot_for_teachers dropdown with available blocks."""
        # Get all blocks that are not booked
        available_blocks = app_tables.slots.search(Booked=False)

        # Add them to the dropdown (show Block name)
        self.slot_for_teachers.items = [
            (block['Block'], block) for block in available_blocks
        ]

        # If no blocks are available, set a placeholder
        if not available_blocks:
            self.slot_for_teachers.placeholder = "No blocks available"

    def slot_for_teachers_change(self, **event_args):
        """Handle changes in the slot_for_teachers dropdown."""
        selected_block = self.slot_for_teachers.selected_value
        if selected_block:
            alert(f"You selected block: {selected_block['Block']}")

    def submit_button_click(self, **event_args):
        """Handle the Submit button click."""
        date = self.date_picker_1.date
        time = self.time_dropdown.selected_value
        teacher_slot = self.slot_for_teachers.selected_value

        if date and time and teacher_slot:
            try:
                # Call the server function to save the booking
                result = anvil.server.call('save_booking', date, time, teacher_slot)
                alert(result, title="Success")
            except Exception as e:
                alert(f"Error saving booking: {e}", title="Error")
        else:
            alert("Please select a date, time, and teacher slot.", title="Error")
