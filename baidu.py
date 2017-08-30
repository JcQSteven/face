from aip import AipFace
from pprint import pformat

APP_ID = '10073751'
API_KEY = 'PWccFKGnxVjYqqFImtArYdcc'
SECRET_KEY = 'dzIwIevmMm6FcOysczPD5CkAyMCrbkMS'

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(file_path):
    with open(file_path,'rb') as fp:
        return fp.read()




def print_result(hit, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(v): encode(k) for (v, k) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj

    print hit
    result = encode(result)
    print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))

def adduser(image):
    result=aipFace.addUser(
        'jcq',
        'user info',
        'group1',
        image,
        )
    return result
def verifyuser(img):
    result=aipFace.verifyUser(
              uid='jcq',
              groupId='group1',
              image=img,
            )
def identifyuser(img):
    result=aipFace.identifyUser(
              groupId='group1',
              image=img,
            )
#result=aipFace.detect(get_file_content('xk.jpeg'))
#result=aipFace.match([get_file_content('demo.jpeg'),get_file_content('demo_c.jpeg')])
#print_result('getuser',aipFace.getUser('jcq'))
#print aipFace.deleteUser('jcq')
print verifyuser(get_file_content('demo.jpeg'))
#print identifyuser(get_file_content('demo.jpeg'))
# print adduser(get_file_content('demo_c.jpeg'))