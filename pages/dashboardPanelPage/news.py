import os
from flet import *
from utils.color import *
import pickle
import requests
class News(Container):
    def __init__(self, page:Page):
        super().__init__()
        print('токеннн')
        page.padding = 0
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
                                        color='white',
                                    ),

                                ]
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Главная',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                    # font_family='RobotoSlab',

                                ),

                                on_click=lambda _: self.page.go('/me')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Задание недели',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                    # font_family='RobotoSlab',

                                ),

                                on_click=lambda _: self.page.go('/me/individualtask')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Викторина',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                ),
                                on_click=lambda _: self.page.go('/me/quiz')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Игры',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                ),
                                on_click=lambda _: self.page.go('/me/gameshop')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Новости',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                ),
                                on_click=lambda _: self.page.go('/me/news')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                margin=Margin(left=0,right=0,bottom=0,top=470),
                                height=100,
                                bgcolor='#f09',
                                border_radius=5,
                                alignment=alignment.bottom_center,
                                content=Column(
                                    horizontal_alignment='center',
                                    alignment='center',
                                    controls=[
                                        Container(
                                            on_click=lambda _: self.page.go('/login') & self.logout,
                                            alignment=alignment.center,
                                            height=35,
                                            width=110,
                                            border_radius=5,
                                            bgcolor='#ff1ca4',
                                            content=Text(
                                                value='Выйти',
                                                color='white',
                                                size=14,
                                                weight=FontWeight.W_300,
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
                                margin=Margin(left=5, top=5, bottom=0, right=5),
                                height=70,
                                shadow=BoxShadow(
                                    spread_radius=2,
                                    color=bgc
                                ),
                                padding=padding.only(top=10, bottom=10, right=10, left=30),
                                bgcolor=bgc,
                                content=Row(
                                    # alignment='spaceBetween',
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
                                                        content_padding=padding.only(bottom=10, left=20, top=0,right=10),
                                                        text_style=TextStyle(
                                                            color='#ff14a1',
                                                            size=16,
                                                            weight=FontWeight.W_600
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
                                                    # alignment=alignment.top_right,

                                                    spacing=15,
                                                    controls=[
                                                        Container(
                                                            margin=Margin(left=800, top=0,right=10,bottom=0),
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
                                                        Container(
                                                            margin=12,
                                                            height=40,
                                                            content=Text(
                                                                value=f'Баланс равен: 0',
                                                                size=16,
                                                                text_align='center',
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
                                                ),

                                            ]
                                        )

                                    ]
                                )
                            ),

                            Column(
                                expand=True,
                                scroll='auto',
                                controls=[
                                    Container(
                                      padding=20,
                                      content=Row(
                                          alignment='spaceBetween',
                                          controls=[
                                              Row(
                                                  controls=[
                                                      Container(
                                                          border_radius=20,
                                                          bgcolor='#C5007F',
                                                          padding=10,
                                                          content=Text(
                                                              value='Пока что нечем тебя порадовать =(',
                                                              color='white',
                                                              size=35,
                                                          )
                                                      )
                                                  ]
                                              ),
                                          ]

                                      )
                                    ),
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    def logout(self,e):

        os.remove('../token.pickle')

    def resNews(self, e):
        url = "https://real-time-news-data.p.rapidapi.com/search"

        querystring = {"query": "IT", "country": "RU", "lang": "ru"}

        headers = {
            "X-RapidAPI-Key": "4ea3651a79mshbcc147a1c772537p1f6fc0jsnd2b70bc377bd",
            "X-RapidAPI-Host": "real-time-news-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
