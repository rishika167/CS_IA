import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )
  # Send yourself an email each time feedback is submitted
  anvil.email.send(to="rishika.k1697@gmail.com", # Change this to your email address
                   subject="Request {}".format(name),
                   text="""
  A new request has been sent!

  Date: {}
  Time: {}
  

