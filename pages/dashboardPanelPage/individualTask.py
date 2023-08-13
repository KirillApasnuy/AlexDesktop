import os

import requests
from flet import *
from utils.color import *
import pickle
from flask import Flask, render_template
class IndividualTask(Container):
    def __init__(self, page:Page):
        super().__init__()
        page.padding = 0
        self.expand = True
        self.bgcolor = bgc,
        self.getIndividualTask = Container(

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
                                    value='Предметы',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                ),
                                on_click=lambda _: self.page.go('/me/subject')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Учителя',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                ),
                                on_click=lambda _: self.page.go('/me/teacher')
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Администрация',
                                    size=16,
                                    color='white',
                                    weight=FontWeight.W_300,
                                ),
                                on_click=lambda _: self.getAdmin
                            ),
                            Divider(
                                color='white',
                                height=0.5,
                                thickness=.5
                            ),
                            Container(
                                Text(
                                    value='Магазин игр',
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
                            #main box
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
                                                          width=40,
                                                          height=40,
                                                          bgcolor='#C5007F',
                                                          border_radius=30,
                                                          alignment=alignment.center,
                                                          padding=5,
                                                          content=Icon(
                                                              icons.ADD
                                                          ),
                                                          on_click=lambda _: self.page.go('/me/individualtask/create')
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


# import requests
# from flet import *
# from utils.color import *
# import pickle
# from flask import Flask, render_template
# class IndividualTask(Container):
#     def __init__(self, page:Page):
#         super().__init__()
#         page.padding = 0
#         self.expand = True
#         self.bgcolor = bgc,
#         self.getIndividualTask = Container(
#
#         )
#         # left nav bar
#         self.content = Row(
#             spacing=0,
#             controls=[
#                 Container(
#                     width=220,
#                     bgcolor='#C5007F',
#                     padding=padding.only(top=20, left=10, right=10),
#
#                     content=Column(
#                         controls=[
#                             Row(
#                                 controls=[
#                                     Icon(
#                                         icons.PERSON,
#                                         size=50,
#                                         color='white'
#                                     ),
#                                     Text(
#                                         'Individual Task',
#                                         size=16,
#                                         color='white',
#                                         weight='bold',
#                                         line_height=50
#                                     )
#                                 ]
#                             ),
#                             Row(
#                                 controls=[
#                                     Text(
#                                         'Dashboard',
#                                         size=14,
#                                         color='white',
#                                         weight='bold',
#                                         line_height=40
#                                     )
#                                 ]
#                             ),
#
#                             Row(
#                                 controls=[
#                                     Text(
#                                         'Create Task',
#                                         size=14,
#                                         color='white',
#                                         weight='bold',
#                                         line_height=40
#                                     )
#                                 ]
#                             ),
#                             Row(
#                                 controls=[
#                                     Text(
#                                         'View Task',
#                                         size=14,
#                                         color='white',
#                                         weight='bold',
#                                         line_height=40
#                                     )
#                                 ]
#                             ),
#                             Row(
#                                 controls=[
#                                     Text(
#                                         'My Profile',
#                                         size=14,
#                                         color='white',
#                                         weight='bold',
#                                         line_height=40
#                                     )
#                                 ]
#                             ),
#                             Row(
#                                 controls=[
#                                     Text(
#                                         'Logout',
#                                         size=14,
#                                         color='white',
#                                         weight='bold',
#                                         line_height=40
#                                     )
#                                 ]
#                             ),
#                         ]
#                     )
#                 ),
#                 Container(
#                     width=100,
#                     bgcolor='white'
#                 ),
#                 Container(
#                     width=860,
#                     padding=padding.only(top=20, left=20, right=20),
#                     content=Column(
#                         controls=[
#                             Row(
#                                 controls=[
#                                     Text(
#                                         'View Task',
#                                         size=20,
#                                         weight='bold',
#                                         line_height=40
#                                     )
#                                 ],
#                                 spacing=0,
#                                 padding=padding.only(bottom=20)
#                             ),
#                             Row(
#                                 controls=[
#                                     Column(
#                                         controls=[
#                                             Text(
#                                                 'Task123',
#                                                 size=16,
#                                                 weight='bold',
#                                                 line_height=35
#                                             ),
#                                             Text(
#                                                 'Description: ',
#                                                 size=12,
#                                                 weight='bold',
#                                                 line_height=30
#                                             ),
#                                             Text(
#                                                 'This is task description',
#                                                 size=12,
#                                                 line_height=20
#                                             ),
#                                             Text(
#                                                 'Due Date: ',
#                                                 size=12,
#                                                 weight='bold',
#                                                 line_height=30
#                                             ),
#                                             Text(
#                                                 '11/11/2020',
#                                                 size=12,
#                                                 line_height=20
#                                             ),
#                                             Text(
#                                                 'Assigned To: ',
#                                                 size=12,
#                                                 weight='bold',
#                                                 line_height=30
#                                             ),
#                                             Text(
#                                                 'John Doe',
#                                                 size=12,
#                                                 line_height=20
#                                             ),
#                                             Text(
#                                                 'Status: ',
#                                                 size=12,
#                                                 weight='bold',
#                                                 line_height=30
#                                             ),
#                                             Text(
#                                                 'Completed',
#                                                 size=12,
#                                                 line_height=20,
#                                                 color='green'
#                                             ),
#                                         ],
#                                         spacing=0,
#                                     )
#                                 ]
#                             )
#                         ],
#                         spacing=0
#                     )
#                 )
#             ]
#         )
#
#     def render(self):
#         # make get request to fetch data
#         response = requests.get('https://example.com/get_individual_task')
#         if response.status_code == 200:
#             task_data = response.json()
#             # update task details from response
#             self.content.controls[2].controls[1].controls[0].controls[0].text = task_data['task_name']
#             self.content.controls[2].controls[1].controls[0].controls[2].controls[1].text = task_data['description']
#             self.content.controls[2].controls[1].controls[0].controls[4].controls[1].text = task_data['due_date']
#             self.content.controls[2].controls[1].controls[0].controls[6].controls[1].text = task_data['assigned_to']
#             self.content.controls[2].controls[1].controls[0].controls[8].controls[1].text = task_data['status']
#
#         return super().render()
#
#




