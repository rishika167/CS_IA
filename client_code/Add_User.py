from ._anvil_designer import Add_UserTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Add_User(Add_UserTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def user_id_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def Back_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('AdminPagelanding')

  def Sign_out_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_in')
