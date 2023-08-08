from flet import *
from utils.color import *
from takePhoto import take_screenshot_from_cam
import cv2
import os
import time
# import flet as ft
class Singup(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.padding = 0
        self.alignment = alignment.center
        self.expand = True
        self.bgcolor ='#3d3d3d'
        self.firstname_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Введите имя',
                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white'
                )

            ),
            border_radius=20,
        )
        self.lastname_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Введите фамилию',
                cursor_color=input_col,
                text_style=TextStyle(
                    size=16,
                    color='white'
                )
            ),
            border_radius=20,
        )
        self.email_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14, color=input_col,

                ),
                hint_text='Введите свой email',
                cursor_color='#c9c9c9',
                text_style=TextStyle(
                    size=16,
                    color='white'
                ),
            ),
            border_radius=20,
        )
        self.imgFace_box = Container(

            content=TextField(
                border=InputBorder.NONE,
                bgcolor='#a6006c',
                content_padding=padding.only(top=0, bottom=0, left=20, right=20),
                hint_style=TextStyle(
                    size=14,
                    color=input_col,
                ),
                hint_text='Пропишите ИФ на лат. пример: kirill_beziazukov',
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
                hint_text='Введите свой пароль',
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
                                value='Регистрация',
                                size=20,
                                font_family='RobotoSlab',
                                color='white',
                                text_align='center'
                            ),
                            self.firstname_box,

                            self.lastname_box,
                            self.imgFace_box,
                            self.email_box,
                            self.password_box,
                            Container(height=0),

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
                                            width=205,
                                            height=40,
                                            content=Text(
                                                value='Зарегистрироваться!',
                                                color='white',
                                                size=18,
                                            ),
                                            on_click=self.singup,
                                        ),
                                        Container(
                                            alignment=alignment.center,

                                            bgcolor='#ff00a6',
                                            border_radius=15,
                                            width=155,
                                            height=40,
                                            content=Text(
                                                value='Сделать фото',
                                                color='white',
                                                size=18,
                                            ),
                                            on_click=self.photo,
                                        ),
                                    ]
                                )
                            )



                        ]

                    )
                )
            ]
        )

    def singup(self, e):
        pass

    def photo(self, e):
        self.event_handlers
        print(e)
        take_screenshot_from_cam()
        # cap = cv2.VideoCapture(0)
        # count = 0
        #
        # if not os.path.exists("dataset_from_cam"):
        #     os.mkdir("dataset_from_cam")
        #
        # while True:
        #     fps = cap.get(cv2.CAP_PROP_FPS)
        #     multiplier = fps * 3
        #     # print(fps)
        #     ret, frame = cap.read()
        #
        #     if ret:
        #         frame_id = int(round(cap.get(1)))
        #         # print(frame_id)
        #         cv2.imshow("frame", frame)
        #         k = cv2.waitKey(20)
        #         cv2.imwrite(f"dataset_from_cam/{count}.jpg", frame)
        #         time.sleep(3)
        #
        #         if k == ord("e"):
        #
        #             cv2.imwrite(f"dataset_from_cam/{count}.jpg", frame)
        #             time.sleep(10)
        #             count += 1
        #
        #         elif k == ord("q") or count == 1:
        #             break
        #     else:
        #         print("[ERROR]Can't get the frame")
        #         break
        #
        # cap.release()
        # cv2.destroyAllWindows()