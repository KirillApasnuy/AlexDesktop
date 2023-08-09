from flet import *
from utils.color import *
class DashBoard(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.expand = True
        self.bgcolor = bgc,

        self.content = Row(
            spacing=0,
            controls=[
                Container(
                    width=220,
                    bgcolor='#C5007F',
                    padding=padding.only(top=20, left=10, right=10),

                    content=Column(
                        controls=[
                            Row(
                                controls=[
                                    Icon(
                                        icons.PERSON,
                                        size=50,
                                        color='white'
                                    )

                                ]
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='dashboard',
                                    size=16,
                                    color='white',
                                    font_family='RobotoSlab',

                                )
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='utilitues',
                                    size=16,
                                    color='white',
                                    font_family='RobotoSlab',
                                )
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            # Row(
                            #     alignment='center',
                            #     controls=[
                            #         Container(
                            #             alignment=alignment.center,
                            #             height=35,
                            #             width=35,
                            #             bgcolor='white',
                            #             border_radius= 20,
                            #             content=Icon(
                            #                 icons.ARROW_BACK_IOS_SHARP,
                            #                 color='black',
                            #                 size=15,
                            #             )
                            #
                            #         )
                            #     ]
                            # )
                            Container(
                                height=100,
                                bgcolor='#f09',
                                border_radius=5,
                                alignment=alignment.bottom_center,
                                content=Column(
                                    horizontal_alignment='center',
                                    alignment='center',
                                    controls=[
                                        # Text(
                                        #     value='Занимался дизайном: БК',
                                        #     text_align='center',
                                        #     color='white',
                                        # ),
                                        Container(
                                            on_click=lambda _: self.page.go('/login'),
                                            alignment=alignment.center,
                                            height=35,
                                            width=110,
                                            border_radius=5,
                                            bgcolor='#ff1ca4',
                                            content=Text(
                                                value='Log out',
                                                color='white',
                                                size=14,
                                                font_family='RobotoSlab',
                                            )
                                        )

                                    ]
                                )
                            )
                        ]
                    )

                ),
                Container(
                    expand=True,
                    bgcolor=bgc,
                    content=Column(
                        expand=True,
                        controls=[

                            Container(
                                height=70,
                                shadow=BoxShadow(
                                    spread_radius=2,
                                    color=bgc
                                ),
                                padding=padding.only(top=10, bottom=10, right=10, left=32),
                                bgcolor=bgc,
                                content=Row(
                                    alignment='spaceBetween',
                                    controls=[
                                        Row(
                                            spacing=0,
                                            controls=[
                                                Container(
                                                    width=350,
                                                    height=40,
                                                    border_radius=BorderRadius(top_right=0,top_left=5,bottom_left=5,bottom_right=0),
                                                    content=TextField(
                                                        border=InputBorder.NONE,
                                                        hint_text='Хочу найти...',
                                                        hint_style=TextStyle(
                                                            size=12
                                                        ),
                                                        content_padding=padding.only(bottom=10, left=20),
                                                        text_style=TextStyle(
                                                            color='#ff14a1',
                                                            size=17,
                                                            weight=FontWeight.W_500
                                                        )
                                                    )
                                                ),
                                                Container(
                                                    height=40,
                                                    width=40,
                                                    bgcolor='#C5007F',
                                                    border_radius=BorderRadius(top_right=5,top_left=0,bottom_left=0,bottom_right=5),
                                                    content=Icon(
                                                        icons.SEARCH
                                                    )
                                                ),
                                                Row(
                                                    spacing=15,
                                                    controls=[
                                                        Container(
                                                            alignment=alignment.center,
                                                                content=Stack(
                                                                    controls=[
                                                                        Container(
                                                                            content=Icon(
                                                                                icons.NOTIFICATIONS,
                                                                                size=28,
                                                                                color='#c70077',
                                                                            ),
                                                                            margin=10,
                                                                        ),
                                                                        Container(
                                                                            height=15,
                                                                            width=18,
                                                                            bgcolor=None,
                                                                            right=3,
                                                                            top=11,
                                                                            alignment=alignment.center,
                                                                            content=Text(
                                                                                value='1',
                                                                                size=12,
                                                                            )
                                                                        )
                                                                    ]
                                                                ),

                                                        ),
                                                        Container(
                                                            height=40,
                                                            width=1,
                                                            bgcolor='#C5007F',
                                                        ),
                                                        CircleAvatar(
                                                            foreground_image_url="",
                                                            radius=15,
                                                        )
                                                    ]
                                                )

                                            ]
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )