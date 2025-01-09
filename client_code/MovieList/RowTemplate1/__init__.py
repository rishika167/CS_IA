from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def edit_row_click(self, **event_args):
        self.parent.raise_event('x-edit-movie', movie=self.item)

    def delete_row_click(self, **event_args):
        self.parent.raise_event('x-delete-movie', movie=self.item)

