from ._anvil_designer import chemicals_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class chemicals_add(chemicals_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def Back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('chemicals')

  def Sign_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_in')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.clear()
    pass
