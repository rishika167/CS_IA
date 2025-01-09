from ._anvil_designer import MovieListTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Movie import Movie

class MovieList(MovieListTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        self.repeating_panel_1.items = app_tables.movies.search()
        self.repeating_panel_1.add_event_handler('x-edit-movie', self.edit_movie)
        self.repeating_panel_1.add_event_handler('x-delete-movie', self.delete_movie)

    def edit_click(self, **event_args):
        item = dict(self.item)
        editing_form = MovieEdit(item=item)
        alert(content=editing_form, large=True)
        anvil.server.call('update_movie', item)
        self.item = app_tables.movies.search()[0]
        self.refresh_data_bindings()

    def add_movie_click(self, **event_args):
        item = {}
        editing_form = MovieEdit(item=item)
        alert(content=editing_form, large=True)
        anvil.server.call('add_movie', item)
        self.repeating_panel_1.items = app_tables.movies.search()
        
    def edit_movie(self, movie, **event_args):
        item = dict(movie)
        editing_form = MovieEdit(item=item)
        alert(content=editing_form, large=True)
        anvil.server.call('update_movie', movie, item)
        self.repeating_panel_1.items = app_tables.movies.search()

    def delete_movie(self, movie, **event_args):
        if confirm(f"Do you really want to delete the movie {movie['movie_name']}?"):
            anvil.server.call('delete_movie', movie)
            self.repeating_panel_1.items = app_tables.movies.search()

      