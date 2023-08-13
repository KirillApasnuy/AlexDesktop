from flet import *
from utils.validation import Validator
from utils.color import *
import requests
import json
from servic.generatePickleFile import *

class CreateQuiz(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.padding = 0
        self.alignment = alignment.center
        self.expand = True
        self.validator = Validator()
        self.bgcolor = bgc
        self.error_border = border.all(width=1, color='red', )
        self.name_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Предмет',
                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white'
                )
            ),
            border_radius=20,
        )
        self.topic_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Тема',
                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white'
                )
            ),
            border_radius=20,
        )
        self.value_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Содержание',
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
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value='Создание викторины',
                                size=20,
                                font_family='RobotoSlab',
                                color='white',
                                text_align='center'
                            ),
                            Container(height=0),
                            self.name_box,
                            self.topic_box,
                            self.value_box,
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
                                            on_click=lambda _: self.page.go('/me/quiz')
                                        ),

                                        Container(
                                            alignment=alignment.center,

                                            bgcolor='#ff00a6',
                                            border_radius=15,
                                            width=370,
                                            height=40,
                                            content=Text(
                                                value='Добавить',
                                                color='white',
                                                size=18,
                                            ),
                                            on_click=self.createQuiz
                                        ),
                                    ]
                                )
                            )

                        ]

                    )
                )
            ]
        )
    def createQuiz(self, e):
        token = generatePickleFile()
        print(token)
        if token != None:
            print('есть токен в функции')
            url = 'http://localhost:5000/alex/quiz/'
            name = self.name_box.content.value
            topic = self.topic_box.content.value
            value = self.value_box.content.value
            headers = {'Authorization': 'Bearer {}'.format(token)}
            payload = {'subject': name,
                       'topic': topic,
                       'value': value}
            res = requests.post(url=url, json=payload, headers=headers)
            values = res.text
            print(values)
            json_value = json.loads(values[values.index('{'):values.rindex('}') + 1])
            print(json_value)
            message = json_value['message']
            self.page.snack_bar = SnackBar(
                Text(
                    message
                )

            )
            self.page.snack_bar.open = True
            self.page.update()
