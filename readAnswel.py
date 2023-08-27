import pickle
def readAnswer():
    with open('../answer.pickle', 'rb') as file:
        answer = pickle.load(file)
    return answer
# print(readAnswer())