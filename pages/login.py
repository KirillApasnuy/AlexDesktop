from flet import *
from utils.color import *
# import flet as ft
class Login(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.padding = 0
        self.alignment = alignment.center
        self.expand = True
        self.bgcolor ='#3d3d3d'
        self.name_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Введите имя и фамилию',
                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white'
                )
            ),
            border_radius=20,
        )
        self.password_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14, color=input_col,

                ),
                hint_text='Введите пароль',
                cursor_color='#c9c9c9',
                text_style=TextStyle(
                    size=16,
                    color='white'
                ),
                password=True,
            ),
            border_radius=20,
        )
        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    padding=40,
                    border_radius=20,
                    bgcolor='#C5007F',
                    content=Column(
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value='Добро пожаловать!',
                                size=20,
                                font_family='RobotoSlab',
                                color='white',
                                text_align='center'
                            ),
                            self.name_box,
                            self.password_box,
                            Container(height=0),

                            Container(
                                alignment=alignment.center,
                                bgcolor= '#ff00a6',
                                border_radius=15,
                                height=40,
                                content=Text(
                                    value='Войти',
                                    color='white',
                                    size=18,
                                ),
                                on_click=self.login
                            ),

                            Container(
                                content=Text(
                                    value='Забыли пароль?',
                                    color='white',
                                    size=16
                                ),
                                on_click=lambda _: self.page.go('/forgotpassword')
                            ),

                            Container(
                                alignment=alignment.center,
                                content=Text(
                                    value='Зарегистрироваться!',
                                    color='white',
                                    size=16
                                ),
                                on_click=lambda _: self.page.go('/singup')
                            ),



                        ]

                    )
                )
            ]
        )

    def login(self, e):
        pass