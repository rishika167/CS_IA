from ._anvil_designer import Log_inTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Log_in(Log_inTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def sign_in_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
