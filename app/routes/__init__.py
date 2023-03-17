# pages need to be called in on both init__.py files
# in route folders and the app folder
from .home import bp as home
from .dashboard import bp as dashboard