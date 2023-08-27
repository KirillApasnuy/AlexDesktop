import pickle
def readName():
    with open('../name.pickle', 'rb') as file:
        name = pickle.load(file)
    return name

        # print(pickle.load(file))