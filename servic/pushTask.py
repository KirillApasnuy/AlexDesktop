import tts
import pickle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def pushTask(e, data, answelTask):
    e = data[e]['value']
    print(e)
    try:
        with open('../name.pickle', 'rb') as file:
            schoolboy = pickle.load(file)

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
        tts.va_speak('Ответ отправлен на почту учителя')
    except:
        tts.va_speak('Ошибка, не удалось отправить сообщение =(')