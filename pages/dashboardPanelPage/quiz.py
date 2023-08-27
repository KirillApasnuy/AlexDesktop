import os
import random
from flet import *

# import tts
from utils.color import *
import requests
import json
import simpleaudio as sa
CDIR = os.getcwd()
def play(phrase):
    filename = f"{CDIR}\\sound\\"

    if phrase == "win":
        filename += f"win.wav"
    elif phrase == "fail":
        filename += f"fail.wav"

    wave_obj = sa.WaveObject.from_wave_file(filename)
    wave_obj.play()

url = "http://localhost:5000/alex/quiz"  # URL, откуда вы хотите получить данные

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
count = 0
quiz = {}
while count < len(data):
    value = data[count]['value']
    answel = data[count]['answel']
    quiz[value] = answel
    count += 1
print(quiz)
class Quiz(Container):
    def __init__(self, page:Page):
        super().__init__()
        print('токеннн')
        page.padding = 0
        self.expand = True
        self.bgcolor = bgc,
        self.answer_box = Container(
            width=250,

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=5, bottom=80, left=20, right=20),

                hint_style=TextStyle(
                    size=14,
                    color=input_col,

                ),
                hint_text='Ваш ответ',
                cursor_color=input_col,
                width=200,
                text_style=TextStyle(
                    size=16,
                    color='white',
                ),
            ),
            border_radius=20,
        )
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
                            Row(
                                controls=[
                                    Column(
                                        controls=[
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=400,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=10,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject1,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic1,
                                                            size=25,
                                                        ),
                                                        Text(
                                                            value=value1,
                                                            size=20,
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value1)
                                                        )
                                                    ]

                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=400,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=10,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject2,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic2,
                                                            size=25,
                                                        ),
                                                        Text(
                                                            value=value2,
                                                            size=20
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value2)
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
                                                height=400,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=10,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject3,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic3,
                                                            size=25
                                                        ),
                                                        Text(
                                                            value=value3,
                                                            size=20
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value3)
                                                        )
                                                    ]

                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=400,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=10,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject4,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic4,
                                                            size=25,
                                                        ),
                                                        Text(
                                                            value=value4,
                                                            size=20,
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value4)
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
                                                height=400,
                                                bgcolor='#C5007F',
                                                padding=10,
                                                alignment=alignment.center,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject5,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic5,
                                                            size=25,
                                                        ),
                                                        Text(
                                                            value=value5,
                                                            size=20,
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value5)
                                                        )
                                                    ]

                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=400,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=10,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject6,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic6,
                                                            size=25,
                                                        ),
                                                        Text(
                                                            value=value6,
                                                            size=20,
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value6)
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
                                                height=400,
                                                bgcolor='#C5007F',
                                                padding=10,
                                                alignment=alignment.center,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject7,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic7,
                                                            size=25,
                                                        ),
                                                        Text(
                                                            value=value7,
                                                            size=20,
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value7)
                                                        )
                                                    ]

                                                )
                                            ),
                                            Container(
                                                border_radius=20,
                                                margin=10,
                                                width=300,
                                                height=400,
                                                bgcolor='#C5007F',
                                                alignment=alignment.center,
                                                padding=10,
                                                # padding=padding.only(left=5, right=5, top=10, bottom=10),
                                                content=Column(
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        Text(
                                                            value=subject8,
                                                            size=30,
                                                        ),
                                                        Text(
                                                            value=topic8,
                                                            size=25
                                                        ),
                                                        Text(
                                                            value=value8,
                                                            size=20,
                                                        ),
                                                        self.answer_box,
                                                        Container(
                                                            width=150,
                                                            height=50,
                                                            border_radius=10,
                                                            bgcolor='#ff1ca4',
                                                            margin=Margin(left=75, right=75, bottom=10, top=50),
                                                            padding=5,
                                                            content=Text(
                                                                text_align='center',

                                                                value='Проверить',
                                                                color='white',
                                                                size=20,
                                                            ),
                                                            on_click=lambda _: self.cheakAnswel(e=value8)
                                                        )
                                                    ]

                                                )
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    def logout(self,e):
        os.remove('../token.pickle')


    def cheakAnswel(self, e):
        answelSchoolboy = self.answer_box.content.value
        false = 0
        for i, j in quiz.items():
            if answelSchoolboy == j:
                print('true')
            else:
                false += 1
        if false == len(quiz):
            play('fail')
            # tts.va_speak('Не грусти. попробуй ещё раз!')

        else:
            play('win')
            # tts.va_speak('Правильный ответ!. Ты очень умный!')

