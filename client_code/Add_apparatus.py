from ._anvil_designer import Add_apparatusTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Add_apparatus(Add_apparatusTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.repeating_panel_1.items = app_tables.chemicals.search()

  def Back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AdminPagelanding')

  def Sign_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_in')

  def repeating_panel_1_show(self, **event_args):
    """This method is called when the repeating panel is shown on the screen"""
    pass
