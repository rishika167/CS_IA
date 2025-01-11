from ._anvil_designer import AdminPagelandingTemplate
from anvil import *
import anvil.users
import anvil.server
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
    open_form('Add_User')

  def apparatus_page_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('appratus')

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('addSlot')

  def bookings_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Bookings')
    

  def chemicals_page_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('chemicals')

  def Sign_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_in')

  def Back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AdminPagelanding')
    pass
    
