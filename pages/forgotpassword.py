from flet import *
from utils.color import *
class FogotPassword(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.expand = True
        self.alignment = alignment.center
        self.bgcolor = '#3d3d3d'
        self.email_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14, color='#c9c9c9',

                ),
                hint_text='Введите email привязанный к аккаунту',
                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white'
                )
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
                        alignment='center',
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value='Ты точно забыл пароль?',
                                size=22,
                                color='white',
                                font_family='RobotoSlab',
                                text_align='center',
                            ),

                            Text(
                                value='Введите ваш email, для получения дальнейших указаний по восстановлению пароля',
                                size=16,
                                color= p,
                                text_align='center',
                            ),
                            self.email_box,
                            Container(

                                content=Row(
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            bgcolor='#ff00a6',
                                            border_radius=15,
                                            width=40,
                                            height=40,
                                            content=Text(
                                                value='<',
                                                color='white',
                                                size=18,
                                            ),
                                            on_click=lambda _: self.page.go('/login')
                                        ),

                                        Container(
                                            alignment=alignment.center,

                                            bgcolor='#ff00a6',
                                            border_radius=15,
                                            width=370,
                                            height=40,
                                            content=Text(
                                                value='Отправить',
                                                color='white',
                                                size=18,
                                            ),
                                            on_click=self.reset_password,
                                        ),
                                    ]
                                )
                            )



                        ]
                    )
                )
            ]

        )
    def reset_password(self, e):
        pass