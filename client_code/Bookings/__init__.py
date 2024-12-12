from ._anvil_designer import BookingsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Bookings(BookingsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        
        # Populate time dropdown
        self.time_dropdown = [("8:00-9:00", "8:00-9:00"), 
                              ("9:00-10:00", "9:00-10:00"), 
                              ("10:00-11:00", "10:00-11:00")]

    def submit_button_click(self, **event_args):
        "Handle the Submit button click."
        date = self.date_picker_1.date
        time = self.drop_down_1.selected_value
        
        if date and time:
            try:
                # Call the server function to save the booking
                result = anvil.server.call('save_booking', date, time)
                alert(result, title="Success")
            except Exception as e:
                alert(f"Error saving booking: {e}", title="Error")
        else:
            alert("Please select both a date and a time.", title="Error")

    def drop_down_1_change(self, **event_args):
      """This method is called when an item is selected"""
      pass

    def date_picker_1_change(self, **event_args):
      """This method is called when the selected date changes"""
      pass

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass
