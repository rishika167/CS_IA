from ._anvil_designer import addSlotTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class addSlot(addSlotTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def drop_down_2_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def Back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AdminPagelanding')

  def Sign_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_in')
