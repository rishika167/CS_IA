from ._anvil_designer import AdminPagelandingTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AdminPagelanding(AdminPagelandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def add_user_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def apparatus_page_click(self, **event_args):
    """This method is called when the button is clicked"""
    form1 = 
    open_form(form1)
    
