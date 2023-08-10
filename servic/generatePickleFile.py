# import os
# import pickle
#
# def generatePickleFile(token):
#     print('начало')
#     if os.path.exists('../token.pickle'):
#         os.remove('token.pickle')
#     with open(f"../token.pickle", "wb") as file:
#         file.write(pickle.dumps(token))
#     print(f"[info] File token.pickle successfuly created")