from .ui import UI
from .controller import Controller

CONTROLLER = Controller(4, 10)
UI = UI(600, 800, CONTROLLER)

UI.run()
