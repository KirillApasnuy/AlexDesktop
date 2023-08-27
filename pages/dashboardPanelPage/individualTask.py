import json

# import tts
from readAnswel import *
from flet import *
from utils.color import *
import random
import requests
import smtplib
import pickle

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
url = "http://localhost:5000/alex/individualTask"  # URL, откуда вы хотите получить данные

response = requests.get(url)  # Выполнить GET-запрос
data = json.loads(response.text)
i = random.randrange(0, len(data))
data1 = data[i]
i = random.randrange(0, len(data))
data2 = data[i]
i = random.randrange(0, len(data))
data3 = data[i]
i = random.randrange(0, len(data))
data4 = data[i]
i = random.randrange(0, len(data))
data5 = data[i]
i = random.randrange(0, len(data))
data6 = data[i]
i = random.randrange(0, len(data))
data7 = data[i]
i = random.randrange(0, len(data))
data8 = data[i]
value = ''
print(data)  # Вывести массив данных
subject1 = data1['subject']
topic1 = data1['topic']
value1 = data1['value']
subject2 = data2['subject']
topic2 = data2['topic']
value2 = data2['value']
subject3 = data3['subject']
topic3 = data3['topic']
value3 = data3['value']
subject4 = data4['subject']
topic4 = data4['topic']
value4 = data4['value']
subject5 = data5['subject']
topic5 = data5['topic']
value5 = data5['value']
subject6 = data6['subject']
topic6 = data6['topic']
value6 = data6['value']
subject7 = data7['subject']
topic7 = data7['topic']
value7 = data7['value']
subject8 = data8['subject']
topic8 = data8['topic']
value8 = data8['value']
answel = readAnswer()
class IndividualTask(Container):

    def __init__(self, page:Page):
        super().__init__()
        data = requests.get('http://localhost:5000/alex/individualTask')
        print(data)
        page.padding = 0
        self.expand = True
        self.bgcolor = bgc,
        self.answer_box = Container(

            content=TextField(


                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=5, bottom=80, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Введите ответ',

                value=answel,

                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white',

                ),
            ),
            border_radius=20,
        )

        self.create = Container(
                width=40,
                height=40,
                bgcolor='#C5007F',
                border_radius=30,
                alignment=alignment.center,
                padding=5,
                content=Icon(
                icons.ADD
                ),
                on_click=lambda _: self.page.go(
                '/me/individualtask/create')
        )
        self.tasks = Column(
            height=1000,
            scroll='auto',

        )
        # left nav bar
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
                                            on_click=lambda _: self.page.go('/login'),
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
                #top nav bar
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
                            #main box
                            Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content = Column(

                                                    horizontal_alignment='center',
                                                            controls=[
                                                                Text(
                                                                    value=subject1,
                                                                    size=25,
                                                                    color='white'
                                                                ),
                                                                Text(
                                                                    value=topic1,
                                                                    size=23,
                                                                    color='white'
                                                                ),
                                                                Text(
                                                                    value=value1,
                                                                    size=21,
                                                                    color='white',
                                                                ),
                                                                self.answer_box,
                                                                Container(
                                                                    # margin=5,
                                                                    width=100,
                                                                    height=40,
                                                                    margin=Margin(left=10, right=10, bottom=10, top=50),
                                                                    border_radius=12,
                                                                    alignment=alignment.center,
                                                                    bgcolor='#ff1ca4',
                                                                    content=Text(
                                                                        value='Отправить',
                                                                        color='white',
                                                                        size=16,
                                                                    ),
                                                                    on_click=lambda _:self.pushTask(e=value1)
                                                                )
                                                            ]
                                                        )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject2,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic2,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value2,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value2)
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]



                                    ),
                                    Column(
                                        controls=[
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject3,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic3,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value3,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value3)
                                                        )
                                                    ]
                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject4,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic4,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value4,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value4)
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]

                                    ),
                                    Column(
                                        controls=[
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject5,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic5,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value5,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value5)
                                                        )
                                                    ]
                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject6,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic6,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value6,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value6)
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]

                                    ),
                                    Column(
                                        controls=[
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject7,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic7,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value7,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value7)
                                                        )
                                                    ]
                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=450,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(

                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject8,
                                                            size=25,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=topic8,
                                                            size=23,
                                                            color='white'
                                                        ),
                                                        Text(
                                                            value=value8,
                                                            size=21,
                                                            color='white',
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            # margin=5,
                                                            width=100,
                                                            height=40,
                                                            margin=Margin(left=10, right=10, bottom=10, top=50),
                                                            border_radius=12,
                                                            alignment=alignment.center,
                                                            bgcolor='#ff1ca4',
                                                            content=Text(
                                                                value='Отправить',
                                                                color='white',
                                                                size=16,
                                                            ),
                                                            on_click=lambda _:self.pushTask(e=value8)
                                                        )
                                                    ]
                                                )
                                            ),
                                        ]

                                    ),

                                    self.create,
                                ]
                            )
                        ]
                    )
                )
            ]
        )

    def pushTask(self, e):
        # print(e)
        # e = int(e)
        # e = data[e]['value']
        print(e)
        try:
            with open('../name.pickle', 'rb') as file:
                schoolboy = pickle.load(file)
            answelTask = self.answer_box.content.value
            text = f'{schoolboy}. {e}: {answelTask}.'
            emailAlex = 'alexvoiceassistent@yandex.ru'
            passwordAlex = 'ejivdpmxsbacfvxo'
            msg = MIMEMultipart()
            msg['From'] = emailAlex
            msg['To'] = emailAlex
            msg['Subject'] = 'Ответ на задание'
            msg.attach(
                MIMEText(text, 'plain')
            )

            server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            server.ehlo(emailAlex)
            server.login(emailAlex, passwordAlex)
            server.auth_plain()
            server.send_message(msg)
            server.quit()
            # tts.va_speak('Ответ отправлен на почту учителя')
            self.page.snack_bar = SnackBar(
                    Text(
                        'Ответ отправлен на почту учителя'
                    )
                )
            self.page.snack_bar.open = True
            self.page.update()
        except:
            # tts.va_speak('ОШИБКА Не удалось отправить сообщение')
            self.page.snack_bar = SnackBar(
                Text(
                    'ОШИБКА Не удалось отправить сообщение =( '
                )
            )
            self.page.snack_bar.open = True
            self.page.update()
