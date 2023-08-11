import requests
import json
import pickle
def postLoginSchoolboy(name, password):

    print('начало post(login)')
    url = "http://localhost:5000/alex/schoolboy/login"
    name = name.split("_")
    first_name = name[0]
    last_name = name[1]

    try:
        payload = {
            'first_name': first_name,
            'last_name': last_name,
            'password': password
        }
        print(payload)
        print('отправленно успешно')

        res = requests.post(url, json=payload)
        values = res.text
        json_value = json.loads(values[values.index('{'):values.rindex('}') + 1])
        token = json_value['token']
        print('1')
        # with open('token.pickle', 'wb') as file:
        #     pickle.dump(token, file)
        print(token)


        return token
    except:
        return None
