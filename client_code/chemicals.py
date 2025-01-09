from ._anvil_designer import chemicalsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class chemicals(chemicalsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

class ChemicalsPage(ChemicalsPageTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Initialize the repeating panel with data from the database
        self.repeating_panel_1.items = app_tables.chemicals.search()
        
        # Add event handlers for update and delete buttons
        self.repeating_panel_1.set_event_handler('x-update-chemical', self.update_chemical)
        self.repeating_panel_1.set_event_handler('x-delete-chemical', self.delete_chemical)

    def add_chemical_click(self, **event_args):
        """This function is called when the Add Chemical button is clicked"""
        item = {}
        editing_form = ChemicalEdit(item=item)  # Use a form to edit chemical details
        if alert(content=editing_form, large=True, buttons=[("Save", True), ("Cancel", False)]):
            anvil.server.call('add_chemical', item)  # Call server function to add chemical
            self.repeating_panel_1.items = app_tables.chemicals.search()  # Refresh the data

    def update_chemical(self, chemical, **event_args):
        """This function is called when the Update button is clicked"""
        item = dict(chemical)
        editing_form = ChemicalEdit(item=item)
        if alert(content=editing_form, large=True, buttons=[("Save", True), ("Cancel", False)]):
            anvil.server.call('update_chemical', item)  # Call server function to update
            self.repeating_panel_1.items = app_tables.chemicals.search()  # Refresh the data

    def delete_chemical(self, chemical, **event_args):
        """This function is called when the Delete button is clicked"""
        if confirm(f"Do you really want to delete the chemical {chemical['chemical_name']}?"):
            anvil.server.call('delete_chemical', chemical)  # Call server function to delete
            self.repeating_panel_1.items = app_tables.chemicals.search()  # Refresh the data
