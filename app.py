# from flet import ft
from flet import *
from pages.login import Login
from pages.singup import Singup
from pages.dashboard import DashBoard
from pages.forgotpassword import FogotPassword


class Main(UserControl):
    def __init__(self, page: Page,):
        super().__init__()
        self.page = page
        page.fonts = {
            "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
        }
        self.init_helper()

    def init_helper(self,):
        self.page.on_route_change = self.on_route_change
        self.page.go('/me')

    def on_route_change(self, route):
        new_page = {
            "/login": Login,
            "/singup": Singup,
            "/me": DashBoard,
            "/forgotpassword": FogotPassword
        }[self.page.route](self.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )

app(target=Main, assets_dir='assets', view=WEB_BROWSER)

