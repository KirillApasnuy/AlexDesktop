import flet
from flet import *
from pages.login import Login
from pages.singup import Singup
from pages.dashboard import DashBoard
from pages.forgotpassword import FogotPassword
from pages.dashboardPanelPage.news import *
from pages.dashboardPanelPage.individualTask import *
from pages.dashboardPanelPage.quiz import *
from dbmethod.create.crateQuiz import *
from dbmethod.create.createIndividualTask import *

class Main(UserControl):
    def __init__(self, page: Page,):
        super().__init__()
        page.window_full_screen = True
        self.page = page
        self.page.title = 'Alex'
        self.page.margin = 0
        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }
        self.init_helper()

    def init_helper(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/singup')

    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/singup": Singup,
            "/me": DashBoard,
            "/me/news": News,
            "/me/individualtask": IndividualTask,
            "/me/quiz": Quiz,
            "/me/individualtask/create": CreateIndividualTask,
            "/me/quiz/create": CreateQuiz,
            "/forgotpassword": FogotPassword
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )

app(target=Main, assets_dir='assets')

