from flet import *

class DashBoard(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.expand = True
        self.bgcolor = 'blue'