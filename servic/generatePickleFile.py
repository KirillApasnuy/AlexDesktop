import pickle

def generatePickleFile():
    print('начало')
    with open('token.pickle', 'rb') as file:
        return pickle.load(file)
