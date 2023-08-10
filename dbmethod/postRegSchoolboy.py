import requests

def postRegSchoolboy(imgFace, password, email):
    print('начало post(reg)')
    name = imgFace.split("_")
    first_name = name[0]
    last_name = name[1]
    url = "http://localhost:5000/api/schoolboy/registration"
    payload = {
    "first_name": first_name,
    "last_name": last_name,
    "email": email,
    "imgFace": imgFace,
    "password": password,
    "role": 'admin'
    }
    print(payload)
    res = requests.post(url, json=payload)
    print('отправленно успешно!')
    print(res.text)
